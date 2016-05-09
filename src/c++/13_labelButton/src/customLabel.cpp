#include "customLabel.h"


CustomLabel::CustomLabel(QWidget *parent) :
    QLabel(parent)
{
    resourcePath = QDir::currentPath().split("/build").join("") + "/resources/";
    icon.load(resourcePath + "close_button_black30x30.png");

    this->setMouseTracking(true);
    this->connect(this, SIGNAL(signalLabelHover()), this, SLOT(slotLabelHover()));
    this->connect(this, SIGNAL(signalLabelPress()), this, SLOT(slotLabelPress()));
    this->connect(this, SIGNAL(signalLabelRelease()), this, SLOT(slotLabelRelease()));
    this->connect(this, SIGNAL(signalLabelLeave()), this, SLOT(slotLabelLeave()));
}

void CustomLabel::setInfoLabel(InfoLabel* info)
{
    infoText = info;
}


bool CustomLabel::event(QEvent *event)
{
    switch (event->type())
    {
    case QEvent::MouseMove:
        emit signalLabelHover();
        return true;
        break;
    case QEvent::MouseButtonPress:
        emit signalLabelPress();
        return true;
        break;
    case QEvent::MouseButtonRelease:
        emit signalLabelRelease();
        return true;
        break;
    case QEvent::Leave:
        emit signalLabelLeave();
        return true;
        break;
    }
    QWidget::event(event);
    return true;
}


void CustomLabel::slotLabelHover()
{
    icon.load(resourcePath + "close_button_gray30x30.png");
    this->setPixmap(icon);
    infoText->setText("Hover");
    update();
}


void CustomLabel::slotLabelPress()
{
    icon.load(resourcePath + "close_button_red30x30.png");
    this->setPixmap(icon);
    infoText->setText("Press");
    update();
}


void CustomLabel::slotLabelRelease()
{
    icon.load(resourcePath + "close_button_red30x30.png");
    this->setPixmap(icon);
    infoText->setText("Release");
    update();
}


void CustomLabel::slotLabelLeave()
{
    icon.load(resourcePath + "close_button_black30x30.png");
    this->setPixmap(icon);
    infoText->setText("Leave");
    update();
}