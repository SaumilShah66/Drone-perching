	cmake_minimum_required(VERSION 2.8.3)
project(process_image_features)
add_compile_options(-std=c++11)

find_package(cmake_modules REQUIRED)
#find_package(Boost REQUIRED system filesystem date_time thread)
find_package(Eigen3 REQUIRED)
	find_package(LAPACK REQUIRED)

find_package(catkin REQUIRED
  cylinder_msgs
  geometry_msgs
  roscpp
)

catkin_package(
  INCLUDE_DIRS include/process_image_features
  CATKIN_DEPENDS 
   cylinder_msgs 
   geometry_msgs 
   roscpp

  DEPENDS 
   EIGEN3
   Boost
   LAPACK
)


include_directories(
  include/process_image_features
  ${catkin_INCLUDE_DIRS}
)

include_directories(SYSTEM ${EIGEN3_INCLUDE_DIRS})
include_directories(SYSTEM ${LAPACK_INCLUDE_DIRS})

add_executable(process_image_features src/process_image_features.cpp src/filter.cpp)

target_link_libraries(process_image_features
   ${catkin_LIBRARIES}
   ${EIGEN3_LIBRARIES}
   ${LAPACK_LIBRARIES}
 #  ${Boost_LIBRARIES}
 )

#add_dependencies(process_image_features cylinder_msgs_generate_messages_cpp)
