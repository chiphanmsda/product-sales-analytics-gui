from PyQt5 import uic
from PyQt5.QtGui import QWindow
from EmployeesDialog import EmployeesDialog
from TeacherDialog import TeacherDialog

class AppWindow(QWindow):
    """
    The main application window.
    """
    
    def __init__(self):
        """
        Load the UI and initialize its components.
        """
        super().__init__()
        
        self.ui = uic.loadUi('demo_app.ui')
        self.ui.show();
        
        # Student dialog.
        self._employees_dialog = EmployeesDialog()
        self.ui.student_button.clicked.connect(self._show_employees_dialog)
        
        # Teacher dialog.
        self._teacher_dialog = TeacherDialog()
        self.ui.teacher_button.clicked.connect(self._show_teacher_dialog)

    def _show_employees_dialog(self):
        """
        Show the student dialog.
        """
        self._employees_dialog.show_dialog()

    def _show_teacher_dialog(self):
        """
        Show the teacher dialog.
        """
        self._teacher_dialog.show_dialog()
