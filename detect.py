# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Main script to run the object detection routine."""
import argparse
import sys
import time

import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

import utils
import robot
import sonar
from gpiozero import Servo

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
import RPi.GPIO as GPIO


def run(model: str, camera_id: int, width: int, height: int, num_threads: int,
        enable_edgetpu: bool) -> None:
    try:
        """Continuously run inference on images acquired from the camera.
        Args:
            model: Name of the TFLite object detection model.
            camera_id: The camera id to be passed to OpenCV.
            width: The width of the frame captured from the camera.
            height: The height of the frame captured from the camera.
            num_threads: The number of CPU threads to run the model.
            enable_edgetpu: True/False whether the model is a EdgeTPU model.
        """

        # Start capturing video input from the camera
        cap = cv2.VideoCapture(camera_id)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap_xcenter=cap.get(cv2.CAP_PROP_FRAME_WIDTH) /2


        # Initialize the object detection model
        base_options = core.BaseOptions(
            file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)
        detection_options = processor.DetectionOptions(
            max_results=3, score_threshold=0.3)
        options = vision.ObjectDetectorOptions(
            base_options=base_options, detection_options=detection_options)
        detector = vision.ObjectDetector.create_from_options(options)

        # initialize servo
        servo = Servo(16, pin_factory=factory)
        servo.mid()

        # Continuously capture images from the camera and run inference
        while cap.isOpened():

            # check sonar distance
            distance=sonar.distance()
            #print("distance", distance)
            if(distance<30):
                robot.stop()
                time.sleep(1)
                print("robot stop -> detection stopped")
            else:
                # move servo-webcam 
                if servo.value ==1.0: #servo is in position left
                    servo.mid()
                    print(servo.value)
                elif servo.value ==-1.0: #servo is in position right
                    servo.max()
                    print(servo.value)
                elif servo.value == 0.0 or servo.value==-0.0: #servo is neutral position
                    servo.min()
                    print(servo.value)

                # object detection for 10 seconds
                t_end = time.time() + 10
                followed=False
                detection_result=None
                while not followed and time.time() < t_end:
                    detection_result = do_detection(cap, detector )
                        # move the robot if target is detected
                    for detection in detection_result.detections:
                        category = detection.categories[0]
                        print("category", category)
                        category_name = category.category_name
                        if not followed and category_name == "person" and category.score>0.80:
                            print("OBJECT DETECTED")
                            follow_detected_object(servo, cap)
                            # stop following
                            followed=True
                            print("stop following")
                            cap.open(1)
                            break
    # Stop the program if CTRL+C is pressed.
    except KeyboardInterrupt:
        print("Program is stopped")
        cap.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()
        sys.exit()

def follow_detected_object(servo, cap):
    try:
        # check sonar distance
        distance=sonar.distance()
        while distance>30:
            if servo.value ==1.0: #servo is in position left
                print("move robot left")
                robot.forwardleft(0.5)
                servo.mid()
            elif servo.value ==-1.0: #servo is in position right
                print("move robot right")
                robot.forwardright(0.5)
                servo.mid()
            elif servo.value == 0.0 or servo.value == -0.0: #servo is neutral position
                print("move robot center")
                robot.forward(0.05)
            distance=sonar.distance()
        
        # stop robot if distance is less than 30 cm
        robot.stop()
        time.sleep(1)
        print("robot stop")
        return
        # Stop the program if CTRL+C is pressed.
    except KeyboardInterrupt:
        print("Program is stopped")
        cap.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()
        sys.exit()

def do_detection(cap, detector):
    # Variables to calculate FPS
    counter, fps = 0, 0
    start_time = time.time()

    # Visualization parameters
    row_size = 20  # pixels
    left_margin = 24  # pixels
    text_color = (0, 0, 255)  # red
    font_size = 1
    font_thickness = 1
    fps_avg_frame_count = 10
    
    success, image = cap.read()
    height, width, channels = image.shape
    if not success:
        sys.exit(
            'ERROR: Unable to read from webcam. Please verify your webcam settings.'
        )

    counter += 1
    image = cv2.flip(image, 1)

    # Convert the image from BGR to RGB as required by the TFLite model.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a TensorImage object from the RGB image.
    input_tensor = vision.TensorImage.create_from_array(rgb_image)

    # Run object detection estimation using the model.
    detection_result = detector.detect(input_tensor)

    # Draw keypoints and edges on input image
    #image = utils.visualize(image, detection_result)
    # Calculate the FPS
#    if counter % fps_avg_frame_count == 0:
       # end_time = time.time()
       # fps = fps_avg_frame_count / (end_time - start_time)
       # start_time = time.time()
    
        # Show the FPS
       # fps_text = 'FPS = {:.1f}'.format(fps)
       # text_location = (left_margin, row_size)
       # cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
        #            font_size, text_color, font_thickness)

    #cv2.imshow('object_detector', image)
    return detection_result

def robot_direction(boundingbox_center,cap_xcenter):
    # 4) adjust robot direction based on bounding box
    if (boundingbox_center > cap_xcenter+30): # 30 is the threshold (intorno)
        print("robot moves left")
        robot.forwardleft(0.05)
    elif (boundingbox_center < cap_xcenter-30): # 30 is the threshold (intorno)
        print("robot moves right")
        robot.forwardright(0.05)

def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Path of the object detection model.',
      required=False,
      default='efficientdet_lite0.tflite')
  parser.add_argument(
      '--cameraId', help='Id of camera.', required=False, type=int, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      type=int,
      default=640)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      type=int,
      default=480)
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run the model.',
      required=False,
      type=int,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='Whether to run the model on EdgeTPU.',
      action='store_true',
      required=False,
      default=False)
  args = parser.parse_args()

  run(args.model, int(args.cameraId), args.frameWidth, args.frameHeight,
      int(args.numThreads), bool(args.enableEdgeTPU))


if __name__ == '__main__':
  main()

