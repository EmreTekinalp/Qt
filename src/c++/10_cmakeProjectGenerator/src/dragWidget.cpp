#include "dragWidget.h"

DragWidget::DragWidget(QWidget* parent):
    QWidget(parent)
{
    setMouseTracking(true);
    this->setStyleSheet("QWidget{background-color: DarkMagenta;}"
                        "QWidget:hover{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #f6f7fa);}");
}

void DragWidget::mousePressEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton) {
        dragPosition = event->globalPos() - this->window()->frameGeometry().topLeft();
        event->accept();
    }
}

void DragWidget::mouseMoveEvent(QMouseEvent *event)
{
    if (event->buttons() & Qt::LeftButton) {
        this->window()->move(event->globalPos() - dragPosition);
        event->accept();
    }
}
