#ifndef helixQtCmd_h
#define helixQtCmd_h
// Copyright 2015 Autodesk, Inc. All rights reserved.
// 
// Use of this software is subject to the terms of the Autodesk
// license agreement provided at the time of installation or download,
// or which otherwise accompanies this software in either electronic
// or hard copy form.
//  Must ensure that at least one Qt header is included before anything
//  else.
#include <QtCore\qpointer.h>
#include <QtCore\qcoreapplication.h>
#include <QtGui\qpushbutton.h>
#include <QtGui\qmainwindow.h>
#include <maya/MPxCommand.h>
#include <maya/MQtUtil.h>
#include <vector>
#include <iostream>

using std::cout;
using std::endl;

#include "ui_MainWindow.h"


class HelixButton : public QMainWindow, private Ui::MainWindow
{
    Q_OBJECT
public:
    HelixButton(QWidget* parent = MQtUtil::mainWindow());
private slots:
    void    createHelix();
    void    buttonOne();
    void    buttonTwo();
    void    buttonThree();
private:
    float   fOffset;
};
class HelixQtCmd : public MPxCommand
{
public:
    static void     cleanup();
    static void*    creator() { return new HelixQtCmd(); }
    MStatus         doIt(const MArgList& args);
    static QPointer<HelixButton>    button;
    static const MString            commandName;
};
#endif
