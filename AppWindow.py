from PyQt5 import uic
from PyQt5.QtGui import QWindow
from Employees import EmployeesDialog
from ProductLines import ProductLinesDialog

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
        
        # Employees dialog.
        self._employees_dialog = EmployeesDialog()
        self.ui.employees_button.clicked.connect(self._show_employees_dialog)
        
        # Product Lines dialog.
        self._productLines_dialog = ProductLinesDialog()
        self.ui.productLines_button.clicked.connect(self._show_productLines_dialog)

    def _show_employees_dialog(self):
        """
        Show the eployees dialog.
        """
        self._employees_dialog.show_dialog()

    def _show_productLines_dialog(self):
        """
        Show the product lines dialog.
        """
        self._productLines_dialog.show_dialog()
