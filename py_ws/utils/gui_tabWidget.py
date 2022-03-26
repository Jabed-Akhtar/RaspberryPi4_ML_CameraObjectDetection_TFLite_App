"""
 ******************************************************************************
 * @file: gui_tabWidget.py
 * @author: Jabed-Akhtar
 * @date: 09.03.2022
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
                             QSlider, QLCDNumber)
from PyQt5.QtGui import QActionEvent, QFont
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot, QThread, QObject
from PyQt5 import uic


AW = 1925  # Application window width 594
AH = 1000  # Application window height 371

msgInCou = 0


class WidgetTab(QWidget):
    """
    A class used to represent an Animal
    ...
    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.confTabs()
        self.confCAN()

        self.thread = {}

        self.CANMon_Worker()

    def confTabs(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """
        self.layout = QGridLayout(self)

        # self.canMon = self.createGUI_CANMonitor()

        self.layout.addWidget(self.createGUI_CANMonitor(), 0, 0, 0, 1)
        self.layout.addWidget(self.createGUI_CANSend(), 0, 1)
        self.layout.addWidget(self.createGUI_CANInfo(), 1, 1)
        self.layout.addWidget(self.createGUI_CANInfoConsole(), 2, 1)

        #self.canMon.writeToConsole()

        self.setLayout(self.layout)

    def confCAN(self):
        #self.canReceive = CANReceive()
        #self.canReceive.start()
        pass

    def createGUI_CANMonitor(self):
        """
        :Description:
            ---
        :return: grpBox (QGroupBox)
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox('CAN-Msg-Monitor')
        # configuring the QGroupBox
        grpBox.setMinimumWidth(500)
        grpBox.setStyleSheet('background-color: Tan;')
        #grpBox.setStyleSheet("QGroupBox { border: 2px solid lime;}")

        self.consMsgMonitor = QTextEdit()
        self.consMsgMonitor.setReadOnly(True)
        #self.consMsgMonitor.setText('---> Programm ready!')

        # configuring the QTextEdit
        self.consMsgMonitor.setStyleSheet('border: 2px solid black;'
                                          'background-color: DarkGray;')
        #self.consMsgMonitor.setContentsMargins(10, 10, 10, 10)

        vbox = QVBoxLayout()
        vbox.addWidget(self.consMsgMonitor)
        # vbox.addStretch(1)
        grpBox.setLayout(vbox)

        return grpBox

    def createGUI_CANSend(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox('CAN-Msg-Send')
        # configuring Group-Layout
        grpBox.setMinimumHeight(300)
        # grpBox.setMinimumWidth(500)
        # grpBox.setMaximumWidth(900)
        grpBox.setStyleSheet('background-color: Goldenrod;')

        # definning layout (inside the QGroupBox)
        self.gLayout = QGridLayout()

        # defnning components ***************
        self.varID = QLabel('ID (in Hex):')
        self.varIDInput = QLineEdit()

        self.varTxRate = QLabel('Cycle-Time (in ms):')
        self.varTxRateInput = QLineEdit()

        self.varData = QLabel('Data:')
        self.b1 = QRadioButton("in Hex")
        self.b2 = QRadioButton("in Int")
        self.varDataInput = QLineEdit()

        self.sendButton = QPushButton('Send')

        # configuring the components added in the group
        self.varID.setMinimumHeight(30)
        self.varID.setStyleSheet('border: 1px solid maroon;'
                                 'background-color: saddlebrown;'
                                 'font: bold 14px;')
        self.varIDInput.setMaximumSize(100, 30)
        self.varIDInput.setStyleSheet('border: 1px solid maroon;'
                                 'background-color: Gainsboro;'
                                 'font: bold 14px;')
        self.varTxRate.setMinimumHeight(30)
        self.varTxRate.setStyleSheet('border: 1px solid maroon;'
                                 'background-color: saddlebrown;'
                                 'font: bold 14px;')
        self.varTxRateInput.setMaximumSize(100, 30)
        self.varTxRateInput.setStyleSheet('border: 1px solid maroon;'
                                      'background-color: Gainsboro;'
                                      'font: bold 14px;')
        self.varData.setMinimumHeight(30)
        self.varData.setStyleSheet('border: 1px solid maroon;'
                                 'background-color: saddlebrown;'
                                 'font: bold 14px;')
        self.varDataInput.setMaximumSize(500, 30)
        self.varDataInput.setStyleSheet('border: 1px solid maroon;'
                                          'background-color: Gainsboro;'
                                          'font: bold 14px;')
        self.sendButton.setStyleSheet('background-color: Chocolate;')

        # Adding components to the group
        self.gLayout.addWidget(self.varID, 0, 0)
        self.gLayout.addWidget(self.varIDInput, 0, 1)
        self.gLayout.addWidget(self.varTxRate, 1, 0)
        self.gLayout.addWidget(self.varTxRateInput, 1, 1)
        self.gLayout.addWidget(self.varData, 2, 0)
        self.gLayout.addWidget(self.b1, 2, 1, 1, 1)
        self.gLayout.addWidget(self.b2, 2, 1, 2, 3)
        self.gLayout.addWidget(self.varDataInput, 3, 1)
        self.gLayout.addWidget(self.sendButton, 5, 0)

        # Adding responses
        self.sendButton.clicked.connect(self.on_CANSendButton_clicked)
        #self.sld.valueChanged.connect(self.on_Slider_change)
        # self.sendButton.clicked.connect(self.writeToConsole)

        grpBox.setLayout(self.gLayout)

        return grpBox

    def createGUI_CANInfo(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox('CAN-Msg-Info')
        # configuring Group-Layout
        # grpBox.setMinimumWidth(400)
        grpBox.setMinimumHeight(300)
        # grpBox.setMaximumWidth(900)
        grpBox.setStyleSheet('background-color: Tan;')

        self.consMsgInfo = QTextEdit()
        self.consMsgInfo.setReadOnly(True)
        self.consMsgInfo.setText('---> Programm ready from CAN-Info!')

        # configuring the QTextEdit
        self.consMsgInfo.setStyleSheet('border: 1px solid black;'
                                        'background-color: LightGray;')

        vbox = QVBoxLayout()
        vbox.addWidget(self.consMsgInfo)
        # vbox.addStretch(1)
        grpBox.setLayout(vbox)

        return grpBox

    def createGUI_CANInfoConsole(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # creating a object of QGroupBox
        grpBox = QGroupBox('CAN-Msg-Info-Console')
        # configuring Group-Layout
        # grpBox.setMinimumWidth(400)
        grpBox.setMinimumHeight(300)
        # grpBox.setMaximumWidth(900)
        grpBox.setStyleSheet('background-color: Tan;')

        self.consMsgInfoConsole = QTextEdit()
        self.consMsgInfoConsole.setReadOnly(True)
        self.consMsgInfoConsole.setText('---> Programm ready CAN-Cons!')

        # configuring the QTextEdit
        self.consMsgInfoConsole.setStyleSheet('border: 1px solid black;'
                                                'background-color: LightGray;')

        vbox = QVBoxLayout()
        vbox.addWidget(self.consMsgInfoConsole)
        # vbox.addStretch(1)
        grpBox.setLayout(vbox)

        return grpBox

    @pyqtSlot()
    def on_CANSendButton_clicked(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # print(self.varIDInput.text())
        # msg_id = self.varIDInput.text()
        # data=[0x11, 0x12]
        # data = self.varDataInput.text()

        # msg = can.Message(arbitration_id=112, is_extended_id=False, data=[0x11, 0x12])

        # Printing info to consolde
        self.consMsgInfoConsole.append('----->>> Message sent!')

        self.CANSend_Worker()

        # cansend = CANSend()
        # cansend.canSend()

        # canUt.CAN_Send(msg_id, data)

    def CANMon_Worker(self):
        self.thread[1] = CANReceive_th(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.CANMon_writeToGUI)
        pass

    def CANMon_Worker_Stop(self):
        self.thread[1].stop()

    def CANSend_Worker(self):
        self.thread[2] = CANSend_th(parent=None, index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.CANSend_writeToGUI)

    def CANSend_Worker_Stop(self):
        self.thread[2].stop()

    def CANMon_writeToGUI(self, counter):

        cnt = counter
        print(cnt)
        strin = 'Counter (CAN-Monitor): ' + str(cnt)
        self.consMsgMonitor.append(strin)

    def CANSend_writeToGUI(self, counter):
        cnt = counter
        print(cnt)
        strin = 'Counter (CAN-Send): ' + str(cnt)
        self.consMsgMonitor.append(strin)


class CANReceive_th(QThread):
    any_signal = pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(CANReceive_th, self).__init__(parent)
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


class CANSend_th(QThread):
    any_signal = pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(CANSend_th, self).__init__(parent)
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