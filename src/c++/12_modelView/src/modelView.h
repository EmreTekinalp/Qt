#pragma once

#include <QtWidgets>

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

private:
    Ui::MainWindow *ui;
    QStringListModel *model;
    QStringList list;
private slots:
    void on_addButton_clicked();
};