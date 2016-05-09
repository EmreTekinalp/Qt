cmake_minimum_required(VERSION 2.6)
project(HelloMayaQt)

set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/module)
set(MAYA_QT_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Middleware/QtMaya/include)

add_subdirectory(src)
