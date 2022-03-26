"""
 ******************************************************************************
 * @file: gui_menu_FileNSettings.py
 * @author: Jabed, gyanthp, Tek, Mukesh, Bibek
 * @date: 02.01.2021
 *****************************************************************************
 * :Description:
 *
 *
 ******************************************************************************
"""

# imports
#from utils import CANUtils as canUt
from utils.gui_tabWidget import *

UI_WinPOS_X = 100  # 1500 #use 0
UI_WinPOS_Y = 100  # use 0
AW = 1925  # Application window width 594
AH = 1000  # Application window height 371
OFFSET_X = 10
WINDOW_TITLE = "CAN Simulation"

var_ActivatedCANChannel = 1
var_CANBaudrate = 125


class GUI_MainWin(QMainWindow):
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

    def __init__(self):
        super().__init__()

        self.initUI()
        self.initOthers()

    def initUI(self):
        """
        :Description:
            here all UI are to be initialized
        :return: nothing
        """

        # creating vertical layout for all contents inside GUI
        vLayout = QVBoxLayout()
        self.setLayout(vLayout)

        # adding components to vertical layout (vLayout)
        # self.create_menu()
        # grid.addWidget(, 0, 0)
        #vLayout.addWidget(self.createGUI_menuBar())
        # vLayout.addWidget(self.createGUI_CANMonitor())
        self.createGUI_menuBar()

        # configuring GUI-Window
        # self.setGeometry(UI_WinPOS_X, UI_WinPOS_Y, AW, AH)  # 594x371mm is the total size of 7inch display
        self.setWindowTitle(WINDOW_TITLE)
        self.setStyleSheet('background-color: grey;')

        # adding Tab to GUI-Widget
        self.tab_widget = WidgetTab(self)
        self.setCentralWidget(self.tab_widget)
        #self.tab_widget.setGeometry(0, 20, AW, AH - 20)
        self.tab_widget.move(0, 20)
        self.tab_widget.setMinimumSize(500, 500)

        # showing the GUI
        self.showMaximized()  # showing the GUI will maximized size of display
        self.show()

    def initOthers(self):
        """
        :Description:
            here other initialisations, beside the GUIs, are done
        :return: nth
        """

        self.on_MenuSettCANChCAN0_clicked()
        self.on_MenuSettCANBdRate125_clicked()

        #self.guiWid = createGUI()

    def createGUI_menuBar(self):
        """
        :Description:
            here Menu-Bar GUI are to be initialized/created
        :return: nth
        """

        # creating menu var >>>>>
        menuBar = self.menuBar()
        # menuBar.setFixedSize(1000, 25)
        menuBar.setMinimumSize(1000, 25)
        menuBar.setStyleSheet("background-color: green")

        # creating menus >>>>>
        # File menu **********
        fileMenu = QMenu("&File", self)
        fileMenu.setStyleSheet("border-width: 1px;")
        # adding components to file menu
        fileMenu.addAction('open setting')
        fileMenu.addAction('save setting')
        self.varCANlog = QAction('save CAN-Log as text')
        fileMenu.addAction(self.varCANlog)
        self.varExit = QAction('Exit', fileMenu)
        fileMenu.addAction(self.varExit)
        # Setting menu **********
        settingMenu = QMenu("&Settings", self)
        # menu - Setting
        settingCANCh = settingMenu.addMenu('select CAN-Channels')
        # adding more Actions to Setting-Menu-CANChannels
        self.varCAN0 = QAction('can0', self, checkable=True)
        # var = settingCANCh.addAction('can0', self, checkable=True)
        settingCANCh.addAction(self.varCAN0)
        self.varCAN0.setChecked(True)
        self.varCAN1 = QAction('can1', self, checkable=True)
        settingCANCh.addAction(self.varCAN1)
        # settingCANCh.addAction('can1')
        self.varCANboth = QAction('both', self, checkable=True)
        settingCANCh.addAction(self.varCANboth)
        # settingCANCh.addAction('both')
        # menu - Baudrate
        bdRate = settingMenu.addMenu('set Baudrate')
        self.varbdRate125 = QAction('125kBd', self, checkable=True)
        bdRate.addAction(self.varbdRate125)
        self.varbdRate125.setChecked(True)
        # bdRate.addAction('125kBd')
        self.varbdRate250 = QAction('250kBd', self, checkable=True)
        bdRate.addAction(self.varbdRate250)
        self.varbdRate500 = QAction('500kBd', self, checkable=True)
        bdRate.addAction(self.varbdRate500)
        # bdRate.addAction('500kBd')
        # Help menu **********
        self.helpMenu = QMenu("&Help", self)
        self.menuHelpDoc = self.helpMenu.addAction('Doc')
        self.menuHelpAbt = self.helpMenu.addAction('About CANotronics')

        # can info menu
        canInfoMenu = QMenu("&Tab", self)
        self.canMon = QAction("&CAN-Monitor", self, checkable=True)
        self.canMon.setChecked(True)
        self.cansend = QAction("&CAN-Send", self, checkable=True)
        self.config = QAction("&CAN-Info", self, checkable=True)
        canInfoMenu.addAction(self.canMon)
        canInfoMenu.addAction(self.cansend)
        canInfoMenu.addAction(self.config)

        # get triggered as soon as menu_button is clicked
        # config.triggered.connect(lambda: self.canInfo_clicked())

        # adding components to menu bar
        menuBar.addMenu(fileMenu)
        menuBar.addMenu(settingMenu)
        menuBar.addMenu(self.helpMenu)
        # menuBar.addMenu(canInfoMenu) # !!! not in use for now

        # adding responses
        # file menu responses
        self.varCANlog.triggered.connect(lambda: self.on_SaveCANlogAsText_clicked())
        self.varExit.triggered.connect(lambda: self.on_Exit_clicked())
        # setting menu responses
        self.varCAN0.triggered.connect(self.on_MenuSettCANChCAN0_clicked)
        self.varCAN1.triggered.connect(self.on_MenuSettCANChCAN1_clicked)
        self.varCANboth.triggered.connect(self.on_MenuSettCANChCANBoth_clicked)
        self.varbdRate125.triggered.connect(self.on_MenuSettCANBdRate125_clicked)
        self.varbdRate250.triggered.connect(self.on_MenuSettCANBdRate250_clicked)
        self.varbdRate500.triggered.connect(self.on_MenuSettCANBdRate500_clicked)
        # Help menu responses
        self.menuHelpDoc.triggered.connect(self.on_MenuHelpDoc_clicked)
        self.menuHelpAbt.triggered.connect(self.on_MenuHelpAbt_clicked)
        # get triggered as soon as menu_button is clicked # !!! not in use for now
        # self.canMon.triggered.connect(lambda : self.on_CANMon_clicked())
        # self.cansend.triggered.connect(lambda : self.on_CANSend_clicked())
        # self.config.triggered.connect(lambda: self.on_CANInfo_clicked())

    def on_SaveCANlogAsText_clicked(self):
        """
        :Description:
            function to be called when the save CAN-Log as text menu is pressed
        :return: nth
        """

        print("----->>> prompt to save")
        file = open("logs/CAN_Signals.txt", "w")
        file.write(
            "|     Time-Intervals      |        ID (HEX)        |       dir (Rx/Tx)        |         DLC          |         Data         |")
        file.close()

    def on_Exit_clicked(self):
        """
        :Description:
            function to be called when the exit option is pressed
        :return: nth
        """

        print("----->>> prompt to exit")

        ''' this code was written by Sab before... do we need all this?
        class Startup(object):
            def setup_ui(self, Dialog):
                Dialog.setObjectName("Dialog")
                self.start_button = QtWidgets.QPushButton('', Dialog)
                self.start_button.clicked.connect(self.start_program)
            class Ui_MainWindow(object):
                def setupUi(self, MainWindow):
                    font = QFont("Times", 30, QFont.Bold)
                    MainWindow.setObjectName("NBA Predictor")
                    MainWindow.resize(1150, 790)
                    self.centralwidget = QtWidgets.QWidget(MainWindow)
                def start_program(self):
                    # segmentation = QtWidgets.QApplication(sys.argv)
                    self.mainWindow = QtWidgets.QMainWindow()
                    ui.setupUi(self.mainWindow)
                    self.mainWindow.show()
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        global ui
        ui = Startup()
        ui.setup_ui(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
        '''

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setWindowTitle("Exit Window")
        msg.setText("Want to exit?")
        msg.setInformativeText("Warning: CAN-Log file is not saved.")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.buttonClicked.connect(msg)

        retval = msg.exec_()

    def on_MenuSettCANChCAN0_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-CANChennel-CAN0
        :return: nth
        """

        print("----->>> CAN-Channel-0 is activated!")

        """ setting CAN0 checked on click and unchecking all others """
        self.varCAN0.setChecked(True)
        #self.tab_widget.ch0.setChecked(True)
        self.varCAN1.setChecked(False)
        self.varCANboth.setChecked(False)

        # activating can0
        #canUt.confCAN0Channel()

        consText = WidgetTab(self)
        #_, consText = consText.createGUI_CANInfo()
        #consText.setText('---> CAN-Channel-halalalala selected!')

    def on_MenuSettCANChCAN1_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-CANChennel-CAN1
        :return: nth
        """

        print("----->>> CAN-Channel-1 is activated!")

        """ setting CAN1 checked on click and unchecking all others """
        self.varCAN1.setChecked(True)
        self.tab_widget.ch1.setChecked(True)
        self.varCAN0.setChecked(False)
        self.varCANboth.setChecked(False)

    def on_MenuSettCANChCANBoth_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-CANChennel-CANBoth
        :return: nth
        """

        print("----->>> both CAN-Channels are activated!")

        """ setting CAN-Both checked on click and unchecking all others """
        self.varCANboth.setChecked(True)
        self.tab_widget.chB.setChecked(True)
        self.varCAN0.setChecked(False)
        self.varCAN1.setChecked(False)

    def on_MenuSettCANBdRate125_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-BDRate-125
        :return: nth
        """

        print("----->>> Baudrate 125kBd configured!")

        """ setting BDRate-125 checked on click and unchecking all others """
        self.varbdRate125.setChecked(True)
        #self.tab_widget.bd1.setChecked(True)
        self.varbdRate250.setChecked(False)
        self.varbdRate500.setChecked(False)

        # setting Baudrate to 125kBd
        #canUt.confCAN0BdRate125()
        #guiWid = createGUI()
        #guiWid.consMsgMonitor.append('--->')

    def on_MenuSettCANBdRate250_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-BDRate-125
        :return: nth
        """

        print("----->>> Baudrate 125kBd configured!")

        """ setting BDRate-125 checked on click and unchecking all others """
        self.varbdRate250.setChecked(True)
        self.tab_widget.bd2.setChecked(True)
        self.varbdRate125.setChecked(False)
        self.varbdRate500.setChecked(False)

        # setting Baudrate to 125kBd
        canUt.confCAN0BdRate125()

    def on_MenuSettCANBdRate500_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-BDRate-500
        :return: nth
        """

        print("----->>> Baudrate 500kBd configured!")

        """ setting BDRate-500 checked on click and unchecking all others """
        self.varbdRate500.setChecked(True)
        self.tab_widget.bd3.setChecked(True)
        self.varbdRate125.setChecked(False)
        self.varbdRate250.setChecked(False)

        # setting Baudrate to 500kBd
        canUt.confCAN0BdRate500()

    def on_MenuHelpDoc_clicked(self):
        print("----->>> MenuHelpDoc clicked!")
        msg = QMessageBox()
        msg.setWindowTitle("Doc")
        msg.setText(
            "Here we together work to help each other.\nWe work in individual module to complete this project. \n list of frnd with Github link \n1. Jabed \n2. Gyan\n3. Tek \n4. Mukesh \n5. Sabin \n6. Bibek")
        x = msg.exec_()

    def on_MenuHelpAbt_clicked(self):
        print("----->>> MenuHelpAbt clicked!")
        msg = QMessageBox()
        msg.setWindowTitle("About this Project")
        msg.setText(
            "we are legend. our team is very slow in term of doing project. so we are still doing a single project form a year")
        x = msg.exec_()


def main():
    app = QApplication(sys.argv)
    ex = GUI_MainWin()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# ****************************** END OF FILE ******************************