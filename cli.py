# cli.py
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
            # Add Department
            name = input("Enter department name: ")
            Department(name).save() 
            print(f"Department '{name}' added successfully!")

        elif choice == "2":
            # Add Employee
            name = input("Enter employee name: ")
            salary = input("Enter salary: ")
            department_id = input("Enter department ID (or leave blank for Unassigned): ").strip()
            department_id = int(department_id) if department_id else None
            Employee(name, salary, department_id).save()  
            print(f"Employee '{name}' added successfully!")

        elif choice == "3":
            # List Departments
            print("\n Departments:")
            departments = Department.list_all()
            if departments:
                print("ID | Name")
                print("-------------")
                for d in departments:
                    print(f"{d[0]} | {d[1]}")
            else:
                print("⚠️ No departments found.")

        elif choice == "4":
            # List Employees
            print("\n Employees:")
            employees = Employee.list_all()
            if employees:
                print("ID | Name | Salary | Department")
                print("------------------------------------")
                for e in employees:
                    print(f"{e[0]} | {e[1]} | {e[2]} | {e[3]}")
            else:
                print("No employees found.")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
