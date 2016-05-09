set(SOURCE_FILES
	"main.cpp"
	"glWidget.cpp"	
	"dragWidget.cpp"
	"projectGenerator.cpp")
set(HEADER_FILES
	"glWidget.h"
	"dragWidget.h"
	"projectGenerator.h")
set(UI_FILES
	"projectGenerator.ui")

set(GL_LIBS
	opengl32.lib)	
	
set(GENERATOR_EXTENSION "")
if(MSVC)
	set(GENERATOR_EXTENSION msvc2015_64)
endif()
	
set(QT_LIBRARY_DIR $ENV{QT5_DIR}${GENERATOR_EXTENSION}/lib)
set(QT_LIBS qtmaind Qt5Cored Qt5Guid Qt5Widgetsd Qt5OpenGLd)

include_directories(${Qt5Widgets_INCLUDE_DIRS})
link_directories(${QT_LIBRARY_DIR})
add_definitions(${Qt5Widgets_DEFINITIONS})

qt5_wrap_cpp(MOCS_HDRS ${HEADER_FILES})
qt5_wrap_ui(UI_HDRS ${UI_FILES})

add_executable(${PROJECT_NAME} WIN32 ${SOURCE_FILES} ${HEADER_FILES} ${MOCS_HDRS} ${UI_HDRS})
target_link_libraries(${PROJECT_NAME} ${QT_LIBS} ${GL_LIBS})
