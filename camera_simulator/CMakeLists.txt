cmake_minimum_required(VERSION 2.8.3)
project(camera_simulator)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(cmake_modules REQUIRED)
find_package(Boost REQUIRED system filesystem date_time thread)
find_package(Eigen3 REQUIRED)

find_package(catkin REQUIRED
  geometry_msgs
  nav_msgs
  roscpp
  std_msgs
  cylinder_msgs
)

catkin_package( 
	INCLUDE_DIRS include/camera_simulator
	CATKIN_DEPENDS 
		cylinder_msgs 
		geometry_msgs 
		nav_msgs 
		roscpp 
		std_msgs
	DEPENDS
		EIGEN3
		Boost
)

include_directories(
  include/camera_simulator
  ${catkin_INCLUDE_DIRS}
)

include_directories(SYSTEM ${Boost_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIRS})
#include_directories(${catkin_INCLUDE_DIRS})

add_executable(camera_simulator src/camera_simulator.cpp)

target_link_libraries(camera_simulator
   ${catkin_LIBRARIES}
   ${EIGEN3_LIBRARIES}
   ${Boost_LIBRARIES}
 )

#add_dependencies(camera_simulator cylinder_msgs_generate_messages_cpp)
