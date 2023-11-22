import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter task...")
        layout.addWidget(self.task_input)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        self.setLayout(layout)
        self.show()

    def add_task(self):
        # Logic to add a task to the list
        task_text = self.task_input.text()
        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    sys.exit(app.exec())
