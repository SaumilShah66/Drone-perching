cmake_minimum_required(VERSION 2.8.3)
project(cylinder_detection)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages

find_package(cmake_modules REQUIRED)
find_package(Boost REQUIRED system filesystem date_time thread)
find_package(Eigen3 REQUIRED)
find_package(VISP REQUIRED)
find_package(OpenCV REQUIRED )

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  cylinder_msgs
  geometry_msgs
  image_transport
  nodelet
  roscpp
  sensor_msgs
)

catkin_package( 
	INCLUDE_DIRS include/cylinder_detection
	CATKIN_DEPENDS 
		cylinder_msgs 
		geometry_msgs 
		cv_bridge
		roscpp 
		sensor_msgs
		nodelet
		image_transport
	DEPENDS
		EIGEN3
		Boost
		VISP
)

include_directories(
  include/cylinder_detection
  ${catkin_INCLUDE_DIRS}
  ${VISP_INCLUDE_DIRS}
)

include_directories(SYSTEM ${Boost_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIRS})
include_directories(${OpenCV_INCLUDE_DIRS})

add_library(cylinder_detection src/cylinder_detection.cpp src/imgproc.cpp)

# add_executable(cylinder_detection thread system signals)

target_link_libraries(cylinder_detection
   ${catkin_LIBRARIES}
   ${EIGEN3_LIBRARIES}
   ${Boost_LIBRARIES}
   ${OpenCV_LIBRARIES}
   ${VISP_LIBRARIES}
 )

#add_dependencies(cylinder_detection cylinder_msgs_generate_messages_cpp)
