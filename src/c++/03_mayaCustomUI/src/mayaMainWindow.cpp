#include "mayaMainWindow.h"
#include "ui_MainWindow.h"


void MainWindow::getMayaWindow()
{
    QCoreApplication*  app = qApp;
    if (app) {
        cout << "Application name is '" << app->applicationName().toStdString() << "'" << endl;
    }
    else
    {
        cout << "No maya app detected: " << app << endl;
    }
}


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
