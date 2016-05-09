set(SOURCE_FILES
	"main.cpp"
	"graphicsViewItem.cpp"
	"customItem.cpp")
set(HEADER_FILES
	"graphicsViewItem.h"
	"customItem.h")
set(UI_FILES
	"graphicsViewItem.ui")
	
set(CMAKE_INCLUDE_CURRENT_DIR ON)
	
# find Qt5
find_package(Qt5Widgets REQUIRED)

# get lib path and specify required libs
set(QT_LIBRARY_DIRS ${_qt5Widgets_install_prefix}/lib)
set(QT_LIBS qtmaind.lib Qt5Cored Qt5Guid Qt5Widgetsd Qt5OpenGLd)

include_directories(${Qt5Widgets_INCLUDE_DIRS})
link_directories(${QT_LIBRARY_DIRS})
add_definitions(${Qt5Widgets_DEFINITIONS})

qt5_wrap_cpp(MOCS_HDRS ${HEADER_FILES})
qt5_wrap_ui(UI_HDRS ${UI_FILES})

add_executable(${PROJECT_NAME} WIN32 ${SOURCE_FILES} ${HEADER_FILES} ${MOCS_HDRS} ${UI_HDRS})
target_link_libraries(${PROJECT_NAME} ${QT_LIBS})
