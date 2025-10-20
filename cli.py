# craeting a CLI
from models import Department, Employee


def main_menu():
    while True:
        print("\n=== Employee & Department Management System ===")
        print("1. Add Department")
        print("2. Add Employee")
        print("3. List Departments")
        print("4. List Employees")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter department name: ")
            dept = Department(name)
            dept.save()

        elif choice == "2":
            name = input("Enter employee name: ")
            salary = int(input("Enter employee salary: "))
            department_id = int(input("Enter department ID: "))
            emp = Employee(name, salary, department_id)
            emp.save()

        elif choice == "3":
            Department.list_all()

        elif choice == "4":
            Employee.list_all()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
