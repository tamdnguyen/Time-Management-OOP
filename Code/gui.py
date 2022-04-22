import datetime
from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget, QMessageBox, 
    QPushButton, QLabel, QMenu,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QInputDialog, QAction)
from PyQt5.QtCore import Qt, QTimer
from day_task import DayTask
from activity import Activity
from gui_help import HelpGUI
from gui_pomodoro_setting import PomodoroSettingGUI
from gui_choose_day import ChooseDaySettingGUI
from gui_statistics import StatisticsGUI
from pomodoro import Pomodoro
from date import Date


class GUI(QWidget):
    """
    The class GUI creates the graphical user interface of the program using PyQt5
    """
    def __init__(self, dayTask):
        """
        This method creates the initial GUI of the program
        """
        super().__init__()
        self.help = None # No help window is displayed

        self.pomodoro = None # No pomodoro reminder is turned on
        self.pomodoro_reminder = None

        self.dayTask = dayTask
        self.allTask = self.dayTask.get_allTask()

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
        self.resize(600, 600)
        self.center()

        self.setWindowTitle('Time Management App')
        self.show()


    def layout(self):
        """
        This method creates a layout for the program
        """
        app_layout  = QVBoxLayout() # this is the outermost layout which contains every childLayout

        title_layout = QHBoxLayout() # This is the first row in the designed UI, which has 3 columns: the button switch, activity date, button to add new activity

        activity_layout = QGridLayout() # This is the section for activities and their timer

        mainbutton_layout = QHBoxLayout() # This section is for the main buttons: start, stop, reset, pomodoro setting, show statistics (stats + charts)

        otherbutton_layout = QHBoxLayout() # This section is for the other buttons: show day, next day, export, import 

        # add the widget to the sections' layout
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
        self.stats_btn.clicked.connect(self.stats_btn_widget)

        # TODO: Create graph and pop up window show Statistics


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
        self.pomodoro_btn.clicked.connect(self.pomodoro_btn_widget)
        self.more_btn_widget()
        self.help_btn.clicked.connect(self.help_btn_widget)


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

        TODO: Fix same name activity
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


    def stats_btn_widget(self):
        """
        This method creates and shows a statistics GUI
        """
        self.statisticsGUI = StatisticsGUI(self.dayTask)
        self.statisticsGUI.show()


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


    def pomodoro_btn_widget(self):
        """
        This method creates a pop up window to ask for pomodoro setting and then
        """
        if self.pomodoro is None:
            self.pomodoro_setting = PomodoroSettingGUI()
            
        self.pomodoro_setting.accepted.connect(self.create_pomodoro)
        self.pomodoro_setting.show()
        

    def more_btn_widget(self):
        """
        This method creates the content and adds functionality for the More button on the GUI

        TODO: Choose Day buttons
        """
        more_menu = QMenu(self)

        more_menu.addAction("Export", lambda: self.export_btn())
        more_menu.addAction("Next Day", lambda: self.next_day_btn())
        more_menu.addAction("Choose Day", lambda: self.choose_day_btn())

        self.more_btn.setMenu(more_menu)


    def help_btn_widget(self):
        """
        This method shows a pop up windows to show some guidance for the user.
        """
        if self.help is None:
            self.help_box = HelpGUI()
        self.help_box.show()
        

    def create_pomodoro(self, values):
        """
        This method creates a pomodoro with the given configuration
        """
        worktime = int(values["worktime"])
        resttime = int(values["resttime"])

        self.pomodoro_reminder = Pomodoro(self.dayTask.get_activities(), worktime, resttime)


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
        export_box.setText("Exported files are in CSV type and are best\nviewed with Excel. For visualizing data,\nplease use Stats button in the app instead.\nExported file can be found in folder time_data.")
        export_box.setInformativeText("Do you want to proceed?")
        export_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        export_box.setDefaultButton(QMessageBox.Yes)
        confirmation = export_box.exec()

        if confirmation == QMessageBox.Yes:
            self.dayTask.export_data()
            self.dayTask.get_allTask().export_file()


    def next_day_btn(self):
        """
        This method creates a new windows that show the data of the next day of the current date of dayTask object
        """

        """
        First, we need to create a dayTask that uses parameter "tomorrow date" (tomorrow here means the tomorrow of the current date of the dayTask which is being displayed in the main)
        
        We can achieve the date of the tomorrow by using command:
            datetime.date.today() + datetime.timedelta(days=1)
        Then we create dayTask object of tomorrow:
            DayTask(datetime.date.today() + datetime.timedelta(days=1))
        Finally we use method add_days() of class AllTask to see if the dayTask of tomorrow existed or not:
            - if yes then use that dayTask object
            - if no then create new dayTask object of tomorrow and add to the list of dayTask

        See the documentation of AllTask.
        """
        tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow_day = tomorrow_date.day
        tomorrow_month = tomorrow_date.month
        tomorrow_year = tomorrow_date.year

        next_day_dayTask = self.allTask.add_days(DayTask(Date(tomorrow_year, tomorrow_month, tomorrow_day)))

        self.next_day = GUI(next_day_dayTask)


    def choose_day_btn(self):
        """
        This method creates a pop up window that allow users to choose the day they want to open the app
        """
        self.choose_day_setting = ChooseDaySettingGUI()

        self.choose_day_setting.accepted.connect(self.choose_day)
        self.choose_day_setting.show()


    def choose_day(self, values):
        """
        This method creates a new windows that show the data of the chosen day from user

        See documentation of AllTask, ChooseDaySettingGUI
        """
        chosen_day = int(values["day"])
        chosen_month = int(values["month"])
        chosen_year = int(values["year"])

        choose_day_dayTask = self.allTask.add_days(DayTask(Date(chosen_year, chosen_month, chosen_day)))

        self.choose_day_GUI = GUI(choose_day_dayTask) 


    def closeEvent(self, event):
        """
        This method confirms if the user wants to quit with save or quite without save or not quit
        """
        reply = QMessageBox()
        reply.setIcon(QMessageBox.Question)
        reply.setWindowTitle("Confirm quit")
        reply.setText("Save the time management data?")
        reply.setStandardButtons(QMessageBox.Save | 
                                QMessageBox.Discard | 
                                QMessageBox.Cancel)
        reply.setDefaultButton(QMessageBox.Save)

        discard_btn = reply.button(QMessageBox.Discard)
        discard_btn.setText("Don't Save")
        action = reply.exec()

        if action == QMessageBox.Save:
            self.dayTask.export_data()
            self.dayTask.get_allTask().export_file()
            event.accept()
        elif action == QMessageBox.Cancel:
            event.ignore()
        else:
            event.accept()


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

        The method also checks for the QLabel that are not mapped to some activities, and then will set the name of that QLabel to the original names.

        So to understand this method, read the small comments below to see how the method is divided into 2 parts:
            - first part is for showing the name + timer for the QLabel widgets that are mapped to the activities
            - second part is for renaming the QLabel widgets that are not mapped to any activities
        """

        """
        - format: this is the format for the set_time_format() method of class Activity.
            The value is set to the self.time_format of the class. In this way, when there are changes with the TimeConversion dropdown list, only the self.time_format is changed, and everything is updated. The default time expression format is 1.

        See method change_time_expression()
        """

        # FIRST PART: Displaying name + timer for QLabel that are mapped to activity
        format = self.time_format

        activity_widget_dict = self.activity_widget_dict()

        for key, value in activity_widget_dict.items():
            value[0].setText(key.get_name())
            value[1].setText(key.set_time_format(format))

        # SECOND PART: Reset the text display for QLabel that aren't mapped to activity
        default_activity_label_list = list(self.index_widget_dict().values())
        actual_activity_label_list = list(activity_widget_dict.values())

        for label in default_activity_label_list:
            if label not in actual_activity_label_list:
                label[0].setText("Untitled")
                label[1].setText("00:00:00")

    
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

    
    def update_pomodoro(self):
        """
        This method updates the timer in Pomodoro along with the app, and Pomodoro will send notification if it counts to the working time or the restting time
        """
        if self.pomodoro_reminder != None:
            self.pomodoro_reminder.updateAll()


    def updateAll(self):
        """
        This method combines different updates of the backend info vs GUI widget display, and it makes all these updates at once
        """
        self.update_activity_info()
        self.update_btn_functionality()
        self.update_pomodoro()
        


