cmake_minimum_required(VERSION 2.8.3)
project(cylinder_msgs)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   CylinderPose.msg
   ImageFeatures.msg
   ParallelPlane.msg
 )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   geometry_msgs
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES cylinder_msgs
  CATKIN_DEPENDS message_runtime geometry_msgs
#  DEPENDS system_lib
)


