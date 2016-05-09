#include "customItem.h"


CustomItem::CustomItem()
{
    pressed = false;
    setFlag(QGraphicsItem::ItemIsMovable);
}


QRectF CustomItem::boundingRect() const
{
    return QRectF(0, 0, 100, 100);
}


void CustomItem::paint(QPainter * painter, const QStyleOptionGraphicsItem * option, QWidget * widget)
{
    QRectF rec = boundingRect();
    QBrush brush(Qt::red);

    if (pressed)
    {
        brush.setColor(Qt::green);
    }
    else
    {
        brush.setColor(Qt::red);
    }
    painter->fillRect(rec, brush);
    painter->drawEllipse(rec);
    painter->drawRect(rec);
}


void CustomItem::mousePressEvent(QGraphicsSceneMouseEvent * event)
{
    pressed = true;
    update();
    QGraphicsItem::mousePressEvent(event);
}


void CustomItem::mouseReleaseEvent(QGraphicsSceneMouseEvent * event)
{
    pressed = false;
    update();
    QGraphicsItem::mouseReleaseEvent(event);
}
