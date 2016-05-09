#include "projectGenerator.h"
#include "ui_projectGenerator.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    setAutoFillBackground(true);
    setWindowFlags(Qt::Widget | Qt::FramelessWindowHint);
    this->setStyleSheet("color:white; background-color:Dimgray;");

    resourcePath = QDir::currentPath().split("/build").join("") + "/resources/";
    ui->projectName_led->setStyleSheet("color:black; background-color:white;");
    ui->projectPath_led->setStyleSheet("color:black; background-color:white;");
    ui->optionButton->setStyleSheet("QPushButton{background-color:gray; min-width: 1em; padding: 6px; border: none;}"
                                    "QPushButton:hover{background-color:DarkGray; min-width: 1em; padding: 6px; border: none;}"
                                    "QPushButton:pressed{background-color:DimGray; min-width: 1em; padding: 6px; border: none;}");
    ui->closeButton->setStyleSheet("QPushButton{background-color:gray; min-width: 1em; padding: 6px; border: none;}"
                                   "QPushButton:hover{background-color:DarkGray; min-width: 1em; padding: 6px; border: none;}"
                                   "QPushButton:pressed{background-color:DimGray; min-width: 1em; padding: 6px; border: none;}");

    // pencil icon
    QAction *myPencilAction = ui->projectPath_led->addAction(QIcon(resourcePath + "pencil2.png"), QLineEdit::TrailingPosition);
    connect(myPencilAction, &QAction::triggered, this, &MainWindow::projectPath);

    // get DesktopScreen
    QDesktopWidget desktop;
    QRect rect = desktop.availableGeometry(desktop.primaryScreen());

    // set animation
    QPropertyAnimation *anim = new QPropertyAnimation(this, "geometry");
    anim->setDuration(500);
    anim->setStartValue(QRect(0, (rect.height() / 2) - (this->height() / 2), this->width(), this->height()));
    anim->setEndValue(QRect((rect.width() / 2) - (this->width() / 2),
                            (rect.height() / 2) - (this->height() / 2),
                            this->width(), this->height()));
    anim->setEasingCurve(QEasingCurve::OutQuad);
    anim->start();
}

MainWindow::~MainWindow()
{
    delete ui;
}

int* MainWindow::projectPath()
{
    QString folder = QFileDialog::getExistingDirectory(this, tr("Open Directory"), "/home",
        QFileDialog::ShowDirsOnly | QFileDialog::DontResolveSymlinks);
    ui->contentWidget->clear();
    QDir path(folder);
    path.setFilter(QDir::AllDirs | QDir::NoDotAndDotDot);
    QStringList folders = path.entryList();
    ui->contentWidget->addItems(folders);
    ui->projectPath_led->setText(folder);
    return 0;
}

void MainWindow::on_numberButton_clicked()
{
    if (numCheck)
    {
        ui->numberButton->setText("ABC");
        numCheck = false;
    }
    else
    {
        ui->numberButton->setText("123");
        numCheck = true;
    }
}

void MainWindow::on_generateButton_clicked()
{
    AllocConsole();
    freopen("CONOUT$", "w", stdout);
    cout << resourcePath.toStdString() << endl;
}