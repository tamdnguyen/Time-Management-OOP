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

        # Set a variable to indicate the format of time_expression
        self.time_format = 1

        # Set a timer to call the update function periodically
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateAll)
        self.timer.start(1000) # Update the time on the screen after every second
        

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
        time_conversion_menu.addAction("Hour:Min:Sec", self.change_time_expression(1))
        time_conversion_menu.addAction("Min:Sec", self.change_time_expression(2))
        time_conversion_menu.addAction("Finnish ECTS (1ECT=27hour)", self.change_time_expression(3))
        time_conversion_menu.addAction("Standard Expression", self.change_time_expression(4))
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
        activity_name, ok = QInputDialog.getText(self, 'Activity Name',
                                        'Enter activity name:')

        if ok:
            activity = Activity(activity_name)

            add_successfully = self.dayTask.add_activities(activity)

            if not add_successfully:
                warning_box = QMessageBox()
                warning_box.setIcon(QMessageBox.Warning)
                warning_box.setWindowTitle("Adding new activity failed")
                warning_box.setText("Maximum 5 activities can\nbe added at the same time.\n\nEdit/Delete an activity if\nyou want to add a new one.")
                warning_box.exec()
    

    def index_widget_dict(self):
        """
        This method returns a dictionary that maps the INDEX of the activities in the DayTask object to the corresponding GUI widget.
        """
        index_widget_dict = {0: [self.activity_1, self.activity_1_time], 
                            1: [self.activity_2, self.activity_2_time], 
                            2: [self.activity_3, self.activity_3_time], 
                            3: [self.activity_4, self.activity_4_time], 
                            4: [self.activity_5, self.activity_5_time]}
        return index_widget_dict


    def activity_widget_dict(self):
        """
        This method maps the activities of the DayTask object to the corresponding GUI widget in the index_widget_dict

        When all 5 activities are added to the DayTask object, the dictionary is

        activity_widget_dict = {
            self.dayTask.get_activities()[0]: [self.activity_1, self.activity_1_time], 
            self.dayTask.get_activities()[1]: [self.activity_2, self.activity_2_time], 
            self.dayTask.get_activities()[2]: [self.activity_3, self.activity_3_time], 
            self.dayTask.get_activities()[3]: [self.activity_4, self.activity_4_time], 
            self.dayTask.get_activities()[4]: [self.activity_5, self.activity_5_time]
            }
        """
        activity_widget_dict = {}

        index_widget_dict = self.index_widget_dict()
        activities_list = self.dayTask.get_activities()

        try:
            for key, value in index_widget_dict.items():
                main_key = activities_list[key]
                main_value = value
                activity_widget_dict[main_key] = main_value
        except IndexError:
            pass

        return activity_widget_dict


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


    def update_activity_info(self):
        """
        This method updates the name and the timer of the activities in the dayTask object and shows it in the corresponding GUI widget

        This method also shows the time according to the time expression user choose.
        """

        """
        - format: this is the format for the set_time_format() method of class Activity.
            The value is set to the self.time_format of the class. In this way, when there are changes with the TimeConversion dropdown list, only the self.time_format is changed, and everything is updated. The default time expression format is 1.

        See method TODO: change_time_expression()
        """
        format = self.time_format

        activity_widget_dict = self.activity_widget_dict()

        for key, value in activity_widget_dict.items():
            value[0].setText(key.get_name())
            value[1].setText(key.set_time_format(format))

    
    def change_time_expression(self, format):
        """
        This method changes the value of self.time_format, which will also changes the time expression in the GUI widget.
        """
        self.time_format = format


    def updateAll(self):
        """
        This method combines different updates of the backend info vs GUI widget display, and it makes all these updates at once
        """
        self.update_activity_info()


