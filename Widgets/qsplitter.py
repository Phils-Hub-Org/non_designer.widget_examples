from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QTextEdit, QPushButton, QApplication
from PySide6.QtCore import Qt

def add_splitter_to_layout(layout):
    # Create the QSplitter
    splitter = QSplitter(Qt.Vertical)  # You can also use Qt.Vertical for a vertical splitter

    # Create some example widgets to add to the splitter
    text_edit1 = QTextEdit("Left pane")
    text_edit2 = QTextEdit("Right pane")

    # Add widgets to the splitter
    splitter.addWidget(text_edit1)
    splitter.addWidget(text_edit2)

    # Add the splitter to the existing layout
    layout.addWidget(splitter)

# Example usage
if __name__ == "__main__":
    app = QApplication([])

    # Main window
    main_window = QWidget()
    main_layout = QVBoxLayout()  # Could also be QHBoxLayout, etc.

    # Add some widgets to the layout before the splitter
    button = QPushButton("Button Above Splitter")
    main_layout.addWidget(button)

    # Add the splitter to the layout
    add_splitter_to_layout(main_layout)

    # Add more widgets after the splitter if needed
    another_button = QPushButton("Button Below Splitter")
    main_layout.addWidget(another_button)

    # Set the main layout to the main window
    main_window.setLayout(main_layout)
    main_window.show()

    app.exec()
