cmake_minimum_required(VERSION 3.5)
project(tmc_wrs_gazebo_launch)

set(ROS1 FALSE)
if(DEFINED ENV{ROS_DISTRO})
  if($ENV{ROS_DISTRO} STREQUAL "noetic")
    set(ROS1 TRUE)
  endif()
  if($ENV{ROS_DISTRO} STREQUAL "melodic")
    set(ROS1 TRUE)
  endif()
endif()

if(ROS1)
  find_package(catkin REQUIRED)
  catkin_package()
  install(
    DIRECTORY launch
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
    FILES_MATCHING
    PATTERN "*.launch"
  )
  install(DIRECTORY
    config
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  )
  if (CATKIN_ENABLE_TESTING)
    find_package(roslaunch REQUIRED)
    roslaunch_add_file_check(launch USE_TEST_DEPENDENCIES)
  endif()
else()
  find_package(ament_cmake REQUIRED)
  install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
  install(DIRECTORY config DESTINATION share/${PROJECT_NAME})
  ament_package()
endif()

