#include "modelView.h"
#include "ui_modelView.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    model = new QStringListModel(this);

    list << "cats" << "dogs" << "birds";
    model->setStringList(list);
    ui->listView->setModel(model);
    ui->comboBox->setModel(model);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_addButton_clicked()
{
    QString text = ui->itemLineEdit->text();
    if (!text.isEmpty())
    {
        list << ui->itemLineEdit->text();
        model->setStringList(list);
        ui->listView->setModel(model);
        ui->comboBox->setModel(model);
    }
    ui->itemLineEdit->clear();
}