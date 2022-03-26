"""
 ******************************************************************************
 * @file: gui.py
 * @author: Jabed-Akhtar
 * @date: 26.03.2022
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
WINDOW_TITLE = "Raspi-CAM-ObjectDetector App"

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
        self.main_widget = WidgetTab(self)
        self.setCentralWidget(self.main_widget)
        #self.tab_widget.setGeometry(0, 20, AW, AH - 20)
        self.main_widget.move(0, 20)
        self.main_widget.setMinimumSize(500, 500)

        # showing the GUI
        self.showMaximized()  # showing the GUI will maximized size of display
        self.show()

    def initOthers(self):
        """
        :Description:
            here other initialisations, beside the GUIs, are done
        :return: nth
        """

        self.on_SelM_m1_clicked()

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
        self.varSaveLog = QAction('save log as csv')
        fileMenu.addAction(self.varSaveLog)
        self.varExit = QAction('Exit', fileMenu)
        fileMenu.addAction(self.varExit)
        # Setting menu **********
        settingMenu = QMenu("&Settings", self)
        # menu - Setting
        settingSelectModel = settingMenu.addMenu('select Model')
        # adding more Actions to Setting-Menu-CANChannels
        self.settingSelM_m1 = QAction('model1', self, checkable=True)
        settingSelectModel.addAction(self.settingSelM_m1)
        self.settingSelM_m1.setChecked(True)
        self.settingSelM_m2 = QAction('model2', self, checkable=True)
        settingSelectModel.addAction(self.settingSelM_m2)
        self.settingSelM_m3 = QAction('model3', self, checkable=True)
        settingSelectModel.addAction(self.settingSelM_m3)
        # Help menu **********
        self.helpMenu = QMenu("&Help", self)
        self.menuHelpDoc = self.helpMenu.addAction('Doc')
        self.menuHelpAbt = self.helpMenu.addAction('About this App')

        # adding components to menu bar
        menuBar.addMenu(fileMenu)
        menuBar.addMenu(settingMenu)
        menuBar.addMenu(self.helpMenu)
        # menuBar.addMenu(canInfoMenu) # !!! not in use for now

        # adding responses
        # file menu responses
        self.varSaveLog.triggered.connect(lambda: self.on_SaveLog_clicked())
        self.varExit.triggered.connect(lambda: self.on_Exit_clicked())
        # setting menu responses
        self.settingSelM_m1.triggered.connect(self.on_SelM_m1_clicked)
        self.settingSelM_m2.triggered.connect(self.on_SelM_m2_clicked)
        self.settingSelM_m3.triggered.connect(self.on_SelM_m3_clicked)
        # Help menu responses
        self.menuHelpDoc.triggered.connect(self.on_MenuHelpDoc_clicked)
        self.menuHelpAbt.triggered.connect(self.on_MenuHelpAbt_clicked)

    def on_SaveLog_clicked(self):
        """
        :Description:
            function to be called when the save CAN-Log as text menu is pressed
        :return: nth
        """
        '''
        print("----->>> prompt to save")
        file = open("logs/CAN_Signals.txt", "w")
        file.write(
            "|     Time-Intervals      |        ID (HEX)        |       dir (Rx/Tx)        |         DLC          |         Data         |")
        file.close()
        '''

        pass

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

    def on_SelM_m1_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-CANChennel-CAN0
        :return: nth
        """

        print("----->>> CAN-Channel-0 is activated!")

        """ setting CAN0 checked on click and unchecking all others """
        self.settingSelM_m1.setChecked(True)
        #self.tab_widget.ch0.setChecked(True)
        self.settingSelM_m2.setChecked(False)
        self.settingSelM_m3.setChecked(False)

        # activating can0
        #canUt.confCAN0Channel()

        consText = WidgetTab(self)
        #_, consText = consText.createGUI_CANInfo()
        #consText.setText('---> CAN-Channel-halalalala selected!')

    def on_SelM_m2_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-CANChennel-CAN1
        :return: nth
        """

        print("----->>> CAN-Channel-1 is activated!")

        """ setting CAN1 checked on click and unchecking all others """
        self.settingSelM_m2.setChecked(True)
        #self.tab_widget.ch1.setChecked(True)
        self.settingSelM_m1.setChecked(False)
        self.settingSelM_m3.setChecked(False)

    def on_SelM_m3_clicked(self):
        """
        :Description:
            function to be called/executed on clicking MenuBar-Setting-CANChennel-CANBoth
        :return: nth
        """

        print("----->>> both CAN-Channels are activated!")

        """ setting CAN-Both checked on click and unchecking all others """
        self.settingSelM_m3.setChecked(True)
        #self.tab_widget.chB.setChecked(True)
        self.settingSelM_m1.setChecked(False)
        self.settingSelM_m2.setChecked(False)

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