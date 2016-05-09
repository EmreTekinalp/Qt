#include "labelButton.h"
#include "customLabel.h"
#include "ui_labelButton.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // set the current path
    resourcePath = QDir::currentPath().split("/build").join("") + "/resources/";
    icon.load(resourcePath + "close_button_black30x30.png");
    ui->labelOne->setPixmap(icon);
    ui->labelOne->setInfoLabel(ui->infoOne);
    ui->labelTwo->setPixmap(icon);
    ui->labelTwo->setInfoLabel(ui->infoTwo);
    ui->labelThree->setPixmap(icon);
    ui->labelThree->setInfoLabel(ui->infoThree);
}


MainWindow::~MainWindow()
{
    delete ui;
}
