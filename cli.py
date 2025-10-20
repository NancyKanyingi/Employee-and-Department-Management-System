from models import Department, Employee
from database import create_tables

def main():
    create_tables()
    print("Welcome to the Employee & Department Management System!")
    print("Type 'help' to see available commands.\n")

    while True:
        command = input("> ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        elif command == "help":
            print("""
Available commands:
  add department [name]
  list departments
  add employee [name] [salary] [department_id]
  list employees
  update salary [employee_id] [new_salary]
  assign department [employee_id] [department_id]
  exit
""")

        elif command.startswith("add department"):
            name = command.replace("add department", "").strip()
            if name:
                Department(name).save()
                print(f"Department '{name}' added.")
            else:
                print("Please provide a department name.")

        elif command == "list departments":
            for d in Department.all():
                print(f"{d[0]} - {d[1]}")

        elif command.startswith("add employee"):
            try:
                parts = command.split()
                name = parts[2]
                salary = float(parts[3])
                dept_id = int(parts[4]) if len(parts) > 4 else None
                Employee(name, salary, dept_id).save()
                print(f"Employee '{name}' added.")
            except Exception:
                print("Usage: add employee [name] [salary] [department_id]")

        elif command == "list employees":
            for e in Employee.all():
                print(f"{e[0]} | {e[1]} | ${e[2]} | {e[3] or 'Unassigned'}")

        elif command.startswith("update salary"):
            parts = command.split()
            try:
                emp_id = int(parts[2])
                new_salary = float(parts[3])
                Employee.update_salary(emp_id, new_salary)
                print("Salary updated successfully.")
            except Exception:
                print("Usage: update salary [employee_id] [new_salary]")

        elif command.startswith("assign department"):
            parts = command.split()
            try:
                emp_id = int(parts[2])
                dept_id = int(parts[3])
                Employee.assign_department(emp_id, dept_id)
                print("Department assigned successfully.")
            except Exception:
                print("Usage: assign department [employee_id] [department_id]")

        else:
            print("Unknown command. Type 'help' to see options.")


if __name__ == "__main__":
    main()
