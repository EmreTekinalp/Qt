#include "glWidget.h"


CustomItem::CustomItem(int x, int y, QString nodeName, const QColor &color)
{
    this->_x = x;
    this->_y = y;
    this->_nodeName = nodeName;
    this->_color = color;
    setFlag(QGraphicsItem::ItemIsMovable);
    setFlag(QGraphicsItem::ItemIsSelectable);
}


QRectF CustomItem::boundingRect() const
{
    return QRectF(_x, _y, 40, 40);
}

void CustomItem::paint(QPainter * painter, const QStyleOptionGraphicsItem * option, QWidget * widget)
{
    QRectF rec = boundingRect();

    QColor fillColor = (option->state & QStyle::State_Selected) ? this->_color.dark(150) : this->_color;

    if (QStyle::State_MouseOver)
        // to be able to see cout results we have to allocate a console
        AllocConsole();
        freopen("CONOUT$", "w", stdout);
        cout << option->state << endl;

    if (option->state & QStyle::State_MouseOver)
        fillColor = fillColor.light(125);

    painter->fillRect(rec, fillColor);
    painter->setBrush(fillColor);
    painter->drawRect(rec);
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
