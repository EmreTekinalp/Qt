#pragma once

#include <QtWidgets>
#include "projectGenerator.h"

class DragWidget : public QWidget
{
    Q_OBJECT
public:
    explicit DragWidget(QWidget* parent = 0);
    void mousePressEvent(QMouseEvent *event) Q_DECL_OVERRIDE;
    void mouseMoveEvent(QMouseEvent *event) Q_DECL_OVERRIDE;
private:
    QPoint dragPosition;
};