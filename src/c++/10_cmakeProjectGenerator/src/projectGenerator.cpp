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

    ui->importButton->setStyleSheet("QPushButton{background-color:Dimgray; min-width: 1em; padding: 6px; border: none;}"
                                    "QPushButton:hover{background-color:#007474; border-top-width: 5px; border-top-color: #006464; border-top-style: solid;}"
                                    "QPushButton:pressed{background-color:#006464;}");
    ui->optionButton->setStyleSheet("QPushButton{background-color:Dimgray; min-width: 1em; padding: 6px; border: none;}"
                                    "QPushButton:hover{background-color:#007474; border-top-width: 5px; border-top-color: #006464; border-top-style: solid;}"
                                    "QPushButton:pressed{background-color:#006464;}");
    ui->closeButton->setStyleSheet("QPushButton{background-color:Dimgray; min-width: 1em; padding: 6px; border: none;}"
                                   "QPushButton:hover{background-color:#007474; border-top-width: 5px; border-top-color: #006464; border-top-style: solid;}"
                                   "QPushButton:pressed{background-color:#006464;}");
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

    currentPath = "/home";
}

MainWindow::~MainWindow()
{
    delete ui;
}

int* MainWindow::projectPath()
{
    QString folder = QFileDialog::getExistingDirectory(this, tr("Open Directory"),
                                                       currentPath,
                                                       QFileDialog::ShowDirsOnly |
                                                       QFileDialog::DontResolveSymlinks);
    if (!folder.isEmpty())
    {
        ui->contentWidget->clear();
        currentPath = folder;
        path = QDir(folder);
        path.setFilter(QDir::AllDirs | QDir::NoDotAndDotDot);
        folders = path.entryList();
        ui->contentWidget->addItems(folders);
        ui->projectPath_led->setText(folder);
    }
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
    /*
    AllocConsole();
    freopen("CONOUT$", "w", stdout);
    */

    int len = folders.length();
    char s[4];

    if (numCheck)
    {
        if (ui->projectName_led->text().isEmpty())
        {
            return;
        }
        std::sprintf(s, "%02d_", len + 1);
        QString projectName = QString(s) + ui->projectName_led->text();
        setupProject(projectName);
    }
}

void MainWindow::setupProject(QString projectName)
{

    if (! QDir(projectName).exists())
    {
        path.mkdir(projectName);
        QString projectPath = appendPath(path.absolutePath(), projectName);
        QDir(projectPath).mkdir("build");
        QDir(projectPath).mkdir("src");
        QString sourcePath = appendPath(projectPath, "src");
        createFile(projectPath);
        createFile(sourcePath);
        ui->contentWidget->addItem(projectName);
        ui->projectName_led->clear();
    }
}

QString MainWindow::appendPath(QString path1, QString path2)
{
    return QDir::cleanPath(path1 + QDir::separator() + path2);
}

void MainWindow::createFile(QString filePath)
{
    QFile cmakeFile(filePath + QDir::separator() + "CMakeLists.txt");
    if (!cmakeFile.exists())
    {
        cmakeFile.open(QIODevice::ReadWrite);
    }
}