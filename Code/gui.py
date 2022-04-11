from ctypes import alignment
from tracemalloc import stop
from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget, QMessageBox, 
    QPushButton, QLabel, QMenu,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QInputDialog)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class Color(QWidget):
    """
    This class creates a box with color to create the initial layout of the program
    """
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class GUI(QWidget):
    """
    The class GUI create the graphical user interface of the program using PyQt5
    """
    def __init__(self):
        """
        This method creates the initial GUI of the program
        """
        super().__init__()

        self.layout()
        self.init_windows()

    def init_windows(self):
        """
        This method set the windows of the app
        and put it in the center of the screen
        """
        self.resize(500, 500)
        self.center()

        self.setWindowTitle('Time Management App')
        self.show()

    def layout(self):
        """
        This method creates a layout for the program

        The widget will initially be a Color widget (see class Color above)
        However, the widget can be changed later to add the real widget we want
        """
        app_layout  = QVBoxLayout() # this is the outermost layout which contains every childLayout

        title_layout = QHBoxLayout() # This is the first row in the designed UI, which has 3 columns: the button switch, activity date, button to add new activity

        activity_layout = QGridLayout() # This is the section for activities and their timer

        mainbutton_layout = QHBoxLayout() # This section is for the main buttons: start, stop, reset, pomodoro setting, show statistics (stats + charts)

        otherbutton_layout = QHBoxLayout() # This section is for the other buttons: show day, next day, export, import 

        # add the widet to the sections' layout
        self.title_widget(title_layout)
        self.activity_widget(activity_layout)
        self.mainbutton_widget(mainbutton_layout)
        self.otherbutton_widget(otherbutton_layout)

        # Nest the inner layouts to the app_layout
        app_layout.addLayout(title_layout, stretch=1)
        app_layout.addLayout(activity_layout, stretch=10)
        app_layout.addLayout(mainbutton_layout, stretch=1)
        app_layout.addLayout(otherbutton_layout, stretch=1)
        
        self.setLayout(app_layout)


    def title_widget(self, title_layout):
        """
        This method adds the widgets to the title section of the GUI
        """
        # create the widgets and add the function for them
        # TODO: add the action when user choose the item in the dropdown list
        self.time_conversion = QPushButton("Time Conversion", self)
        time_conversion_menu = QMenu(self)
        time_conversion_menu.addAction("Hour:Min:Sec", lambda: self.activity_date.setText("<h1>H:M:S</h1>"))
        time_conversion_menu.addAction("Min:Sec")
        time_conversion_menu.addAction("Finnish ECTS (1ECT=27hour)")
        time_conversion_menu.addAction("Standard Expression")
        self.time_conversion.setMenu(time_conversion_menu)

        # TODO: connect the text h1 below to the real date show of the DayTask
        self.activity_date = QLabel("<h1>{:s}</h1>".format("Current Activity Date"), self)
        
        self.add_activity = QPushButton("Add Activity", self)
        self.add_activity.clicked.connect(self.show_add_dialog)

        # add the widgets to the GUI Layout
        title_layout.addWidget(self.time_conversion, 1, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        title_layout.addWidget(self.activity_date, 4, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        title_layout.addWidget(self.add_activity, 1, alignment=Qt.AlignRight | Qt.AlignVCenter)

    def activity_widget(self, activity_layout):
        """
        This method adds the widgets to the activity section of the GUI
        """
        # create the widgets
        # TODO: when change the setText() QLabel, use <h2> tag for these widgets
        self.activity_1 = QLabel("Task 1", self)
        self.activity_1_time = QLabel("00:00:00", self)
        self.activity_2 = QLabel("Task 2", self)
        self.activity_2_time = QLabel("00:00:00", self)
        self.activity_3 = QLabel("Task 3", self)
        self.activity_3_time = QLabel("00:00:00", self)
        self.activity_4 = QLabel("Task 4", self)
        self.activity_4_time = QLabel("00:00:00", self)
        self.activity_5 = QLabel("Task 5", self)
        self.activity_5_time = QLabel("00:00:00", self)

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        activity_layout.addWidget(self.activity_1, 0, 0, alignment)
        activity_layout.addWidget(self.activity_1_time, 0, 1, alignment)
        activity_layout.addWidget(self.activity_2, 1, 0, alignment)
        activity_layout.addWidget(self.activity_2_time, 1, 1, alignment)
        activity_layout.addWidget(self.activity_3, 2, 0, alignment)
        activity_layout.addWidget(self.activity_3_time, 2, 1, alignment)
        activity_layout.addWidget(self.activity_4, 3, 0, alignment)
        activity_layout.addWidget(self.activity_4_time, 3, 1, alignment)
        activity_layout.addWidget(self.activity_5, 4, 0, alignment)
        activity_layout.addWidget(self.activity_5_time, 4, 1, alignment)

    def mainbutton_widget(self, mainbutton_layout):
        """
        This method adds the widgets to the main button section of the GUI
        """
        # create the widgets
        self.start_btn = QPushButton("Start", self)
        self.stop_btn = QPushButton("Stop", self)
        self.reset_btn = QPushButton("Reset", self)
        self.edit_btn = QPushButton("Edit", self)
        self.stats_btn = QPushButton("Statistics", self)

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        mainbutton_layout.addWidget(self.start_btn, alignment)
        mainbutton_layout.addWidget(self.stop_btn, alignment)
        mainbutton_layout.addWidget(self.reset_btn, alignment)
        mainbutton_layout.addWidget(self.edit_btn, alignment)
        mainbutton_layout.addWidget(self.stats_btn, alignment)

    def otherbutton_widget(self, otherbutton_layout):
        """
        This method adds the widgets to the other button section of the GUI
        """
        # create the widgets
        self.export_btn = QPushButton("Export", self)
        self.import_btn = QPushButton("Import", self)
        self.next_day_btn = QPushButton("Next Day", self)
        self.pomodoro_btn = QPushButton("Pomodoro", self)
        self.help_btn = QPushButton("Need help?", self)

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        otherbutton_layout.addWidget(self.export_btn, alignment)
        otherbutton_layout.addWidget(self.import_btn, alignment)
        otherbutton_layout.addWidget(self.next_day_btn, alignment)
        otherbutton_layout.addWidget(self.pomodoro_btn, alignment)
        otherbutton_layout.addWidget(self.help_btn, alignment)

    def show_add_dialog(self):
        """
        This method shows a pop up windows to ask for the name of the activity"""
        text, ok = QInputDialog.getText(self, 'Activity Name',
                                        'Enter activity name:')

        if ok:
            self.activity_1.setText(str(text))

    def closeEvent(self, event):
        """
        This method confirms if the user wants to quit or not
        """
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        """
        This method centers the window on the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


