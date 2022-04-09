from ctypes import alignment
import sys
from tracemalloc import stop
from PyQt5.QtWidgets import (
    QWidget, QDesktopWidget, QApplication, QMessageBox, 
    QPushButton, QLabel, QComboBox,
    QGridLayout, QHBoxLayout, QVBoxLayout)
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

        title_layout = QHBoxLayout() # This is the first row in the designed UI, which has 3 columns: the button switch, activity date, button to add new task

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
        # create the widgets
        time_conversion = QPushButton("Time Conversion")
        activity_date = QLabel("Current Activity Date")
        add_task = QPushButton("Add Task")

        # add the widgets to the GUI Layout
        title_layout.addWidget(time_conversion, 1, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        title_layout.addWidget(activity_date, 4, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
        title_layout.addWidget(add_task, 1, alignment=Qt.AlignRight | Qt.AlignVCenter)

    def activity_widget(self, activity_layout):
        """
        This method adds the widgets to the activity section of the GUI
        """
        # create the widgets
        task_1 = QLabel("Task 1")
        task_1_time = QLabel("00:00:00")
        task_2 = QLabel("Task 2")
        task_2_time = QLabel("00:00:00")
        task_3 = QLabel("Task 3")
        task_3_time = QLabel("00:00:00")
        task_4 = QLabel("Task 4")
        task_4_time = QLabel("00:00:00")
        task_5 = QLabel("Task 5")
        task_5_time = QLabel("00:00:00")

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        activity_layout.addWidget(task_1, 0, 0, alignment)
        activity_layout.addWidget(task_1_time, 0, 1, alignment)
        activity_layout.addWidget(task_2, 1, 0, alignment)
        activity_layout.addWidget(task_2_time, 1, 1, alignment)
        activity_layout.addWidget(task_3, 2, 0, alignment)
        activity_layout.addWidget(task_3_time, 2, 1, alignment)
        activity_layout.addWidget(task_4, 3, 0, alignment)
        activity_layout.addWidget(task_4_time, 3, 1, alignment)
        activity_layout.addWidget(task_5, 4, 0, alignment)
        activity_layout.addWidget(task_5_time, 4, 1, alignment)

    def mainbutton_widget(self, mainbutton_layout):
        """
        This method adds the widgets to the main button section of the GUI
        """
        # create the widgets
        start_btn = QPushButton("Start")
        stop_btn = QPushButton("Stop")
        reset_btn = QPushButton("Reset")
        pomodoro_btn = QPushButton("Pomodoro")
        stats_btn = QPushButton("Statistics")

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        mainbutton_layout.addWidget(start_btn, alignment)
        mainbutton_layout.addWidget(stop_btn, alignment)
        mainbutton_layout.addWidget(reset_btn, alignment)
        mainbutton_layout.addWidget(pomodoro_btn, alignment)
        mainbutton_layout.addWidget(stats_btn, alignment)

    def otherbutton_widget(self, otherbutton_layout):
        """
        This method adds the widgets to the other button section of the GUI
        """
        # create the widgets
        show_day_btn = QPushButton("Choose Day")
        next_day_btn = QPushButton("Next Day")
        export_btn = QPushButton("Export")
        import_btn = QPushButton("Import")
        help_btn = QPushButton("Need help?")

        # set the alignment to the center vertically and horizontally of the cell
        alignment = Qt.AlignHCenter | Qt.AlignVCenter

        # add the widgets to the GUI Layout
        otherbutton_layout.addWidget(show_day_btn, alignment)
        otherbutton_layout.addWidget(next_day_btn, alignment)
        otherbutton_layout.addWidget(export_btn, alignment)
        otherbutton_layout.addWidget(import_btn, alignment)
        otherbutton_layout.addWidget(help_btn, alignment)


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


def main():

    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()