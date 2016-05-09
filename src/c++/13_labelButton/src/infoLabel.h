#pragma once

#include <QtWidgets>


class InfoLabel : public QLabel
{
    Q_OBJECT

public:
    explicit InfoLabel(QWidget *parent = 0);
    ~InfoLabel();
};