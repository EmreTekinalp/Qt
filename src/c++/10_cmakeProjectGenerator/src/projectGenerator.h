#pragma once

#include <QtWidgets>
#include <iostream>
using std::cout;
using std::endl;
using std::rand;
using std::sprintf;

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
    Ui::MainWindow *ui;
public slots:
    void on_generateButton_clicked();
    void on_importButton_clicked();
private:
    // private methods
    int* projectPath();
    void setupProject(QString projectName);
    QString appendPath(QString path1, QString path2);
    void createFile(QString filePath);
    void setupStyleSheet(QPushButton* button);

    // private variables
    bool numCheck;
    QPoint dragPosition;
    QString resourcePath;
    QStringList folders;
    QString currentPath;
    QDir path;
};
