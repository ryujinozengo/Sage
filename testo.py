import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(100, 100, 100, 50)
        self.button.clicked.connect(self.stop_loop)

    def stop_loop(self):
        self.clicked = True # Set a flag to indicate that the button has been clicked

    def run(self):
        self.clicked = False # Initialize the flag
        while not self.clicked: # Repeat the code block until the button is clicked
            # Your code block goes here
            print("Code block running...")
            QApplication.processEvents() # Process GUI events to keep the GUI responsive

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.run()
    sys.exit(app.exec())
