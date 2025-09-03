cmake_minimum_required(VERSION 3.8)
project(tmc_wrs_gz)

find_package(ament_cmake REQUIRED)

find_package(tmc_wrs_gz_launch REQUIRED)
find_package(tmc_wrs_gz_worlds REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
