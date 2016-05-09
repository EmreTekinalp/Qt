#pragma once

#include <QtOpenGL\qgl.h>
#include <QtGui\QMouseEvent>

class GLWidget : public QGLWidget
{
    Q_OBJECT
public:
    explicit GLWidget(QWidget* parent = 0);
    void initializeGL();
    void resizeGL(int w, int h);
    void paintGL();
    void drawTriangle();
};