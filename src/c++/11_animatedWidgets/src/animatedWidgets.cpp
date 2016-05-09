#include "animatedWidgets.h"
#include "ui_animatedWidgets.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->window()->setStyleSheet("background-color: " + main_bg_color + ";");
    ui->editButton->setStyleSheet("background-color: " + buttons_color + "; border: none;");
    ui->createButton->setStyleSheet("background-color: " + buttons_color + "; border: none;");
    ui->closeButton->setStyleSheet("background-color: " + buttons_color + "; border: none;");
    ui->buttonA->setStyleSheet("background-color: " + active_color + "; border: none;");
    ui->buttonB->setStyleSheet("background-color: " + active_color + "; border: none;");
    ui->buttonC->setStyleSheet("background-color: " + active_color + "; border: none;");
    ui->dragWidget->setStyleSheet("background-color: " + drag_widget_color + ";");

    QDesktopWidget widget;
    mainScreenSize = widget.availableGeometry(widget.primaryScreen());

    QPropertyAnimation *animation = new QPropertyAnimation(this->window(), "geometry");
    animation->setDuration(500);
    animation->setStartValue(QRect(0, (mainScreenSize.height() * 0.5) - (this->window()->height() * 0.5), this->window()->width(), this->window()->height()));
    animation->setEndValue(QRect((mainScreenSize.width() * 0.5) - (this->window()->width() * 0.5), (mainScreenSize.height() * 0.5) - (this->window()->height() * 0.5), this->window()->width(), this->window()->height()));

    animation->start();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_createButton_clicked()
{
    QPropertyAnimation *anim1 = new QPropertyAnimation(ui->editButton, "geometry");
    anim1->setDuration(500);
    anim1->setStartValue(QRect(ui->editButton->pos().x(), ui->editButton->pos().y(), ui->editButton->width(), ui->editButton->height()));
    anim1->setEndValue(QRect(ui->editButton->pos().x(), (this->window()->height() * 0.5), ui->editButton->width(), ui->editButton->height()));

    QPropertyAnimation *anim2 = new QPropertyAnimation(ui->closeButton, "geometry");
    anim2->setDuration(500);
    anim2->setStartValue(QRect(ui->closeButton->pos().x(), ui->closeButton->pos().y(), ui->closeButton->width(), ui->closeButton->height()));
    anim2->setEndValue(QRect(ui->closeButton->pos().x(), (this->window()->height() * 0.5), ui->closeButton->width(), ui->closeButton->height()));

    QParallelAnimationGroup *group = new QParallelAnimationGroup;
    group->addAnimation(anim1);
    group->addAnimation(anim2);

    group->start();
}


void MainWindow::on_editButton_clicked()
{
    if (ui->editButton->pos().y() == this->window()->height() * 0.5)
    {
        QPropertyAnimation *anim1 = new QPropertyAnimation(ui->editButton, "geometry");
        anim1->setDuration(500);
        anim1->setStartValue(QRect(ui->editButton->pos().x(), ui->editButton->pos().y(), ui->editButton->width(), ui->editButton->height()));
        anim1->setEndValue(QRect(ui->editButton->pos().x(), ui->createButton->pos().y(), ui->editButton->width(), ui->editButton->height()));
        anim1->start();
    }
}


void MainWindow::on_closeButton_clicked()
{
    if (ui->closeButton->pos().y() == this->window()->height() * 0.5)
    {
        QPropertyAnimation *anim2 = new QPropertyAnimation(ui->closeButton, "geometry");
        anim2->setDuration(500);
        anim2->setStartValue(QRect(ui->closeButton->pos().x(), ui->closeButton->pos().y(), ui->closeButton->width(), ui->closeButton->height()));
        anim2->setEndValue(QRect(ui->closeButton->pos().x(), ui->createButton->pos().y(), ui->closeButton->width(), ui->closeButton->height()));
        anim2->start();
    }
}


void MainWindow::on_buttonA_pressed()
{
    ui->buttonA->setStyleSheet("background-color: " + pressed_color + "; border: none;");
}

void MainWindow::on_buttonA_released()
{
    ui->buttonA->setStyleSheet("background-color: " + active_color + "; border: none;");
}


void MainWindow::on_buttonB_pressed()
{
    ui->buttonB->setStyleSheet("background-color: " + pressed_color + "; border: none;");
}

void MainWindow::on_buttonB_released()
{
    ui->buttonB->setStyleSheet("background-color: " + active_color + "; border: none;");
}


void MainWindow::on_buttonC_pressed()
{
    ui->buttonC->setStyleSheet("background-color: " + pressed_color + "; border: none;");
}

void MainWindow::on_buttonC_released()
{
    ui->buttonC->setStyleSheet("background-color: " + active_color + "; border: none;");
}