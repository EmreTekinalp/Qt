#include <QtWidgets\qapplication.h>
#include "labelButton.h"

int main(int argc, char* argv[])
{
    QApplication a(argc, argv);

    MainWindow h;
    h.show();
    return a.exec();
}