from database import connect_db

class Department:
    @staticmethod
    def list_all():
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


class Employee:   
    @staticmethod
    def list_all():
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT e.id, e.name, e.salary,
                   COALESCE(d.name, 'Unassigned') AS department
            FROM employees e
            LEFT JOIN departments d ON e.department_id = d.id;
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
