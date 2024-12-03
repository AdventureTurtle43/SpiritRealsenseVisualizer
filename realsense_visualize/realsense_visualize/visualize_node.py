#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VisualizeNode(Node):
    def __init__(self):
        super().__init__('image_node')
        self.subscription = self.create_subscription(
            Image,
            '/device_0/sensor_1/Color_0/image/data',  # Change this to your image topic
            self.listener_callback,
            10
        )
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        # Convert the ROS image to OpenCV format
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        # Display the image using OpenCV
        cv2.imshow('Image', cv_image)
        cv2.waitKey(1)  # Refresh the image window

def main(args=None):
    rclpy.init(args=args)
    image_viewer = VisualizeNode()
    rclpy.spin(image_viewer)

    # Cleanup on shutdown
    image_viewer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()