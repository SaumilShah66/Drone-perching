import rospy
from std_msgs.msg import String
from cylinder_msgs.msg import CylinderPose, ParallelPlane
from geometry_msgs.msg import PoseStamped, Pose
import numpy as np 
from math import atan2
from scipy.spatial.transform import Rotation as R

class Perch():
    def __init__(self):
        rospy.init_node('Percher', anonymous=True)
        subTopic = "/QuadrotorAlpha/cylinder_pose"
        subTopic1 =  "/QuadrotorAlpha/image_features_pp"
        poseTopic = "/firefly/vi_sensor/ground_truth/pose"
        pubTopic = "/firefly/command/pose"
        self.DronePosition = np.array([0.0,0.0,0.0])
        self.messageSent = False
        self.pub = rospy.Publisher(pubTopic, PoseStamped, queue_size=10)    
        self.offsetZ = 0.1
        self.goal = PoseStamped()
        self.rate = rospy.Rate(10)
        rospy.Subscriber(subTopic, CylinderPose, self.callback)
        rospy.Subscriber(poseTopic, Pose, self.gotpose)
        # rospy.Subscriber(subTopic1, ParallelPlane, self.planebased)
        rospy.spin()

    def gotpose(self, posedata):
        # print("got pose")
        x = posedata.position.x
        y = posedata.position.y
        z = posedata.position.z
        self.DronePosition = np.array([x,y,z])
        # print(self.DronePosition)
        pass

    # def planebased(self, data):
    #     pipeAxisX = data.a.x
    #     pipeAxisY = data.a.y
    #     pipeAxisZ = data.a.z
    #     pipeX = data.P1.x
    #     pipeY = data.P1.y
    #     pipeZ = data.P1.z
    #     zangle = atan2(pipeAxisY, pipeAxisX)
    #     r = R.from_euler('z', zangle)
    #     quat = r.as_quat()
    #     # if self.DronePosition:
    #     self.goal.pose.position.x = pipeX #+ self.DronePosition[0]
    #     self.goal.pose.position.y = pipeY #+self.DronePosition[1]
    #     self.goal.pose.position.z = pipeZ - self.offsetZ #+ self.DronePosition[2]
    #     self.goal.pose.orientation.x = quat[0]
    #     self.goal.pose.orientation.y = quat[1]
    #     self.goal.pose.orientation.z = quat[2]
    #     self.goal.pose.orientation.w = quat[3]
    #     if not self.messageSent:
    #         self.messageSent = True
    #         print("Sent")
    #         print(quat)
    #         print(self.goal.pose.position.x, self.goal.pose.position.y, self.goal.pose.position.z)     
    #         for i in range(10):
    #             self.pub.publish(self.goal)
    #             self.rate.sleep()


    def callback(self, data):
        pipeAxisX = data.a.x
        pipeAxisY = data.a.y
        pipeAxisZ = data.a.z
        pipeX = data.P0.x
        pipeY = data.P0.y
        pipeZ = data.P0.z
        zangle = atan2(pipeAxisY, pipeAxisX)
        r = R.from_euler('z', zangle)
        quat = r.as_quat()
        # if self.DronePosition:
        self.goal.pose.position.x = pipeX + self.DronePosition[0]
        self.goal.pose.position.y = pipeY + self.DronePosition[1]
        self.goal.pose.position.z = pipeZ  + self.DronePosition[2] #- self.offsetZ
        self.goal.pose.orientation.x = quat[0]
        self.goal.pose.orientation.y = quat[1]
        self.goal.pose.orientation.z = quat[2]
        self.goal.pose.orientation.w = quat[3]
        if not self.messageSent:
            self.messageSent = True
            print("Sent")
            print(quat)
            print(self.goal.pose.position.x, self.goal.pose.position.y, self.goal.pose.position.z)     
            for i in range(10):
                self.pub.publish(self.goal)
                self.rate.sleep()

if __name__ == '__main__':
    perch = Perch()
