#pragma once

#include <QtWidgets>
#include "projectGenerator.h"

class CustomItem : public QGraphicsItem
{
    QString _nodeName;
    QColor _color;
    int _x, _y;
public:
    CustomItem(int x, int y, QString nodeName, const QColor &color);

    QRectF boundingRect() const;
    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option, QWidget *widget);

    QString getNodeName();
protected:
    void mousePressEvent(QGraphicsSceneMouseEvent *event);
    void mouseReleaseEvent(QGraphicsSceneMouseEvent *event);
};
