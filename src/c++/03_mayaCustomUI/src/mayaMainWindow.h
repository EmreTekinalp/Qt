#pragma once

#include <QtGui\qmainwindow.h>
#include <QtCore\QCoreApplication.h>
#include <iostream>
using std::cout;
using std::endl;

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

    void getMayaWindow();
private:
    Ui::MainWindow *ui;
};
