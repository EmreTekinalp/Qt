#include "glWidget.h"

GLWidget::GLWidget(QWidget* parent):
    QGLWidget(parent)
{
}

void GLWidget::initializeGL()
{
    GLdouble color[3] = {0.15, 0.15, 0.2};
    glClearColor(color[0], color[1], color[2], 1);
}

void GLWidget::resizeGL(int w, int h)
{
    glViewport(0, 0, w, h);
}

void GLWidget::paintGL()
{
    glClear(GL_COLOR_BUFFER_BIT);
    drawTriangle();
}

void GLWidget::drawTriangle()
{
    glBegin(GL_TRIANGLES);

    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex3f(-0.5f + xPress, -0.5f + yPress, 0.0f);

    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex3f(0.5f + xPress, -0.5f + yPress, 0.0f);

    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex3f(0.0f + xPress, 0.5f + yPress, 0.0f);
    glEnd();

    MGlobal::displayInfo("pressedButton: " + pressedButton +
                         " width: " + MString() + this->width() +
                         " height: " + MString() + this->height() +
                         " rmvX: " + MString() + xPress +
                         " rmvY: " + MString() + yPress);
}


void GLWidget::mousePressEvent(QMouseEvent * event)
{
    if (event->buttons() == Qt::RightButton)
        pressedButton = "Right Button Pressed";
    if (event->button() == Qt::LeftButton)
        pressedButton = "Left Button Pressed";
}

void GLWidget::mouseReleaseEvent(QMouseEvent* event)
{
}

void GLWidget::mouseMoveEvent(QMouseEvent* event)
{
    xPress = remapValue(event->x() * 1.0, 0.0, this->width() * 1.0, -1.0, 1.0);
    yPress = remapValue(event->y() * 1.0, 0.0, this->height() * 1.0, -1.0, 1.0) * -1.0;
    updateGL();
}

float GLWidget::remapValue(float value, float from1, float to1, float from2, float to2)
{
    return (value - from1) / (to1 - from1) * (to2 - from2) + from2;
}