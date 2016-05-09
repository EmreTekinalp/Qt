#include "customItem.h"


CustomItem::CustomItem(QString nodeName, const QColor &color)
{
    this->_nodeName = nodeName;
    this->_color = color;
    setFlag(QGraphicsItem::ItemIsMovable);
    setFlag(QGraphicsItem::ItemIsSelectable);
}


QRectF CustomItem::boundingRect() const
{
    return QRectF(0, 0, 100, 100);
}

void CustomItem::paint(QPainter * painter, const QStyleOptionGraphicsItem * option, QWidget * widget)
{
    QRectF rec = boundingRect();

    QColor fillColor = (option->state & QStyle::State_Selected) ? this->_color.dark(150) : this->_color;
    if (option->state & QStyle::State_MouseOver)
        fillColor = fillColor.light(125);

    painter->fillRect(rec, fillColor);
    painter->setBrush(fillColor);
    painter->drawRect(rec);
    painter->drawText(10, 15, this->_nodeName);
}


QString CustomItem::getNodeName()
{
    return this->_nodeName;
}


void CustomItem::mousePressEvent(QGraphicsSceneMouseEvent * event)
{
    update();
    QGraphicsItem::mousePressEvent(event);
}


void CustomItem::mouseReleaseEvent(QGraphicsSceneMouseEvent * event)
{
    update();
    QGraphicsItem::mouseReleaseEvent(event);
}
