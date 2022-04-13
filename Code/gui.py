from ctypes import alignment
from tracemalloc import stop
from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget, QMessageBox, 
    QPushButton, QLabel, QMenu,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QInputDialog)
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, QTimer
from activity import Activity


class GUI(QWidget):
    """
    The class GUI create the graphical user interface of the program using PyQt5
    """
    def __init__(self, dayTask):
        """
        This method creates the initial GUI of the program
        """
        super().__init__()
        self.dayTask = dayTask

        self.layout()
        self.init_windows()

        # Set a timer to call the update function periodically
        # TODO: create the self.show_time() method and enable next 3 lines
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.show_time())
        # self.timer.start(1000) # Update the time on the screen after every second


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
        time_conversion_menu.addAction("Hour:Min:Sec")
        time_conversion_menu.addAction("Min:Sec")
        time_conversion_menu.addAction("Finnish ECTS (1ECT=27hour)")
        time_conversion_menu.addAction("Standard Expression")
        self.time_conversion.setMenu(time_conversion_menu)

        self.activity_date = QLabel(str(self.dayTask.get_date()), self)
        self.activity_date.setStyleSheet('font-size: 18pt;')
        self.add_activity_btn = QPushButton("Add Activity", self)

        # add the widgets to the GUI Layout
        title_layout.addWidget(self.time_conversion, 1, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        title_layout.addWidget(self.activity_date, 4, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        title_layout.addWidget(self.add_activity_btn, 1, alignment=Qt.AlignRight | Qt.AlignVCenter)

        # add the actions for the widgets
        self.add_activity_btn.clicked.connect(self.add_activity)


    def activity_widget(self, activity_layout):
        """
        This method adds the widgets to the activity section of the GUI

        TODO: Change the label to the real activities in DayTask
        """
        # create the widgets
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

        # change the font-size of the label
        self.activity_1.setStyleSheet('font-size: 14pt;')
        self.activity_2.setStyleSheet('font-size: 14pt;')
        self.activity_3.setStyleSheet('font-size: 14pt;')
        self.activity_4.setStyleSheet('font-size: 14pt;')
        self.activity_5.setStyleSheet('font-size: 14pt;')
        self.activity_1_time.setStyleSheet('font-size: 14pt;')
        self.activity_2_time.setStyleSheet('font-size: 14pt;')
        self.activity_3_time.setStyleSheet('font-size: 14pt;')
        self.activity_4_time.setStyleSheet('font-size: 14pt;')
        self.activity_5_time.setStyleSheet('font-size: 14pt;')

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


    def add_activity(self):
        """
        This method shows a pop up windows to ask for the name of the activity and create new activity for the program
        """
        # this dictionary maps the activities in the DayTask list to the widget in the frontend GUI
        gui_frontend_dict = {0: [self.activity_1, self.activity_1_time], 
                            1: [self.activity_2, self.activity_2_time], 
                            2: [self.activity_3, self.activity_3_time], 
                            3: [self.activity_4, self.activity_4_time], 
                            4: [self.activity_5, self.activity_5_time]}
        
        widget_index = self.dayTask.get_len()

        activity_name, ok = QInputDialog.getText(self, 'Activity Name',
                                        'Enter activity name:')

        if ok:
            activity = Activity(activity_name)

            if self.dayTask.add_activities(activity):
                widget_name_connected = gui_frontend_dict[widget_index][0]
                widget_time_connected = gui_frontend_dict[widget_index][1]
                widget_name_connected.setText(activity_name)
                widget_time_connected.setText(activity.set_time_format(1))
            else:
                warning_box = QMessageBox()
                warning_box.setIcon(QMessageBox.Warning)
                warning_box.setWindowTitle("Adding new activity failed")
                warning_box.setText("Maximum 5 activities can\nbe added at the same time.\n\nEdit/Delete an activity if\nyou want to add a new one.")
                warning_box.exec()
    

    def gui_backend_dict(self):
        """
        TODO: Figure out how to connect the activities in Daytask with the GUI widget
        Then can modify the add_activity() method above to be smarter and more convenient.
        In that way, widgets activity_* and activity_*_time can show the name and time of the activity
        better, also change the time_conversion value can be easier than current way of implementing the
        add_activity() method.
        """
        gui_backend_dict = {0: [self.activity_1, self.activity_1_time], 
                            1: [self.activity_2, self.activity_2_time], 
                            2: [self.activity_3, self.activity_3_time], 
                            3: [self.activity_4, self.activity_4_time], 
                            4: [self.activity_5, self.activity_5_time]}
        return gui_backend_dict


    def closeEvent(self, event):
        """
        This method confirms if the user wants to quit or not

        TODO: Add a save button to export the data file like the Word exit
        """
        reply = QMessageBox.question(self, 'Message',
                                     "Save the time management data?", QMessageBox.Yes |
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


    def show_time(self):
        # TODO: add the method to update the labels which show time of the activities
        # The label activity_*_time
        pass


