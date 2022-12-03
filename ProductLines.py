import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QHeaderView
from mydbutils import do_query

class TeacherDialog(QDialog):
    """
    The teacher dialog.
    """
    
    def __init__(self):
        """
        Load the UI and initialize its components.
        """
        super().__init__()
        
        # Load the dialog components.
        self.ui = uic.loadUi('productLines_dialog.ui')

        # Teacher menu and query button event handlers.
        self.ui.teacher_cb.currentIndexChanged.connect(self._initialize_table)
        self.ui.query_button.clicked.connect(self._enter_student_data)
        
        # Initialize the teacher menu and the student table.
        self._initialize_teacher_menu()
        self._initialize_table()
        
    def show_dialog(self):
        """
        Show this dialog.
        """
        self.ui.show()
    
    def _initialize_teacher_menu(self):
        """
        Initialize the teacher menu with teacher names from the database.
        """
        sql = """
            SELECT first, last FROM teacher
            ORDER BY last
            """
        rows, _ = do_query(sql)

        # Set the menu items to the teacher names.
        for row in rows:
            name = row[0] + ' ' + row[1]
            self.ui.teacher_cb.addItem(name, row)     
            
    def _adjust_column_widths(self):
        """
        Adjust the column widths of the student table to fit the contents.
        """
        header = self.ui.student_table.horizontalHeader();
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        
    def _initialize_table(self):
        """
        Clear the table and set the column headers.
        """
        self.ui.student_table.clear()

        col = ['  ID  ', '   First   ', '   Last   ', 'Subject']
        self.ui.student_table.setHorizontalHeaderLabels(col)        
        self._adjust_column_widths()
        
    def _enter_student_data(self):    
        """
        Enter student data from the query into the student table.
        """    
        name = self.ui.teacher_cb.currentData()
        first_name = name[0]
        last_name = name[1]
        
        sql = ( """
            SELECT student.id, student.first, student.last, 
                   class.subject
            FROM student, teacher, class, takes
            WHERE teacher.last = '""" + last_name + "' "
            """
            AND teacher.first = '""" + first_name + "' "
            """
            AND class.teacher_id = teacher.id 
            AND takes.class_code = class.code
            AND takes.student_id = student.id 
            ORDER BY class.subject, student.last
            """ 
              )                
        rows, _ = do_query(sql)
        
        # Set the student data into the table cells.
        row_index = 0
        for row in rows:
            column_index = 0
            
            for data in row:
                item = QTableWidgetItem(str(data))
                self.ui.student_table.setItem(row_index, column_index, item)
                column_index += 1

            row_index += 1
                
        self._adjust_column_widths()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = TeacherDialog()
    form.show_dialog()
    sys.exit(app.exec_())