/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.5.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCalendarWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QWidget *widget;
    QTabWidget *tabWidget;
    QWidget *tab_4;
    QCalendarWidget *calendarWidget;
    QWidget *tab;
    QTextEdit *textEdit;
    QTextEdit *textEdit_2;
    QWidget *tab_2;
    QTextEdit *textEdit_3;
    QTextEdit *textEdit_4;
    QWidget *tab_3;
    QTextEdit *textEdit_5;
    QTextEdit *textEdit_6;
    QMenuBar *menubar;
    QMenu *menuOOP_Lab_9;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(808, 610);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        widget = new QWidget(centralwidget);
        widget->setObjectName("widget");
        widget->setGeometry(QRect(-1, -1, 811, 561));
        tabWidget = new QTabWidget(widget);
        tabWidget->setObjectName("tabWidget");
        tabWidget->setGeometry(QRect(-1, -1, 811, 561));
        tab_4 = new QWidget();
        tab_4->setObjectName("tab_4");
        calendarWidget = new QCalendarWidget(tab_4);
        calendarWidget->setObjectName("calendarWidget");
        calendarWidget->setGeometry(QRect(9, 6, 791, 331));
        calendarWidget->setGridVisible(false);
        calendarWidget->setVerticalHeaderFormat(QCalendarWidget::NoVerticalHeader);
        tabWidget->addTab(tab_4, QString());
        tab = new QWidget();
        tab->setObjectName("tab");
        textEdit = new QTextEdit(tab);
        textEdit->setObjectName("textEdit");
        textEdit->setGeometry(QRect(60, 60, 671, 451));
        textEdit_2 = new QTextEdit(tab);
        textEdit_2->setObjectName("textEdit_2");
        textEdit_2->setGeometry(QRect(60, 20, 671, 41));
        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName("tab_2");
        textEdit_3 = new QTextEdit(tab_2);
        textEdit_3->setObjectName("textEdit_3");
        textEdit_3->setGeometry(QRect(60, 20, 681, 41));
        textEdit_4 = new QTextEdit(tab_2);
        textEdit_4->setObjectName("textEdit_4");
        textEdit_4->setGeometry(QRect(60, 60, 681, 451));
        tabWidget->addTab(tab_2, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName("tab_3");
        textEdit_5 = new QTextEdit(tab_3);
        textEdit_5->setObjectName("textEdit_5");
        textEdit_5->setGeometry(QRect(60, 20, 681, 41));
        textEdit_6 = new QTextEdit(tab_3);
        textEdit_6->setObjectName("textEdit_6");
        textEdit_6->setGeometry(QRect(60, 60, 681, 451));
        tabWidget->addTab(tab_3, QString());
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 808, 21));
        menuOOP_Lab_9 = new QMenu(menubar);
        menuOOP_Lab_9->setObjectName("menuOOP_Lab_9");
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuOOP_Lab_9->menuAction());

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_4), QCoreApplication::translate("MainWindow", "Calendar App", nullptr));
        textEdit->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\232\320\273\320\260\321\201 QTabWidget \320\275\320\260\320\264\320\260\321\224 \320\262\321\226\320\264\320\266\320\265\321\202-\320\272\320\276\320\275\321\202\320\265\320\271\320\275\320\265\321\200 \320\264\320\273\321\217 \320\262\321\226\320\264\320\276\320\261\321\200\320\260\320\266\320\265\320\275\320\275\321\217 \320\264\320\265\320\272\321\226\320\273\321\214\320\272\320\276\321\205 \320"
                        "\262\320\272\320\273\320\260\320\264\320\276\320\272. \320\232\320\276\320\266\320\275\320\260 \320\262\320\272\320\273\320\260\320\264\320\272\320\260 \320\274\321\226\321\201\321\202\320\270\321\202\321\214 \320\276\320\272\321\200\320\265\320\274\320\270\320\271 \320\262\321\226\320\264\320\266\320\265\321\202, \321\226 \320\272\320\276\321\200\320\270\321\201\321\202\321\203\320\262\320\260\321\207 \320\274\320\276\320\266\320\265 \320\277\320\265\321\200\320\265\320\274\320\270\320\272\320\260\321\202\320\270\321\201\321\217 \320\274\321\226\320\266 \320\262\320\272\320\273\320\260\320\264\320\272\320\260\320\274\320\270 \320\275\320\260\321\202\320\270\321\201\320\272\320\260\320\275\320\275\321\217\320\274 \320\275\320\260 \320\275\320\270\321\205.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px;\">\320\236\321\201\321\214 \320\264\320\265\321\217\320\272\321\226 \320\272\320\273\321\216\321\207\320\276\320\262\321\226 \320\276\321\201\320\276\320\261\320\273\320\270\320\262\320\276\321\201\321\202\321\226 \320\272\320\273\320\260\321\201\321\203 QTabWidget:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\237\321\200\320\276\321\201\321\202\320\270\320\271 \321\203 \320\262\320\270\320\272\320\276\321\200\320\270\321\201\321\202\320\260\320\275\320\275\321\226 \321\202\320\260 \320\275\320\260\320\273\320\260\321\210\321\202\321\203\320\262\320\260\320\275\320\275\321\226</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\237\321\226\320\264\321\202"
                        "\321\200\320\270\320\274\321\203\321\224 \320\277\320\265\321\200\320\265\320\262\320\277\320\276\321\200\321\217\320\264\320\272\321\203\320\262\320\260\320\275\320\275\321\217 \320\262\320\272\320\273\320\260\320\264\320\276\320\272 \320\267\320\260 \320\264\320\276\320\277\320\276\320\274\320\276\320\263\320\276\321\216 \320\277\320\265\321\200\320\265\321\202\321\217\320\263\321\203\320\262\320\260\320\275\320\275\321\217</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\234\320\276\320\266\320\265 \320\261\321\203\321\202\320\270 \321\201\321\202\320\270\320\273\321\226\320\267\320\276\320\262\320\260\320\275\320\270\320\271 \320\267\320\260 \320\264\320\276\320\277\320\276\320\274\320\276\320\263\320\276\321\216 \321\202\320\260\320\261\320\273\320\270\321\206\321\214 \321\201\321\202\320\270\320\273\321\226\320\262</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\">- \320\237\321\226\320\264\321\202\321\200\320\270\320\274\321\203\321\224 \321\217\320\272 \320\263\320\276\321\200\320\270\320\267\320\276\320\275\321\202\320\260\320\273\321\214\320\275\321\203, \321\202\320\260\320\272 \321\226 \320\262\320\265\321\200\321\202\320\270\320\272\320\260\320\273\321\214\320\275\321\203 \320\276\321\200\321\226\321\224\320\275\321\202\320\260\321\206\321\226\321\216 \320\262\320\272\320\273\320\260\320\264\320\276\320\272</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\234\320\276\320\266\320\275\320\260 \320\264\320\270\320\275\320\260\320\274\321\226\321\207\320\275\320\276 \320\267\320\274\321\226\320\275\321\216\320\262\320\260\321\202\320\270 \321\200\320\276\320\267\320\274\321\226\321\200 \320\262\321\226\320\264\320\277\320\276\320\262\321\226\320\264\320\275\320\276 \320\264\320\276 \320\262\320\274\321\226\321\201\321\202\321\203</p>\n"
"<p style=\"-qt-parag"
                        "raph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\251\320\276\320\261 \320\262\320\270\320\272\320\276\321\200\320\270\321\201\321\202\320\276\320\262\321\203\320\262\320\260\321\202\320\270 QTabWidget \321\203 \320\262\320\260\321\210\320\276\320\274\321\203 \320\264\320\276\320\264\320\260\321\202\320\272\321\203 Qt, \320\262\320\270 \320\274\320\276\320\266\320\265\321\202\320\265 \321\201\321\202\320\262\320\276\321\200\320\270\321\202\320\270 \320\275\320\276\320\262\320\270\320\271 \320\265\320\272\320\267\320\265\320\274\320\277\320\273\321\217\321\200 \320\272\320\273\320\260\321\201\321\203 \321\226 \320\264\320\276\320\264\320\260\321\202\320\270 \320\264\320\276 \320\275\321\214\320\276\320\263\320\276 \320\262\320\272\320\273\320\260\320\264\320\272\320\270 \320\267\320\260 \320\264\320"
                        "\276\320\277\320\276\320\274\320\276\320\263\320\276\321\216 \320\274\320\265\321\202\320\276\320\264\321\203 `addTab()`. \320\222\320\270 \321\202\320\260\320\272\320\276\320\266 \320\274\320\276\320\266\320\265\321\202\320\265 \320\275\320\260\320\273\320\260\321\210\321\202\321\203\320\262\320\260\321\202\320\270 \320\267\320\276\320\262\320\275\321\226\321\210\320\275\321\226\320\271 \320\262\320\270\320\263\320\273\321\217\320\264 \321\202\320\260 \320\277\320\276\320\262\320\265\320\264\321\226\320\275\320\272\321\203 \320\262\320\272\320\273\320\260\320\264\320\276\320\272 \320\267\320\260 \320\264\320\276\320\277\320\276\320\274\320\276\320\263\320\276\321\216 \321\200\321\226\320\267\320\275\320\270\321\205 \320\262\320\273\320\260\321\201\321\202\320\270\320\262\320\276\321\201\321\202\320\265\320\271 \321\202\320\260 \320\274\320\265\321\202\320\276\320\264\321\226\320\262, \320\275\320\260\320\264\320\260\320\275\320\270\321\205 \320\272\320\273\320\260\321\201\320\276\320\274.</p></body></html>", nullptr));
        textEdit_2->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">QTabWidget</span></p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("MainWindow", "\320\236\320\277\320\270\321\201 QTabWidget", nullptr));
        textEdit_3->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">QWidget</span></p></body></html>", nullptr));
        textEdit_4->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\232\320\273\320\260\321\201 QWidget \321\224 \320\261\320\260\320\267\320\276\320\262\320\270\320\274 \320\272\320\273\320\260\321\201\320\276\320\274 \320\264\320\273\321\217 \320\262\321\201\321\226\321\205 \320\265\320\273\320\265\320\274\320\265\320\275\321\202\321\226\320\262 \321\226\320\275\321\202\320\265\321\200\321\204\320\265\320\271\321\201\321\203 \320\272\320\276\321\200\320\270\321"
                        "\201\321\202\321\203\320\262\320\260\321\207\320\260 \321\203 Qt. \320\222\321\226\320\275 \320\275\320\260\320\264\320\260\321\224 \321\207\320\270\321\201\321\202\320\265 \320\277\320\276\320\273\320\276\321\202\320\275\320\276, \321\217\320\272\320\265 \320\262\320\270 \320\274\320\276\320\266\320\265\321\202\320\265 \320\262\320\270\320\272\320\276\321\200\320\270\321\201\321\202\320\276\320\262\321\203\320\262\320\260\321\202\320\270 \320\264\320\273\321\217 \321\201\321\202\320\262\320\276\321\200\320\265\320\275\320\275\321\217 \320\272\320\276\321\200\320\270\321\201\321\202\321\203\320\262\320\260\321\206\321\214\320\272\320\270\321\205 \320\262\321\226\320\264\320\266\320\265\321\202\321\226\320\262, \321\200\320\276\320\267\320\261\320\270\320\262\320\260\321\216\321\207\320\270 \320\271\320\276\320\263\320\276 \320\275\320\260 \320\277\321\226\320\264\320\272\320\273\320\260\321\201\320\270 \321\202\320\260 \320\264\320\276\320\264\320\260\321\216\321\207\320\270 \320\262\320\273\320\260\321\201\320"
                        "\275\321\203 \321\204\321\203\320\275\320\272\321\206\321\226\320\276\320\275\320\260\320\273\321\214\320\275\321\226\321\201\321\202\321\214.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\236\321\201\321\214 \320\264\320\265\321\217\320\272\321\226 \320\272\320\273\321\216\321\207\320\276\320\262\321\226 \320\276\321\201\320\276\320\261\320\273\320\270\320\262\320\276\321\201\321\202\321\226 \320\272\320\273\320\260\321\201\321\203 QWidget:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\235\320\260\320\264\320\260\321\224"
                        " \320\275\320\265\320\267\320\260\320\273\320\265\320\266\320\275\321\203 \320\262\321\226\320\264 \320\277\320\273\320\260\321\202\321\204\320\276\321\200\320\274\320\270 \320\261\320\260\320\267\321\203 \320\264\320\273\321\217 \320\262\321\201\321\226\321\205 \320\262\321\226\320\264\320\266\320\265\321\202\321\226\320\262</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\234\320\276\320\266\320\265 \320\261\321\203\321\202\320\270 \320\277\321\226\320\264\320\272\320\273\320\260\321\201\320\270\321\204\321\226\320\272\320\276\320\262\320\260\320\275\320\270\320\271 \320\264\320\273\321\217 \321\201\321\202\320\262\320\276\321\200\320\265\320\275\320\275\321\217 \320\262\320\273\320\260\321\201\320\275\320\270\321\205 \320\262\321\226\320\264\320\266\320\265\321\202\321\226\320\262</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\237\321"
                        "\226\320\264\321\202\321\200\320\270\320\274\321\203\321\224 \320\274\320\260\320\273\321\216\320\262\320\260\320\275\320\275\321\217, \320\276\320\261\321\200\320\276\320\261\320\272\321\203 \320\277\320\276\320\264\321\226\320\271 \321\202\320\260 \320\272\320\265\321\200\321\203\320\262\320\260\320\275\320\275\321\217 \320\272\320\276\320\274\320\277\320\276\320\275\321\203\320\262\320\260\320\275\320\275\321\217\320\274</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\234\320\276\320\266\320\275\320\260 \320\262\320\270\320\272\320\276\321\200\320\270\321\201\321\202\320\276\320\262\321\203\320\262\320\260\321\202\320\270 \321\217\320\272 \320\272\320\276\320\275\321\202\320\265\320\271\320\275\320\265\321\200 \320\264\320\273\321\217 \321\226\320\275\321\210\320\270\321\205 \320\262\321\226\320\264\320\266\320\265\321\202\321\226\320\262</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px;\">- \320\234\320\276\320\266\320\275\320\260 \321\201\321\202\320\270\320\273\321\226\320\267\321\203\320\262\320\260\321\202\320\270 \320\267\320\260 \320\264\320\276\320\277\320\276\320\274\320\276\320\263\320\276\321\216 \321\202\320\260\320\261\320\273\320\270\321\206\321\214 \321\201\321\202\320\270\320\273\321\226\320\262</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\251\320\276\320\261 \321\201\321\202\320\262\320\276\321\200\320\270\321\202\320\270 \320\262\320\273\320\260\321\201\320\275\320\270\320\271 \320\262\321\226\320\264\320\266\320\265\321\202 \320\267\320\260 \320\264\320\276\320\277\320\276\320\274\320\276\320\263\320\276\321\216 QWidget, \320\262\320\270 \320\274\320\276\320\266\320\265\321\202\320\265 "
                        "\321\201\321\202\320\262\320\276\321\200\320\270\321\202\320\270 \320\271\320\276\320\263\320\276 \320\277\321\226\320\264\320\272\320\273\320\260\321\201 \321\226 \320\277\320\265\321\200\320\265\320\262\320\270\320\267\320\275\320\260\321\207\320\270\321\202\320\270 \320\271\320\276\320\263\320\276 \320\262\321\226\321\200\321\202\321\203\320\260\320\273\321\214\320\275\321\226 \320\274\320\265\321\202\320\276\320\264\320\270, \321\211\320\276\320\261 \320\264\320\276\320\264\320\260\321\202\320\270 \320\262\320\273\320\260\321\201\320\275\321\203 \321\204\321\203\320\275\320\272\321\206\321\226\320\276\320\275\320\260\320\273\321\214\320\275\321\226\321\201\321\202\321\214. \320\222\320\270 \321\202\320\260\320\272\320\276\320\266 \320\274\320\276\320\266\320\265\321\202\320\265 \320\262\320\270\320\272\320\276\321\200\320\270\321\201\321\202\320\276\320\262\321\203\320\262\320\260\321\202\320\270 \321\200\321\226\320\267\320\275\321\226 \320\262\320\273\320\260\321\201\321\202\320\270\320\262\320\276\321\201"
                        "\321\202\321\226 \321\202\320\260 \320\274\320\265\321\202\320\276\320\264\320\270, \320\275\320\260\320\264\320\260\320\275\321\226 \320\272\320\273\320\260\321\201\320\276\320\274, \320\264\320\273\321\217 \320\275\320\260\320\273\320\260\321\210\321\202\321\203\320\262\320\260\320\275\320\275\321\217 \320\267\320\276\320\262\320\275\321\226\321\210\320\275\321\214\320\276\320\263\320\276 \320\262\320\270\320\263\320\273\321\217\320\264\321\203 \321\202\320\260 \320\277\320\276\320\262\320\265\320\264\321\226\320\275\320\272\320\270 \320\262\320\260\321\210\320\276\320\263\320\276 \320\262\321\226\320\264\320\266\320\265\321\202\321\203.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QCoreApplication::translate("MainWindow", "\320\236\320\277\320\270\321\201 QWidget", nullptr));
        textEdit_5->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">QString</span></p></body></html>", nullptr));
        textEdit_6->setHtml(QCoreApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\232\320\273\320\260\321\201 QString \320\275\320\260\320\264\320\260\321\224 \321\200\321\217\320\264\320\276\320\272 \321\201\320\270\320\274\320\262\320\276\320\273\321\226\320\262 Unicode \321\203 Qt. \320\222\321\226\320\275 \320\277\320\276\320\264\321\226\320\261\320\275\320\270\320\271 \320\264\320\276 \321\201\321\202\320\260\320\275\320\264\320\260\321\200\321\202\320\275\320\276\320\263"
                        "\320\276 \320\272\320\273\320\260\321\201\321\203 C++ <span style=\" font-style:italic;\">std::string</span>, \320\260\320\273\320\265 \320\275\320\260\320\264\320\260\321\224 \320\264\320\276\320\264\320\260\321\202\320\272\320\276\320\262\321\226 \320\274\320\276\320\266\320\273\320\270\320\262\320\276\321\201\321\202\321\226 \320\264\320\273\321\217 \320\276\320\261\321\200\320\276\320\261\320\272\320\270 \321\200\321\217\320\264\320\272\321\226\320\262 Unicode.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\236\321\201\321\214 \320\264\320\265\321\217\320\272\321\226 \320\272\320\273\321\216\321\207\320\276\320\262\321\226 \320\276\321\201\320\276\320\261\320\273\320\270\320\262\320\276\321\201\321\202\321\226 \320\272\320\273\320\260\321\201\321\203 QString:</p>"
                        "\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\235\320\260\320\264\320\260\321\224 \320\275\320\265\320\267\320\260\320\273\320\265\320\266\320\275\320\270\320\271 \320\262\321\226\320\264 \320\277\320\273\320\260\321\202\321\204\320\276\321\200\320\274\320\270 \321\201\320\277\320\276\321\201\321\226\320\261 \320\276\320\261\321\200\320\276\320\261\320\272\320\270 \321\200\321\217\320\264\320\272\321\226\320\262 Unicode</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\237\321\226\320\264\321\202\321\200\320\270\320\274\321\203\321\224 \321\201\320\265\320\274\320\260\320\275\321\202\320\270\320\272\321\203 \321\201\320\277\321\226\320\273\321\214\320\275\320\276\320\263\320\276 \320"
                        "\264\320\276\321\201\321\202\321\203\320\277\321\203 \321\202\320\260 \320\263\320\273\320\270\320\261\320\276\320\272\320\276\320\263\320\276 \320\272\320\276\320\277\321\226\321\216\320\262\320\260\320\275\320\275\321\217</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\235\320\260\320\264\320\260\321\224 \321\200\321\226\320\267\320\275\320\276\320\274\320\260\320\275\321\226\321\202\320\275\321\226 \320\274\320\265\321\202\320\276\320\264\320\270 \320\264\320\273\321\217 \320\274\320\260\320\275\321\226\320\277\321\203\320\273\321\216\320\262\320\260\320\275\320\275\321\217 \321\202\320\260 \320\277\320\276\321\210\321\203\320\272\321\203 \321\200\321\217\320\264\320\272\321\226\320\262</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\234\320\276\320\266\320\265 \320\272\320\276\320\275\320\262\320\265\321\200\321\202\321\203\320\262\320"
                        "\260\321\202\320\270\321\201\321\217 \321\203 \321\202\320\260 \320\267 \321\200\321\226\320\267\320\275\320\270\321\205 \320\272\320\276\320\264\321\203\320\262\320\260\320\275\321\214</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- \320\237\321\226\320\264\321\202\321\200\320\270\320\274\321\203\321\224 \321\201\320\277\321\226\320\262\321\201\321\202\320\260\320\262\320\273\320\265\320\275\320\275\321\217 \321\200\320\265\320\263\321\203\320\273\321\217\321\200\320\275\320\270\321\205 \320\262\320\270\321\200\320\260\320\267\321\226\320\262</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\320\251\320\276\320\261 \320\262\320\270\320\272\320\276\321\200\320\270\321\201\321\202\320\276\320\262"
                        "\321\203\320\262\320\260\321\202\320\270 QString \321\203 \320\262\320\260\321\210\320\276\320\274\321\203 \320\264\320\276\320\264\320\260\321\202\320\272\321\203 Qt, \320\262\320\270 \320\274\320\276\320\266\320\265\321\202\320\265 \321\201\321\202\320\262\320\276\321\200\320\270\321\202\320\270 \320\275\320\276\320\262\320\270\320\271 \320\265\320\272\320\267\320\265\320\274\320\277\320\273\321\217\321\200 \320\272\320\273\320\260\321\201\321\203 \321\202\320\260 \321\226\320\275\321\226\321\206\321\226\320\260\320\273\321\226\320\267\321\203\320\262\320\260\321\202\320\270 \320\271\320\276\320\263\320\276 \321\200\321\217\320\264\320\272\320\276\320\262\320\270\320\274 \320\273\321\226\321\202\320\265\321\200\320\260\320\273\320\276\320\274 \320\260\320\261\320\276 \321\226\320\275\321\210\320\270\320\274 \320\276\320\261'\321\224\320\272\321\202\320\276\320\274 QString. \320\222\320\270 \321\202\320\260\320\272\320\276\320\266 \320\274\320\276\320\266\320\265\321\202\320\265 \320\262\320\270\320\272\320\276"
                        "\321\200\320\270\321\201\321\202\320\276\320\262\321\203\320\262\320\260\321\202\320\270 \321\200\321\226\320\267\320\275\321\226 \320\274\320\265\321\202\320\276\320\264\320\270, \320\275\320\260\320\264\320\260\320\275\321\226 \320\272\320\273\320\260\321\201\320\276\320\274, \320\264\320\273\321\217 \320\274\320\260\320\275\321\226\320\277\321\203\320\273\321\216\320\262\320\260\320\275\320\275\321\217 \321\202\320\260 \320\277\320\276\321\210\321\203\320\272\321\203 \321\200\321\217\320\264\320\272\320\260, \320\260\320\261\320\276 \320\277\320\265\321\200\320\265\321\202\320\262\320\276\321\200\320\265\320\275\320\275\321\217 \320\271\320\276\320\263\320\276 \320\264\320\276 \321\202\320\260 \320\267 \321\200\321\226\320\267\320\275\320\270\321\205 \320\272\320\276\320\264\321\203\320\262\320\260\320\275\321\214.</p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QCoreApplication::translate("MainWindow", "\320\236\320\277\320\270\321\201 QString", nullptr));
        menuOOP_Lab_9->setTitle(QCoreApplication::translate("MainWindow", "OOP Lab 9", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
