#pragma once

#include <QtWidgets>
#include "infoLabel.h"


class CustomLabel : public QLabel
{
    // TODOS Deal with masking by using black white of icon
    Q_OBJECT

public:
    explicit CustomLabel(QWidget *parent = 0);
    void setInfoLabel(InfoLabel* info);
protected:
    bool event(QEvent* event);
signals:
    void signalLabelHover();
    void signalLabelPress();
    void signalLabelRelease();
    void signalLabelLeave();
public slots:
    void slotLabelHover();
    void slotLabelPress();
    void slotLabelRelease();
    void slotLabelLeave();
private:
    InfoLabel* infoText;
    QString resourcePath;
    QPixmap icon;
};
