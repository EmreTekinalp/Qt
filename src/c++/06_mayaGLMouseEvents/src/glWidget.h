#pragma once

#include <QtOpenGL\qgl.h>
#include <QtGui\QMouseEvent>
#include <maya\MGlobal.h>
#include <maya\MString.h>

class GLWidget : public QGLWidget
{
    Q_OBJECT
private:
    float xPress, yPress;
    MString pressedButton;
public:
    explicit GLWidget(QWidget* parent = 0);
    void initializeGL();
    void resizeGL(int w, int h);
    void paintGL();
    void drawTriangle();
    float remapValue(float value, float from1, float to1, float from2, float to2);

    void mousePressEvent(QMouseEvent * event);
    void mouseReleaseEvent(QMouseEvent * event);
    void mouseMoveEvent(QMouseEvent * event);
};