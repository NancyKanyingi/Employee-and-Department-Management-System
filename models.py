from database import get_connection

class Department:
    def __init__(self, name):
        self.name = name

    def save(self):
        """
        Inserts a new department into the database.
        If a department with the same name already exists,
        it does nothing 

        """
        conn = get_connection()
        cur = conn.cursor()
        