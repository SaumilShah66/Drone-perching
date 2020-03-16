cmake_minimum_required(VERSION 2.8.3)
project(state_control_cylinder)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(cmake_modules REQUIRED)
#find_package(Boost REQUIRED system filesystem date_time thread)
find_package(Eigen3 REQUIRED)
#find_package(controllers_manager REQUIRED)

find_package(catkin REQUIRED COMPONENTS
  cylinder_msgs
  geometry_msgs
  nav_msgs
  roscpp
  std_srvs
  quadrotor_msgs
  velocity_tracker
  line_tracker
  null_tracker
)

catkin_package(
  INCLUDE_DIRS include/state_control_cylinder
  CATKIN_DEPENDS 
   cylinder_msgs 
   geometry_msgs 
   nav_msgs
   roscpp
   std_srvs
   controllers_manager
   velocity_tracker
   line_tracker
   null_tracker
  DEPENDS 
   EIGEN3
   #Boost
)

include_directories(
  include/state_control_cylinder
  ${catkin_INCLUDE_DIRS}
)
include_directories(SYSTEM ${EIGEN3_INCLUDE_DIRS})


add_executable(state_control src/state_control.cpp src/trajectory.cpp)

add_executable(manual_servo src/manual_servo.cpp)


target_link_libraries(state_control
   ${catkin_LIBRARIES}
   ${EIGEN3_LIBRARIES}
 )

add_dependencies(state_control cylinder_msgs_generate_messages_cpp)