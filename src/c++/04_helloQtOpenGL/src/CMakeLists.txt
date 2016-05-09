set(SOURCE_FILES
	"main.cpp"
	"helloQtOpenGL.cpp"
	"glWidget.cpp")
set(HEADER_FILES
	"helloQtOpenGL.h"
	"glWidget.h")
set(UI_FILES
	"MainWindow.ui")
	
set(GL_LIBS
	glew32.lib
	glew32s.lib
	freeglut.lib
	opengl32.lib)
	
set(CMAKE_INCLUDE_CURRENT_DIR ON)
	
# find Qt5
find_package(Qt5Widgets REQUIRED)

# get lib path and specify required libs
set(QT_LIBRARY_DIRS ${_qt5Widgets_install_prefix}/lib)
set(QT_LIBS qtmaind.lib Qt5Cored Qt5Guid Qt5Widgetsd Qt5OpenGLd)

include_directories(${Qt5Widgets_INCLUDE_DIRS} ${GLEW_INCLUDE_DIR} ${GLUT_INCLUDE_DIR} ${GLM_INCLUDE_DIR})
link_directories(${QT_LIBRARY_DIRS} ${GLEW_LIBRARY_DIR} ${GLUT_LIBRARY_DIR})
add_definitions(${Qt5Widgets_DEFINITIONS})

qt5_wrap_cpp(MOCS_HDRS ${HEADER_FILES})
qt5_wrap_ui(UI_HDRS ${UI_FILES})

add_executable(${PROJECT_NAME} WIN32 ${SOURCE_FILES} ${HEADER_FILES} ${MOCS_HDRS} ${UI_HDRS})
target_link_libraries(${PROJECT_NAME} ${QT_LIBS} ${GL_LIBS})
