set(SOURCE_FILES
	"main.cpp"
	"test.cpp"
	"test.h"
	"ui_test.h")

set(CMAKE_INCLUDE_CURRENT_DIR ON)

find_package(Qt5Widgets)
set(QT_LIBS Qt5Cored.lib Qt5Guid.lib Qt5Widgetsd.lib Qt5OpenGLd.lib qtmaind.lib)

set(QT_LIBRARY_DIRS "C:/Qt/Qt5.6.0/5.6/msvc2015_64/lib")

include_directories(${Qt5Widgets_INCLUDE_DIRS})
link_directories(${QT_LIBRARY_DIRS})
add_definitions(${Qt5Widgets_DEFINITIONS})

QT5_WRAP_CPP(MOCS_HDRS test.h)

add_executable(${PROJECT_NAME} ${SOURCE_FILES};${MOCS_HDRS})
target_link_libraries(${PROJECT_NAME} ${QT_LIBS})