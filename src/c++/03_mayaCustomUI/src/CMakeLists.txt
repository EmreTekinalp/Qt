set(SOURCE_FILES
	"helixCmd.cpp"
	"helixCmd.h"
	"mayaMainWindow.cpp"
	"mayaMainWindow.h")

set(MAYA_QT_LIBS
	QtCore4.lib
	QtGui4.lib
	QtOpenGL4.lib
	qtmain.lib)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
	
find_package(Maya REQUIRED)
find_package(Qt4 4.8.6 REQUIRED)

include_directories(${MAYA_INCLUDE} ${MAYA_QT_INCLUDE_DIR})
link_directories(${MAYA_LIBRARY})
add_definitions(${Qt4_DEFINITIONS})

QT4_WRAP_CPP(MOCS_HDRS ${SOURCE_FILES})

add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES} ${MOCS_HDRS})
target_link_libraries(${PROJECT_NAME} ${MAYA_LIBS} ${MAYA_QT_LIBS})

MAYA_PLUGIN(${PROJECT_NAME})