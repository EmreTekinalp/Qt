#pragma once

#include <QtWidgets>
#include "customItem.h"

namespace Ui
{
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
private slots:
    // The cool thing is because we have a button object called
    // addButton we only need to specify a private slot void function
    // with the key words: on_<BUTTONOBJNAME>_clicked() or
    // on_<BUTTONOBJNAME>_released() or on_<BUTTONOBJNAME>_pressed() etc
    // No need for slot signal editing in QtDesigner for custom slots.
    // If we would reconnect it in Designer or in code we would call it twice.
    void on_addButton_clicked();
private:
    Ui::MainWindow *ui;
    QGraphicsScene *scene;
    CustomItem *rectangle;
    int clickCount;
};