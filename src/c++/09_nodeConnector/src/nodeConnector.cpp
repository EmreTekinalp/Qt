#include <ctime>
#include <iostream>
using std::cout;
using std::endl;
using std::rand;

#include "nodeConnector.h"
#include "ui_nodeConnector.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    scene = new QGraphicsScene(this);
    ui->graphicsView->setScene(scene);
    // turn on antialiasing
    ui->graphicsView->setRenderHint(QPainter::Antialiasing);
    // set backgroundcolor
    scene->setBackgroundBrush(QColor(75, 10, 155, 127));
    // set GraphicsScene limitation to avoid scrollbars popping out
    scene->setSceneRect(0, 0, 100, 100);
    ui->graphicsView->show();
    clickCount = 0;

    for (int i = 0; i < 9; i++)
    {
        ui->nodeComboBox->addItem(QString::number(i) + " node");
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_addButton_clicked()
{
    // to be able to see cout results we have to allocate a console
    AllocConsole();
    freopen("CONOUT$", "w", stdout);

    rectangle = new CustomItem(ui->nodeComboBox->currentText(), QColor(Qt::lightGray));
    scene->addItem(rectangle);
}

void MainWindow::on_removeButton_clicked()
{
    foreach (QGraphicsItem* item, scene->selectedItems())
    {
        cout << item->isSelected() << " " << endl;
    }
}
