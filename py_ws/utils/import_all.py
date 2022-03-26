"""
 ******************************************************************************
 * @file: import_all.py
 * @author: gyanthp
 * @date: 26.12.2021
 *****************************************************************************
 * :Description:
 *
 *
 ******************************************************************************
"""

""" imports """
import sys, os, time, threading
import numpy

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGroupBox, QTableWidget, QTableWidgetItem,
                             QRadioButton, QLineEdit, QTextEdit, QFrame, QCheckBox, QPushButton, QHeaderView,
                             QMenu, QMenuBar, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit,
                             QMessageBox, QAction, QMessageBox, QDesktopWidget, QTabWidget, QFormLayout, QInputDialog)
from PyQt5.QtGui import QActionEvent, QFont
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot
