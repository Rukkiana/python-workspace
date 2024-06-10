class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}"

    def update_position(self, new_position):
        self.position = new_position

    def update_salary(self, new_salary):
        self.salary = new_salary

        class Company:
            def __init__(self):
                self.employees = []

            def add_employee(self, employee):
                self.employees.append(employee)

            def remove_employee(self, name):
                for employee in self.employees:
                    if employee.name == name:
                        self.employees.remove(employee)
                        return
                print("Employee not found")

            def update_employee(self, name, new_position=None, new_salary=None):
                for employee in self.employees:
                    if employee.name == name:
                        if new_position:
                            employee.update_position(new_position)
                        if new_salary:
                            employee.update_salary(new_salary)
                        return
                print("Employee not found")

            def view_all_employees(self):
                for employee in self.employees:
                    print(employee)

            def find_employee(self, name):
                for employee in self.employees:
                    if employee.name == name:
                        return employee
                print("Employee not found")
                return None
            def main():
                company = Company()

                while True:
                    print("\nChoose an action:")
                    print("1. Add a new employee")
                    print("2. Remove an employee")
                    print("3. Update an employee's details")
                    print("4. View all employees")
                    print("5. Find an employee by name")
                    print("6. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        name = input("Enter employee name: ")
                        age = int(input("Enter employee age: "))
                        position = input("Enter employee position: ")
                        salary = float(input("Enter employee salary: "))
                        employee = Employee(name, age, position, salary)
                        company.add_employee(employee)

                    elif choice == '2':
                        name = input("Enter the name of the employee to remove: ")
                        company.remove_employee(name)

                    elif choice == '3':
                        name = input("Enter the name of the employee to update: ")
                        new_position = input("Enter new position (leave blank to keep current): ")
                        new_salary = input("Enter new salary (leave blank to keep current): ")
                        new_position = new_position if new_position else None
                        new_salary = float(new_salary) if new_salary else None
                        company.update_employee(name, new_position, new_salary)

                    elif choice == '4':
                        company.view_all_employees()

                    elif choice == '5':
                        name = input("Enter the name of the employee to find: ")
                        employee = company.find_employee(name)
                        if employee:
                            print(employee)

                    elif choice == '6':
                        break

                    else:
                        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

       