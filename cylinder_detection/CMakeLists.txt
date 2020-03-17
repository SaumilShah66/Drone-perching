cmake_minimum_required(VERSION 2.8.3)
project(cylinder_detection)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
  sensor_msgs
  cv_bridge
  image_transport
  cylinder_msgs
  nodelet
  #trajectory_msgs
)

find_package( OpenCV REQUIRED )
find_package(Boost REQUIRED system filesystem date_time thread)

find_package(VISP REQUIRED)
IF(VISP_FOUND)
 INCLUDE(${VISP_USE_FILE})
 ENDIF(VISP_FOUND)

catkin_package(
   #CATKIN_DEPENDS message_runtime

   DEPENDS
		Boost
)

include_directories(
  include/cylinder_detection	
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

add_library(cylinder_detection src/cylinder_detection.cpp src/imgproc.cpp)


# add_executable(cvTest test/level2/test.cpp src/imageConvert.cpp)

target_link_libraries(cylinder_detection
   ${catkin_LIBRARIES}
   ${OpenCV_LIBRARIES}
 )

include_directories(cylinder_detection ${Boost_INCLUDE_DIR})
#add_dependencies(cylinder_detection cylinder_msgs_generate_messages_cpp)

