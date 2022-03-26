"""
 ******************************************************************************
 * @file: gui_tabWidget.py
 * @author: Jabed-Akhtar
 * @date: 26.03.2022
 *****************************************************************************
 * :Description:
 *
 *
 ******************************************************************************
"""


#from import_all import *
import sys, os, time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGroupBox, QTableWidget, QTableWidgetItem,
                             QRadioButton, QLineEdit, QTextEdit, QFrame, QCheckBox, QPushButton, QHeaderView,
                             QMenu, QMenuBar, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit,
                             QMessageBox, QAction, QMessageBox, QDesktopWidget, QTabWidget, QFormLayout, QInputDialog,
                             QSlider, QLCDNumber, QSizePolicy)
from PyQt5.QtGui import QActionEvent, QFont
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot, QThread, QObject
from PyQt5 import uic


AW = 1925  # Application window width 594
AH = 1000  # Application window height 371

msgInCou = 0


class WidgetTab(QWidget):
    """
    A class used to create the Widget
    ...
    Attributes
    ----------
    name : str
        the ---
    Methods
    -------
    says(sound=None)
        Prints the ---
    """

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # cofiguring all sub-widgets / groups
        self.confGroups()

        # thread object
        self.thread = {}

    def confGroups(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # Grid layout for adding groups to widget
        self.layout = QGridLayout(self)

        # Adding groups to widget
        self.layout.addWidget(self.createGUI_Control(), 0, 0, 1, 3)
        self.layout.addWidget(self.createGUI_InfoConsole(), 1, 0, 1, 3)
        self.layout.addWidget(self.createGUI_ImgRealTime(), 0, 3, 2, 7)

        # Setting the layout
        self.setLayout(self.layout)

    def createGUI_Control(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox()
        # configuring Group-Layout
        grpBox.setMinimumHeight(200)
        grpBox.setMinimumWidth(300)
        grpBox.setStyleSheet('background-color: Goldenrod;')

        # definning layout (inside the QGroupBox)
        self.gLayout = QGridLayout()

        # defnning components ***************
        self.sendButStart = QPushButton('Start')
        self.sendButStop = QPushButton('Stop')

        # configuring the components added in the group
        self.sendButStart.setStyleSheet('background-color: Chocolate;')
        self.sendButStop.setStyleSheet('background-color: Chocolate;')

        # Adding components to the group
        self.gLayout.addWidget(self.sendButStart, 0, 0)
        self.gLayout.addWidget(self.sendButStop, 0, 1)

        # Adding responses
        self.sendButStart.clicked.connect(self.on_sendButStart_clicked)
        self.sendButStop.clicked.connect(self.on_sendButStop_clicked)

        grpBox.setLayout(self.gLayout)

        return grpBox

    def createGUI_InfoConsole(self):

        # creating a object of QGroupBox
        grpBox = QGroupBox('Console-Info')
        # configuring the QGroupBox
        grpBox.setMinimumWidth(300)
        grpBox.setStyleSheet('background-color: Tan;')

        self.consMsg = QTextEdit()
        self.consMsg.setReadOnly(True)
        #self.consMsgMonitor.setText('---> Programm ready!')

        # configuring the QTextEdit
        self.consMsg.setStyleSheet('border: 2px solid black;'
                                          'background-color: DarkGray;')
        # self.consMsgMonitor.setContentsMargins(10, 10, 10, 10)

        vbox = QVBoxLayout()
        vbox.addWidget(self.consMsg)
        # vbox.addStretch(1)
        grpBox.setLayout(vbox)

        return grpBox

    def createGUI_ImgRealTime(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox('CAN-Msg-Info')
        # configuring Group-Layout
        grpBox.setMinimumHeight(300)
        grpBox.setStyleSheet('background-color: Tan;')
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        grpBox.setSizePolicy(sizePolicy)

        self.consImgOnline = QTextEdit()
        self.consImgOnline.setReadOnly(True)
        self.consImgOnline.setText('---> Hello from createGUI_ImgRealTime!')

        # configuring the QTextEdit
        self.consImgOnline.setStyleSheet('border: 1px solid black;'
                                        'background-color: LightGray;')

        vbox = QVBoxLayout()
        vbox.addWidget(self.consImgOnline)
        # vbox.addStretch(1)
        grpBox.setLayout(vbox)

        return grpBox

    @pyqtSlot()
    def on_sendButStart_clicked(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # Printing info to consolde
        self.consMsg.append('---> CAM activated!')

        self.CAM_Worker()

    @pyqtSlot()
    def on_sendButStop_clicked(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # Printing info to consolde
        self.consMsg.append('---> CAM deactivated!')

        self.CAM_Worker_Stop()

    def CAM_Worker(self):
        self.thread[1] = CAM_th(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.CANMon_writeToGUI)
        pass

    def CAM_Worker_Stop(self):
        self.thread[1].stop()
        pass

    def CANMon_writeToGUI(self, counter):

        cnt = counter
        print(cnt)
        strin = 'Counter (CAN-Monitor): ' + str(cnt)
        #self.consMsgMonitor.append(strin)

    def CANSend_writeToGUI(self, counter):
        cnt = counter
        print(cnt)
        strin = 'Counter (CAN-Send): ' + str(cnt)
        self.consMsgMonitor.append(strin)


class CAM_th(QThread):
    any_signal = pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(CAM_th, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        print('Starting thread...', self.index)
        cnt = 0
        while (True):
            time.sleep(1)
            cnt += 1
            if cnt == 99: cnt = 0
            time.sleep(0.01)
            self.any_signal.emit(cnt)

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()


# ****************************** END OF FILE ******************************