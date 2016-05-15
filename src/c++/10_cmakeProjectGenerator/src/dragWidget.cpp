#include "dragWidget.h"

DragWidget::DragWidget(QWidget* parent):
    QWidget(parent)
{
    setMouseTracking(true);
    this->setStyleSheet("QWidget{background-color: #500050;}"
                        "QWidget:hover{border-top-width: 5px; border-top-color: #006464; border-top-style: solid;}");
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
