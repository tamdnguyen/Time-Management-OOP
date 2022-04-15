from random import expovariate
from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget, QMessageBox, 
    QPushButton, QLabel, QMenu,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QInputDialog, QAction)
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
        self.time_conversion = QPushButton("Time Conversion", self)
        time_conversion_menu = QMenu(self)
        time_conversion_menu.addAction("Hour:Min:Sec", lambda: self.change_time_expression(1))
        time_conversion_menu.addAction("Min:Sec", lambda: self.change_time_expression(2))
        time_conversion_menu.addAction("Finnish ECTS (1ECT=27hour)", lambda: self.change_time_expression(3))
        time_conversion_menu.addAction("Standard Expression", lambda: self.change_time_expression(4))
        self.time_conversion.setMenu(time_conversion_menu)

        self.activity_date = QLabel(str(self.dayTask.get_date()), self)
        self.activity_date.setStyleSheet('font-size: 18pt;')
        self.add_activity_btn = QPushButton("Add Activity", self)

        # add the widgets to the GUI Layout
        title_layout.addWidget(self.time_conversion, 1, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        title_layout.addWidget(self.activity_date, 4, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        title_layout.addWidget(self.add_activity_btn, 1, alignment=Qt.AlignRight | Qt.AlignVCenter)

        # add functionality for the widgets
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
        self.restart_btn = QPushButton("Restart", self)
        self.stats_btn = QPushButton("Statistics", self)

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        mainbutton_layout.addWidget(self.start_btn, alignment)
        mainbutton_layout.addWidget(self.stop_btn, alignment)
        mainbutton_layout.addWidget(self.reset_btn, alignment)
        mainbutton_layout.addWidget(self.restart_btn, alignment)
        mainbutton_layout.addWidget(self.stats_btn, alignment)

        # add functionality for the buttons
        self.start_btn_widget()
        self.stop_btn_widget()
        self.reset_btn_widget()
        self.restart_btn_widget()


    def otherbutton_widget(self, otherbutton_layout):
        """
        This method adds the widgets to the other button section of the GUI
        """
        # create the widgets
        self.edit_btn = QPushButton("Edit", self)
        self.delete_btn = QPushButton("Delete", self)
        self.pomodoro_btn = QPushButton("Pomodoro", self)
        self.more_btn = QPushButton("More", self)
        self.help_btn = QPushButton("Need help?", self)

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        otherbutton_layout.addWidget(self.edit_btn, alignment)
        otherbutton_layout.addWidget(self.delete_btn, alignment)
        otherbutton_layout.addWidget(self.pomodoro_btn, alignment)
        otherbutton_layout.addWidget(self.more_btn, alignment)
        otherbutton_layout.addWidget(self.help_btn, alignment)

        # add functionality for the buttons
        self.edit_btn_widget()
        self.delete_btn_widget()
        self.more_btn_widget()
        self.help_btn_widget()


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


    def change_time_expression(self, format):
        """
        This method changes the value of self.time_format, which will also changes the time expression in the GUI widget.
        """
        self.time_format = format


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
                warning_box.setText("Maximum 5 activities can\nbe added at the same time.\n\nEdit/Delete an activity if\nyou want to add a new one.\n\nActivities' timers are stopped,\nplease click Start button to continue.")
                warning_box.exec()
            else:
                info_box = QMessageBox()
                info_box.setIcon(QMessageBox.Information)
                info_box.setWindowTitle("Notification")
                info_box.setText("Timers are stopped, please\nclick Start button to continue.")
                info_box.exec()


    def start_btn_widget(self):
        """
        This method creates the content and adds functionality for the Start button on the GUI
        """
        activities_list = self.dayTask.get_activities()

        start_menu = QMenu(self)

        try:
            start_activity1_act = QAction(activities_list[0].get_name(), self)
            start_activity1_act.triggered.connect(activities_list[0].get_timer().start)
            start_menu.addAction(start_activity1_act)

            start_activity2_act = QAction(activities_list[1].get_name(), self)
            start_activity2_act.triggered.connect(activities_list[1].get_timer().start)
            start_menu.addAction(start_activity2_act)

            start_activity3_act = QAction(activities_list[2].get_name(), self)
            start_activity3_act.triggered.connect(activities_list[2].get_timer().start)
            start_menu.addAction(start_activity3_act)

            start_activity4_act = QAction(activities_list[3].get_name(), self)
            start_activity4_act.triggered.connect(activities_list[3].get_timer().start)
            start_menu.addAction(start_activity4_act)

            start_activity5_act = QAction(activities_list[4].get_name(), self)
            start_activity5_act.triggered.connect(activities_list[4].get_timer().start)
            start_menu.addAction(start_activity5_act)
        except IndexError:
            pass

        self.start_btn.setMenu(start_menu)


    def stop_btn_widget(self):
        """
        This method creates the content and adds functionality for the Stop button on the GUI
        """
        activities_list = self.dayTask.get_activities()

        stop_menu = QMenu(self)

        try:
            stop_activity1_act = QAction(activities_list[0].get_name(), self)
            stop_activity1_act.triggered.connect(activities_list[0].get_timer().stop)
            stop_menu.addAction(stop_activity1_act)

            stop_activity2_act = QAction(activities_list[1].get_name(), self)
            stop_activity2_act.triggered.connect(activities_list[1].get_timer().stop)
            stop_menu.addAction(stop_activity2_act)

            stop_activity3_act = QAction(activities_list[2].get_name(), self)
            stop_activity3_act.triggered.connect(activities_list[2].get_timer().stop)
            stop_menu.addAction(stop_activity3_act)

            stop_activity4_act = QAction(activities_list[3].get_name(), self)
            stop_activity4_act.triggered.connect(activities_list[3].get_timer().stop)
            stop_menu.addAction(stop_activity4_act)

            stop_activity5_act = QAction(activities_list[4].get_name(), self)
            stop_activity5_act.triggered.connect(activities_list[4].get_timer().stop)
            stop_menu.addAction(stop_activity5_act)
        except IndexError:
            pass

        self.stop_btn.setMenu(stop_menu)


    def reset_btn_widget(self):
        """
        This method creates the content and adds functionality for the Reset button on the GUI
        """
        activities_list = self.dayTask.get_activities()

        reset_menu = QMenu(self)

        try:
            reset_activity1_act = QAction(activities_list[0].get_name(), self)
            reset_activity1_act.triggered.connect(activities_list[0].get_timer().reset)
            reset_menu.addAction(reset_activity1_act)

            reset_activity2_act = QAction(activities_list[1].get_name(), self)
            reset_activity2_act.triggered.connect(activities_list[1].get_timer().reset)
            reset_menu.addAction(reset_activity2_act)

            reset_activity3_act = QAction(activities_list[2].get_name(), self)
            reset_activity3_act.triggered.connect(activities_list[2].get_timer().reset)
            reset_menu.addAction(reset_activity3_act)

            reset_activity4_act = QAction(activities_list[3].get_name(), self)
            reset_activity4_act.triggered.connect(activities_list[3].get_timer().reset)
            reset_menu.addAction(reset_activity4_act)

            reset_activity5_act = QAction(activities_list[4].get_name(), self)
            reset_activity5_act.triggered.connect(activities_list[4].get_timer().reset)
            reset_menu.addAction(reset_activity5_act)
        except IndexError:
            pass

        self.reset_btn.setMenu(reset_menu)


    def restart_btn_widget(self):
        """
        This method creates the content and adds functionality for the Restart button on the GUI
        """
        activities_list = self.dayTask.get_activities()

        restart_menu = QMenu(self)

        try:
            restart_activity1_act = QAction(activities_list[0].get_name(), self)
            restart_activity1_act.triggered.connect(activities_list[0].get_timer().restart)
            restart_menu.addAction(restart_activity1_act)

            restart_activity2_act = QAction(activities_list[1].get_name(), self)
            restart_activity2_act.triggered.connect(activities_list[1].get_timer().restart)
            restart_menu.addAction(restart_activity2_act)

            restart_activity3_act = QAction(activities_list[2].get_name(), self)
            restart_activity3_act.triggered.connect(activities_list[2].get_timer().restart)
            restart_menu.addAction(restart_activity3_act)

            restart_activity4_act = QAction(activities_list[3].get_name(), self)
            restart_activity4_act.triggered.connect(activities_list[3].get_timer().restart)
            restart_menu.addAction(restart_activity4_act)

            restart_activity5_act = QAction(activities_list[4].get_name(), self)
            restart_activity5_act.triggered.connect(activities_list[4].get_timer().restart)
            restart_menu.addAction(restart_activity5_act)
        except IndexError:
            pass

        self.restart_btn.setMenu(restart_menu)


    def edit_btn_widget(self):
        """
        This method creates the content and adds functionality for the Edit button on the GUI
        """
        activities_list = self.dayTask.get_activities()

        edit_menu = QMenu(self)

        try:
            edit_menu.addAction(activities_list[0].get_name(), lambda: self.rename_dialog(activities_list[0]))
            edit_menu.addAction(activities_list[1].get_name(), lambda: self.rename_dialog(activities_list[1]))
            edit_menu.addAction(activities_list[2].get_name(), lambda: self.rename_dialog(activities_list[2]))
            edit_menu.addAction(activities_list[3].get_name(), lambda: self.rename_dialog(activities_list[3]))
            edit_menu.addAction(activities_list[4].get_name(), lambda: self.rename_dialog(activities_list[4]))

        except IndexError:
            pass

        self.edit_btn.setMenu(edit_menu)


    def delete_btn_widget(self):
        """
        This method creates the content and adds functionality for the Edit button on the GUI

        TODO: Change the label of the activity_* and activity_*_time to the default after deleting
        """
        activities_list = self.dayTask.get_activities()

        delete_menu = QMenu(self)

        try:
            delete_menu.addAction(activities_list[0].get_name(), lambda: self.delete_activity(activities_list[0]))
            delete_menu.addAction(activities_list[1].get_name(), lambda: self.delete_activity(activities_list[1]))
            delete_menu.addAction(activities_list[2].get_name(), lambda: self.delete_activity(activities_list[2]))
            delete_menu.addAction(activities_list[3].get_name(), lambda: self.delete_activity(activities_list[3]))
            delete_menu.addAction(activities_list[4].get_name(), lambda: self.delete_activity(activities_list[4]))

        except IndexError:
            pass

        self.delete_btn.setMenu(delete_menu)


    def more_btn_widget(self):
        """
        This method creates the content and adds functionality for the More button on the GUI
        """
        more_menu = QMenu(self)

        more_menu.addAction("Export", lambda: self.export_btn())
        more_menu.addAction("Import", lambda: self.export_btn())
        more_menu.addAction("Next Day", lambda: self.export_btn())
        more_menu.addAction("Choose Day", lambda: self.export_btn())

        self.more_btn.setMenu(more_menu)


    def help_btn_widget(self):
        """
        This method shows a pop up windows to show some guidance for the user.

        TODO: Add content for help button
        """
        help_box = QMessageBox()
        help_box.setIcon(QMessageBox.Information)
        help_box.setWindowTitle("Help Function")
        help_box.setText("Exported files are in CSV type and are\nbest viewed with Excel. For visualizing data,\nplease use Stats button in the app instead.\nExported file can be found in folder time_data.")
        


    def rename_dialog(self, activity):
        """
        This method creates an InputDialog to get the new_name for the activities

        See method edit_btn_widget().
        """
        activity_name, ok = QInputDialog.getText(self, 'Rename Activity',
                                        'Enter new activity name:')

        if ok:
            activity.edit_name(activity_name)


    def delete_activity(self, activity):
        """
        This method deletes an activity in the list of activities of the dayTask object.

        Before performing the delete action, it shows a pop up windows to get the confirmation from the user.
        """
        confirmation_box = QMessageBox()
        confirmation_box.setIcon(QMessageBox.Critical)
        confirmation_box.setWindowTitle("Confirm Activity Deletion")
        confirmation_box.setText("Deleted activities can't be recovered.\nThis action is permanent and can't be undone.")
        confirmation_box.setInformativeText("Do you want to proceed?")
        confirmation_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation_box.setDefaultButton(QMessageBox.Yes)
        confirmation = confirmation_box.exec()

        if confirmation == QMessageBox.Yes:
            self.dayTask.delete_activities(activity)


    def export_btn(self):
        """
        This method exports the data of the dayTask and AllTask.
        
        Before performing the export action, it shows a pop up windows to get the confirmation from the user.
        """
        export_box = QMessageBox()
        export_box.setIcon(QMessageBox.Question)
        export_box.setWindowTitle("Confirm Exporting Data")
        export_box.setText("Exported files are in CSV type and are\nbest viewed with Excel.For visualizing data,\nplease use Stats button in the app instead.\nExported file can be found in folder time_data.")
        export_box.setInformativeText("Do you want to proceed?")
        export_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        export_box.setDefaultButton(QMessageBox.Yes)
        confirmation = export_box.exec()

        if confirmation == QMessageBox.Yes:
            self.dayTask.export_data()
            self.dayTask.get_allTask().export_file()


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

        See method change_time_expression()
        """
        format = self.time_format

        activity_widget_dict = self.activity_widget_dict()

        for key, value in activity_widget_dict.items():
            value[0].setText(key.get_name())
            value[1].setText(key.set_time_format(format))

    
    def update_btn_functionality(self):
        """
        This method updates the functionality of all the buttons in method main_btn() and other_btn() so that the menu inside these buttons will show the new activities options when new activities are added
        """
        self.start_btn_widget()
        self.stop_btn_widget()
        self.reset_btn_widget()
        self.restart_btn_widget()
        self.edit_btn_widget()
        self.delete_btn_widget()


    def updateAll(self):
        """
        This method combines different updates of the backend info vs GUI widget display, and it makes all these updates at once
        """
        self.update_activity_info()
        self.update_btn_functionality()


