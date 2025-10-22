from database import connect_db

class Department:
    @staticmethod
    def add_department(name):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO departments (name) VALUES (%s) ON CONFLICT DO NOTHING;", (name,))
        conn.commit()
        conn.close()
        print(f"Department '{name}' added successfully.")

    @staticmethod
    def list_all():
        """Fetch and return all departments."""
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM departments;")
        rows = cur.fetchall()
        conn.close()

        if not rows:
            print("No departments found.")
        else:
            print("ID | Department")
            print("----------------")
            for row in rows:
                print(f"{row[0]} | {row[1]}")

    def delete_department(department_id):
        conn = connect_db()
        cur = conn.cursor()

        # Check if department exists first
        cur.execute("SELECT * FROM departments WHERE id = %s;", (department_id,))
        dept = cur.fetchone()
        if not dept:
            print(f"No department found with ID {department_id}.")
            conn.close()
            return

        # Delete department
        cur.execute("DELETE FROM departments WHERE id = %s;", (department_id,))
        conn.commit()
        conn.close()
        print(f"Department with ID {department_id} deleted successfully.")


class Employee:
    @staticmethod
    def add_employee(name, salary, department_id=None):
        conn = connect_db()
        cur = conn.cursor()

        # Handle blank department_id
        if department_id == "" or department_id is None:
            cur.execute(
                "INSERT INTO employees (name, salary) VALUES (%s, %s)",
                (name, salary)
            )
        else:
            cur.execute(
                "INSERT INTO employees (name, salary, department_id) VALUES (%s, %s, %s)",
                (name, salary, department_id)
            )

        conn.commit()
        conn.close()
        print(f"Employee '{name}' added successfully.")

    @staticmethod
    def list_all():
        """Return all employees with their department names."""
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT e.id, e.name, e.salary,
                COALESCE(d.name, 'Unassigned') AS department
            FROM employees e
            LEFT JOIN departments d ON e.department_id = d.id
        """)
        rows = cur.fetchall()
        conn.close()

        if not rows:
            print("No employees found.")
        else:
            print("ID | Name | Salary | Department")
            print("-----------------------------------")
            for row in rows:
                print(f"{row[0]} | {row[1]} | ${row[2]} | {row[3]}")
    def delete_employee(employee_id):
        conn = connect_db()
        cur = conn.cursor()

        # Check if the employee exists before deleting
        cur.execute("SELECT * FROM employees WHERE id = %s;", (employee_id,))
        emp = cur.fetchone()
        if not emp:
            print(f"No employee found with ID {employee_id}.")
            conn.close()
            return

        # Delete the employee
        cur.execute("DELETE FROM employees WHERE id = %s;", (employee_id,))
        conn.commit()
        conn.close()
        print(f"Employee with ID {employee_id} deleted successfully.")
