import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np
from sensor_msgs.msg import Imu

class Nodo(object):
    def __init__(self):
        # Params
        self.image = cv2.imread("pipe5.png")
        self.br = CvBridge()
        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(100)

        # Publishers
        self.pub = rospy.Publisher("cylinder_detection/camera/image", Image, queue_size=10)
        self.IMUpub = rospy.Publisher("QuadrotorAlpha/imu", Imu, queue_size=10)
        # self.imu = MPU9250()
        # self.imu.initialize()
        self.msg = Imu()
        self.IMUMesssage()

    def IMUMesssage(self):
        self.msg.orientation.w = 1
        self.msg.orientation.x = 1
        self.msg.orientation.y = 1
        self.msg.orientation.z = 1
        self.msg.angular_velocity.x = 1
        self.msg.angular_velocity.y = 1
        self.msg.angular_velocity.z = 1
        self.msg.linear_acceleration.x = 1
        self.msg.linear_acceleration.y = 1
        self.msg.linear_acceleration.z = 1
        pass

    def start(self):
        rospy.loginfo("Timing images")
        #rospy.spin()
        while not rospy.is_shutdown():
            rospy.loginfo('publishing image')
            #br = CvBridge()
            if self.image is not None:
                self.pub.publish(self.br.cv2_to_imgmsg(self.image))
            for i in range(100):
                self.IMUpub.publish(self.msg)
                self.loop_rate.sleep()

if __name__ == '__main__':
    rospy.init_node("imagetimer", anonymous=True)
    my_node = Nodo()
    my_node.start()