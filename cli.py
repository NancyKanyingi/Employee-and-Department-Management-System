from models import Department, Employee
from database import connect_db

def main_menu():
    while True:
        print("\n=== Employee & Department Management System ===")
        print("1. Add Department")
        print("2. Add Employee")
        print("3. List Departments")
        print("4. List Employees")
        print("5. Delete Department")
        print("6. Delete Employee")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter department name: ").strip()
            if name:
                Department.add_department(name)
            else:
                print("Department name cannot be empty.")

        elif choice == "2":
            name = input("Enter employee name: ").strip()
            salary = input("Enter employee salary: ").strip()
            department_id = input("Enter department ID (or leave blank): ").strip()
            department_id = int(department_id) if department_id else None

            if name and salary.isdigit():
                Employee.add_employee(name, int(salary), department_id)
            else:
                print("Invalid input. Ensure salary is a number.")

        elif choice == "3":
            Department.list_all()

        elif choice == "4":
            Employee.list_all()

        elif choice == "5":
            dep_id = input("Enter department ID to delete: ").strip()
            if dep_id.isdigit():
                Department.delete_department(int(dep_id))
            else:
                print("Invalid department ID.")

        elif choice == "6":
            emp_id = input("Enter employee ID to delete: ").strip()
            if emp_id.isdigit():
                Employee.delete_employee(int(emp_id))
            else:
                print("Invalid employee ID.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1–7.")


if __name__ == "__main__":
    main_menu()
