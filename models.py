from database import get_connection

# Department Class

class Department:
    def __init__(self, name):
        self.name = name

    def save(self):
        """
        Inserts a new department into the database.
        If a department with the same name already exists,
        it does nothing (thanks to ON CONFLICT DO NOTHING).
        """
        conn = get_connection()
        cur = conn.cursor()

        #  Insert department name (if not already existing)
        cur.execute("""
            INSERT INTO departments (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING;
        """, (self.name,))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def all():
        """Fetch and return all departments."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM departments ORDER BY id;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows


# -------------------------------
# Employee Class
# -------------------------------
class Employee:
    def __init__(self, name, salary, department_id=None):
        self.name = name
        self.salary = salary
        self.department_id = department_id

    def save(self):
        """Insert a new employee into the database."""
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO employees (name, salary, department_id)
            VALUES (%s, %s, %s);
        """, (self.name, self.salary, self.department_id))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def all():
        """Return all employees with their department names."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT e.id, e.name, e.salary, d.name AS department
            FROM employees e
            LEFT JOIN departments d ON e.department_id = d.id
            ORDER BY e.id;
        """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    @staticmethod
    def update_salary(emp_id, new_salary):
        """Update an employee's salary."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE employees SET salary = %s WHERE id = %s;", (new_salary, emp_id))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def assign_department(emp_id, dept_id):
        """Assign an employee to a specific department."""
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE employees SET department_id = %s WHERE id = %s;", (dept_id, emp_id))
        conn.commit()
        cur.close()
        conn.close()
