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

void GLWidget::paintGL()
{
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_TRIANGLES);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex3f(-0.5f, - 0.5f, 0.0f);
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex3f(0.5f, -0.5f, 0.0f);
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex3f(0.0f, 0.5f, 0.0f);
    glEnd();
}

void GLWidget::resizeGL(int w, int h)
{
    glViewport(0, 0, w, h);
}
