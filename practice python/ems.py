# Employee database
employees = []
next_id = 1

# Function to create a new employee record
def create_employee(name, age, department, position):
    global next_id
    employee = {
        'id': next_id,  # Use an integer counter for unique IDs
        'name': name,
        'age': age,
        'department': department,
        'position': position
    }
    employees.append(employee)
    next_id += 1
    print(f"Employee {name} added successfully.\n")

# Function to read all employee records
def read_employees():
    if not employees:
        print("No employees found.\n")
    else:
        for emp in employees:
            print(f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}, Position: {emp['position']}")
        print()

# Function to update an existing employee record by ID
def update_employee(emp_id, name=None, age=None, department=None, position=None):
    for emp in employees:
        if emp['id'] == emp_id:
            if name:
                emp['name'] = name
            if age:
                emp['age'] = age
            if department:
                emp['department'] = department
            if position:
                emp['position'] = position
            print(f"Employee {emp_id} updated successfully.\n")
            return
    print(f"Employee with ID {emp_id} not found.\n")

# Function to delete an employee record by ID
def delete_employee(emp_id):
    global employees
    employees = [emp for emp in employees if emp['id'] != emp_id]
    print(f"Employee {emp_id} deleted successfully.\n")

# Command-line interface
def main():
    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            department = input("Enter department: ")
            position = input("Enter position: ")
            create_employee(name, age, department, position)
        elif choice == '2':
            read_employees()
        elif choice == '3':
            emp_id = int(input("Enter employee ID to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            department = input("Enter new department (leave blank to keep current): ")
            position = input("Enter new position (leave blank to keep current): ")
            update_employee(emp_id, name, age, department, position)
        elif choice == '4':
            emp_id = int(input("Enter employee ID to delete: "))
            delete_employee(emp_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
