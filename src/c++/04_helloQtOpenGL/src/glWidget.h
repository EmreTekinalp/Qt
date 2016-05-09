#pragma once

#include <QtOpenGL\qgl.h>

class GLWidget : public QGLWidget
{
    Q_OBJECT
public:
    explicit GLWidget(QWidget* parent = 0);
    void initializeGL();
    void paintGL();
    void resizeGL(int w, int h);
};