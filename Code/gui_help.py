import sys, PyQt5
from PyQt5.QtWidgets import (QWidget, QScrollArea, QDesktopWidget,
                            QVBoxLayout, QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class HelpGUI(QScrollArea):
    """
    The class HelpGUI creates a windows with information that helps the users using app.
    
    This class is called whenever the button Need help? is clicked.
    
    See the documentation of class GUI.
    """
    def __init__(self):
        """
        This method initializes the class.
        It calls the necessary methods of the class below to creates the initial GUI of the program
        """
        super().__init__()
        self.setStyleSheet("background-color: rgb(250,250,250);")

        self.init_windows()
        self.init_UI()

    
    def init_UI(self):
        """
        This method creates a layout for the pop up window

        self.scroll = QScrollArea() # Scroll area which contains everything inside
        self.widget = QWidget() # Widget that contains the collection of Vertical Box
        self.window_layout = QVBoxLayout() # the window will arrange the widgets inside it vertically

        self.add_widgets() # add the widgets to the layout. See method add_widgets() below

        self.widget.setLayout(self.window_layout)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)
        """
        self.widget = QWidget() # Widget that contains the collection of Vertical Box
        self.window_layout = QVBoxLayout() # the window will arrange the widgets inside it vertically

        self.add_widgets() # add the widgets to the layout. See method add_widgets() below

        self.widget.setLayout(self.window_layout)

        #Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(self.widget)


    def add_widgets(self):
        """
        This method creates and adds the widgets to the layout of the pop up window

        Intended structure of the help window
            - Heading INSTRUCTION
                - First row: Time Conversion button + Date title + Add Activity button
                - Second rows: The activity name + timer
                - Third row: main buttons
                - Fourth row: other buttons for extra functionality
            - Source code:
                - Author + Github link for more detailed description
        """

        # create the widgets
        self.window_heading = QLabel()
        self.first_part = QWidget()
        self.second_part = QWidget()
        self.third_part = QWidget()
        self.fourth_part = QWidget()
        self.source_code = QLabel()

        # add the content to the widgets. See the methods called in this part below
        self.window_heading_widget()
        self.first_part_widget()
        self.second_part_widget()
        self.third_part_widget()
        self.fourth_part_widget()

        # add the widgets to the layout
        self.window_layout.addWidget(self.window_heading, stretch=0)
        self.window_layout.addWidget(self.first_part, stretch=3)
        self.window_layout.addWidget(self.second_part, stretch=3)
        self.window_layout.addWidget(self.third_part, stretch=3)
        self.window_layout.addWidget(self.fourth_part, stretch=3)
        self.window_layout.addWidget(self.source_code, stretch=1)


    def window_heading_widget(self):
        """
        This method adds the content for QLabel self.window_heading
        """
        self.window_heading.setText("<h1>Instruction</h1>")
        self.window_heading.setAlignment(Qt.AlignCenter)


    def first_part_widget(self):
        """
        This method adds the content for QWidget self.first_part
        """
        vertical_box = QVBoxLayout() # create the layout for this widget

        # create the widgets for first part
        heading = QLabel("<h2>App Title & First Controls</h2><br>\
                        At the top of the app graphical interface, you will see\
                        something like this:") 

        screenshot_label = QLabel()
        screenshot_pixmap = QPixmap("Code/screenshots/first_part.png")
        screenshot_label.setPixmap(screenshot_pixmap)

        body = QLabel("<li>- In the middle is the date of the activitites that you're putting a timer on.</li><li>- On the left is the <code style='background-color:#d3d3d3'>Time Conversion</code> button. With this button, you can choose the time expression you like. Currently, there are 4 types of expression: <code style='background-color:#d3d3d3'>HH:MM:SS</code>, <code style='background-color:#d3d3d3'>MM:SS</code>, <code style='background-color:#d3d3d3'>Finnish ECTS</code> (1 ECT = 27 hours), <code style='background-color:#d3d3d3'>Standard Expression</code>.</li><li>- On the right is the <code style='background-color:#d3d3d3'>Add Activity</code> button. You can add new activity you wnat to track time using it. The maximum number of activities can be tracked is 5.</li>")
        body.setWordWrap(True)

        # add the widgets to the layout
        vertical_box.addWidget(heading, stretch=0)
        vertical_box.addWidget(screenshot_label, alignment=Qt.AlignCenter)
        vertical_box.addWidget(body)
        
        # add the layout to the widget self.first_part
        self.first_part.setLayout(vertical_box)

    
    def second_part_widget(self):
        """
        This method adds the content for QWidget self.second_part
        """
        vertical_box = QVBoxLayout() # create the layout for this widget

        # create the widgets for second part
        heading = QLabel("<h2>Activities Information</h2><br>\
                        Below these buttons and title, you will see\
                        something like this:") 

        screenshot_label = QLabel()
        screenshot_pixmap = QPixmap("Code/screenshots/second_part.png")
        screenshot_label.setPixmap(screenshot_pixmap)

        body = QLabel("These are the display of your activities and their timer. The Untitled activities are the activities that are not added yet.")
        body.setWordWrap(True)

        # add the widgets to the layout
        vertical_box.addWidget(heading, stretch=1)
        vertical_box.addWidget(screenshot_label, alignment=Qt.AlignCenter)
        vertical_box.addWidget(body)
        
        # add the layout to the widget self.second_part
        self.second_part.setLayout(vertical_box)


    def third_part_widget(self):
        """
        This method adds the content for QWidget self.third_part
        """
        vertical_box = QVBoxLayout() # create the layout for this widget

        # create the widgets for third part
        heading = QLabel("<h2 style='border-bottom: 2px solid #7a0000;'>Main Control Button</h2>\
                        The main control buttons row looks like this:") 

        screenshot_label = QLabel()
        screenshot_pixmap = QPixmap("Code/screenshots/third_part.png")
        screenshot_label.setPixmap(screenshot_pixmap)

        body = QLabel("There are 5 buttons that the users will mainly use:\
            <ul>\
                <li>The first button is <code style='background-color:#d3d3d3'>Start</code> button. Users can start (resume) the timer of the activities they want.</li>\
                <li>Button <code style='background-color:#d3d3d3'>Stop</code> stops (pauses) the timer of the activity. Users can choose which activity from the button.</li>\
                <li>Button <code style='background-color:#d3d3d3'>Reset</code> stops and resets the timer of the activity to 0. Users can choose which activity from the button.</li>\
                <li>Button <code style='background-color:#d3d3d3'>Restart</code> resets the timer of the activity to 0 and automatically starts the timer. Users can choose which activity from the button.</li>\
                <li>Button <code style='background-color:#d3d3d3'>Statistics</code> shows the statistics of the time management data. The statistics will be in numerical format and also be visualized with graphs and charts.</li>\
            </ul>")
        body.setWordWrap(True)

        # add the widgets to the layout
        vertical_box.addWidget(heading, stretch=0)
        vertical_box.addWidget(screenshot_label, alignment=Qt.AlignCenter)
        vertical_box.addWidget(body)
        
        # add the layout to the widget self.third_part
        self.third_part.setLayout(vertical_box)

    
    def fourth_part_widget(self):
        """
        This method adds the content for QWidget self.fourth_part
        """
        vertical_box = QVBoxLayout() # create the layout for this widget

        # create the widgets for fourth part
        heading = QLabel("<h2 style='border-bottom: 2px solid #7a0000;'>Other Functionality</h2>\
                        The program also has other functions:") 

        screenshot_label = QLabel()
        screenshot_pixmap = QPixmap("Code/screenshots/fourth_part.png")
        screenshot_label.setPixmap(screenshot_pixmap)

        body = QLabel("There are 5 other buttons for extra functionality:\
            <ul>\
                <li>The first button is <code style='background-color:#d3d3d3'>Edit</code> button. Users can change the name of the activities they want.</li>\
                <li>Button <code style='background-color:#d3d3d3'>Delete</code> allows the users to delete the activities they want.</li>\
                <li>Button <code style='background-color:#d3d3d3'>Pomodoro</code> allows the users to change the setting of Pomodoro reminder and turns on the reminder.</li>\
                <li>Button <code style='background-color:#d3d3d3'>More</code> shows more functionality (Export, Import, Go to next day, Choose the day).</li>\
                <li>Button <code style='background-color:#d3d3d3'>Need Help?</code> shows a help information for the users.</li>\
            </ul>")
        body.setWordWrap(True)

        # add the widgets to the layout
        vertical_box.addWidget(heading, stretch=0)
        vertical_box.addWidget(screenshot_label, alignment=Qt.AlignCenter)
        vertical_box.addWidget(body)
        
        # add the layout to the widget self.fourth_part
        self.fourth_part.setLayout(vertical_box)


    def init_windows(self):
        """
        This method set the windows of the app
        and put it in the center of the screen
        """
        self.resize(500, 500)
        self.center()

        self.setWindowTitle('Help Information')
        #self.show()

    
    def center(self):
        """
        This method centers the window on the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    help = HelpGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
