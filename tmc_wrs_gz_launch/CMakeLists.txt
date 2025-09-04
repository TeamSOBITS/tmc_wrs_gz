cmake_minimum_required(VERSION 3.8)
project(tmc_wrs_gz_launch)

# find dependencies
find_package(ament_cmake REQUIRED)

find_package(xacro REQUIRED)
find_package(urdf REQUIRED)
find_package(ros_gz_sim REQUIRED)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
