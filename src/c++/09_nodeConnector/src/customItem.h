#pragma once

#include <QtWidgets>

class CustomItem : public QGraphicsItem
{
    QString _nodeName;
    QColor _color;
public:
    CustomItem(QString nodeName, const QColor &color);

    QRectF boundingRect() const;
    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget);

    QString getNodeName();
protected:
    void mousePressEvent(QGraphicsSceneMouseEvent *event);
    void mouseReleaseEvent(QGraphicsSceneMouseEvent *event);
};
