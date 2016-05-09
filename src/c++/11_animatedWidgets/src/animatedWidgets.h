#pragma once

#include <QtWidgets>
#include <QtCore/qpropertyanimation.h>
#include <QtGui\qscreen.h>

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
public slots:
    void on_createButton_clicked();
    void on_editButton_clicked();
    void on_closeButton_clicked();

    void on_buttonA_pressed();
    void on_buttonA_released();

    void on_buttonB_pressed();
    void on_buttonB_released();

    void on_buttonC_pressed();
    void on_buttonC_released();
private:
    Ui::MainWindow *ui;
    QRect mainScreenSize;

    QString main_bg_color = "DimGray";
    QString drag_widget_color = "#483A58";
    QString active_color = "#56203D";
    QString pressed_color = "#56638A";
    QString buttons_color = "#56203D";
};