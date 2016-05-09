cmake_minimum_required(VERSION 2.8.11)

project(LabelButton)

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# find Qt5
find_package(Qt5Widgets REQUIRED)

add_subdirectory(src)