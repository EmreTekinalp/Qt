#include <ctime>
#include <iostream>
using std::cout;
using std::endl;
using std::rand;

#include "graphicsViewItem.h"
#include "ui_graphicsViewItem.h"

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
    scene->setSceneRect(-200, 200, 400, 250);
    ui->graphicsView->show();
    clickCount = 0;
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

    cout << "Created rectangles: " << clickCount << endl;
    clickCount += 1;

    rectangle = new CustomItem();
    scene->addItem(rectangle);
}
