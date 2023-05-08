# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(855, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 100))
        self.top_frame.setMaximumSize(QSize(16777215, 100))
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.paths_widget = QWidget(self.top_frame)
        self.paths_widget.setObjectName(u"paths_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paths_widget.sizePolicy().hasHeightForWidth())
        self.paths_widget.setSizePolicy(sizePolicy)
        self.paths_widget.setMinimumSize(QSize(0, 100))
        self.gridLayout_2 = QGridLayout(self.paths_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_paths = QLabel(self.paths_widget)
        self.label_paths.setObjectName(u"label_paths")

        self.gridLayout_2.addWidget(self.label_paths, 0, 0, 1, 1)

        self.list_paths = QListWidget(self.paths_widget)
        self.list_paths.setObjectName(u"list_paths")

        self.gridLayout_2.addWidget(self.list_paths, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_path_add = QPushButton(self.paths_widget)
        self.button_path_add.setObjectName(u"button_path_add")

        self.verticalLayout_2.addWidget(self.button_path_add)

        self.button_path_remove = QPushButton(self.paths_widget)
        self.button_path_remove.setObjectName(u"button_path_remove")

        self.verticalLayout_2.addWidget(self.button_path_remove)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.paths_widget)

        self.extensions_widget = QWidget(self.top_frame)
        self.extensions_widget.setObjectName(u"extensions_widget")
        sizePolicy.setHeightForWidth(self.extensions_widget.sizePolicy().hasHeightForWidth())
        self.extensions_widget.setSizePolicy(sizePolicy)
        self.extensions_widget.setMinimumSize(QSize(0, 100))
        self.extensions_widget.setMaximumSize(QSize(200, 200))
        self.gridLayout_3 = QGridLayout(self.extensions_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_extensions = QLabel(self.extensions_widget)
        self.label_extensions.setObjectName(u"label_extensions")

        self.gridLayout_3.addWidget(self.label_extensions, 0, 0, 1, 1)

        self.list_extensions = QListWidget(self.extensions_widget)
        self.list_extensions.setObjectName(u"list_extensions")

        self.gridLayout_3.addWidget(self.list_extensions, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button_ext_add = QPushButton(self.extensions_widget)
        self.button_ext_add.setObjectName(u"button_ext_add")

        self.verticalLayout_3.addWidget(self.button_ext_add)

        self.button_ext_remove = QPushButton(self.extensions_widget)
        self.button_ext_remove.setObjectName(u"button_ext_remove")

        self.verticalLayout_3.addWidget(self.button_ext_remove)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.extensions_widget)


        self.verticalLayout.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bottom_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_2 = QWidget(self.bottom_frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.tree_duplicates = QTreeWidget(self.widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Filename");
        self.tree_duplicates.setHeaderItem(__qtreewidgetitem)
        self.tree_duplicates.setObjectName(u"tree_duplicates")
        self.tree_duplicates.setSelectionMode(QAbstractItemView.NoSelection)
        self.tree_duplicates.setRootIsDecorated(True)
        self.tree_duplicates.setHeaderHidden(False)
        self.tree_duplicates.setColumnCount(2)

        self.verticalLayout_5.addWidget(self.tree_duplicates)

        self.progressbar_hashes = QProgressBar(self.widget)
        self.progressbar_hashes.setObjectName(u"progressbar_hashes")
        self.progressbar_hashes.setValue(0)

        self.verticalLayout_5.addWidget(self.progressbar_hashes)


        self.horizontalLayout_2.addWidget(self.widget)

        self.widget_duplicates = QWidget(self.widget_2)
        self.widget_duplicates.setObjectName(u"widget_duplicates")
        self.widget_duplicates.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget_duplicates)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.button_select_same = QPushButton(self.widget_duplicates)
        self.button_select_same.setObjectName(u"button_select_same")

        self.verticalLayout_6.addWidget(self.button_select_same)

        self.button_remove_selected = QPushButton(self.widget_duplicates)
        self.button_remove_selected.setObjectName(u"button_remove_selected")

        self.verticalLayout_6.addWidget(self.button_remove_selected)

        self.verticalSpacer = QSpacerItem(20, 256, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.button_find_duplicates = QPushButton(self.widget_duplicates)
        self.button_find_duplicates.setObjectName(u"button_find_duplicates")

        self.verticalLayout_6.addWidget(self.button_find_duplicates)

        self.label = QLabel(self.widget_duplicates)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.edit_possible_duplicates = QLineEdit(self.widget_duplicates)
        self.edit_possible_duplicates.setObjectName(u"edit_possible_duplicates")
        self.edit_possible_duplicates.setFrame(False)
        self.edit_possible_duplicates.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.edit_possible_duplicates)

        self.label_2 = QLabel(self.widget_duplicates)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.edit_num_duplicates = QLineEdit(self.widget_duplicates)
        self.edit_num_duplicates.setObjectName(u"edit_num_duplicates")
        self.edit_num_duplicates.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.edit_num_duplicates)

        self.label_3 = QLabel(self.widget_duplicates)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.edit_size_duplicates = QLineEdit(self.widget_duplicates)
        self.edit_size_duplicates.setObjectName(u"edit_size_duplicates")
        self.edit_size_duplicates.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.edit_size_duplicates)


        self.horizontalLayout_2.addWidget(self.widget_duplicates)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_paths.setText(QCoreApplication.translate("MainWindow", u"Paths", None))
        self.button_path_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_path_remove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_extensions.setText(QCoreApplication.translate("MainWindow", u"Extensions", None))
        self.button_ext_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_ext_remove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Duplicates", None))
        ___qtreewidgetitem = self.tree_duplicates.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Size", None));
        self.button_select_same.setText(QCoreApplication.translate("MainWindow", u"Select same directory", None))
        self.button_remove_selected.setText(QCoreApplication.translate("MainWindow", u"Remove selected", None))
        self.button_find_duplicates.setText(QCoreApplication.translate("MainWindow", u"Find duplicates", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Possible duplicates", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Duplicates:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Size of Duplicates:", None))
    # retranslateUi

