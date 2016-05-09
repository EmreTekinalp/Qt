cmake_minimum_required(VERSION 2.6)
project(HelloQtOpenGL)

set(GLEW_LIBRARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Middleware/glew/include)
set(GLEW_LIBRARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Middleware/glew/lib)
set(GLUT_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Middleware/freeglut/include)
set(GLUT_LIBRARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Middleware/freeglut/lib/x64)
set(GLM_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/Middleware/glm)

add_subdirectory(src)
