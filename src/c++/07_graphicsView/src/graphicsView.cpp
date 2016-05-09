#include <ctime>
#include <iostream>
using std::cout;
using std::endl;
using std::rand;


#include "graphicsView.h"
#include "ui_graphicsView.h"

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

    QBrush blueBrush(Qt::blue);
    QPen blackPen(Qt::black);
    rectangle = scene->addRect(0, 0, 100, 100, blackPen, blueBrush);
    rectangle->setFlag(QGraphicsItem::ItemIsMovable);
}
