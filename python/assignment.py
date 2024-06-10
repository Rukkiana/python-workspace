import os

# Define the Employee class
# class Employee:
#     def __init__(self, emp_id, name, age, department):
#         self.emp_id = emp_id
#         self.name = name
#         self.age = age
#         self.department = department

#     def __str__(self):
#         return f'{self.emp_id}, {self.name}, {self.age}, {self.department}'

# # Define the EMS class
# class EmployeeManagementSystem:
#     def __init__(self, filename='employees.txt'):
#         self.filename = filename

#     def add_employee(self, employee):
#         with open(self.filename, 'a') as file:
#             file.write(str(employee) + '\n' )

#     def view_employees(self):
#         if not os.path.exists(self.filename):
#             print("No employees found.")
#             return

#         with open(self.filename, 'r') as file:
#             employees = file.readlines()
#             if not employees:
#                 print("No employees found.")
#             else:
#                 for emp in employees:
#                     print(emp.strip())

#     def update_employee(self, emp_id, updated_employee):
#         if not os.path.exists(self.filename):
#             print(f"Employee with ID {emp_id} not found.")
#             return

#         employees = []
#         updated = False

#         with open(self.filename, 'r') as file:
#             employees = file.readlines()

#         with open(self.filename, 'w') as file:
#             for emp in employees:
#                 emp_data = emp.strip().split(', ')
#                 if emp_data[0] == emp_id:
#                     file.write(str(updated_employee) + '\n')
#                     updated = True
#                 else:
#                     file.write(emp + '\n')

#         if not updated:
#             print(f"Employee with ID {emp_id} not found.")

#     def delete_employee(self, emp_id):
#         if not os.path.exists(self.filename):
#             print(f"Employee with ID {emp_id} not found.")
#             return

#         employees = []
#         deleted = False

#         with open(self.filename, 'r') as file:
#             employees = file.readlines()

#         with open(self.filename, 'w') as file:
#             for emp in employees:
#                 emp_data = emp.strip().split(', ')
#                 if emp_data[0] == emp_id:
#                     deleted = True
#                 else:
#                     file.write(emp + '\n')

#         if not deleted:
#             print(f"Employee with ID {emp_id} not found.")

# # Command Line Interface
# def main():
#     ems = EmployeeManagementSystem()
    
#     while True:
#         print("\nEmployee Management System")
#         print("1. Add Employee")
#         print("2. View Employees")
#         print("3. Update Employee")
#         print("4. Delete Employee")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             emp_id = input("Enter Employee ID: ")
#             name = input("Enter Employee Name: ")
#             age = input("Enter Employee Age: ")
#             department = input("Enter Employee Department: ")
#             employee = Employee(emp_id, name, age, department)
#             ems.add_employee(employee)
#             print("Employee added successfully.")
#         elif choice == '2':
#             print("\nList of Employees:")
#             ems.view_employees()
#         elif choice == '3':
#             emp_id = input("Enter Employee ID to update: ")
#             name = input("Enter new Employee Name: ")
#             age = input("Enter new Employee Age: ")
#             department = input("Enter new Employee Department: ")
#             updated_employee = Employee(emp_id, name, age, department)
#             ems.update_employee(emp_id, updated_employee)
#             print("Employee updated successfully.")
#         elif choice == '4':
#             emp_id = input("Enter Employee ID to delete: ")
#             ems.delete_employee(emp_id)
#             print("Employee deleted successfully.")
#         elif choice == '5':
#             print("Exiting the system.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == '__main__':
#     main()


# BANKING SYSTEM
class Account:

    def __init__(self,account_name, account_number,account_type,balance=0.0):
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
    
    


    #deposit function that add to the balance
    """ def deposit(self,amount):
        self.amount = amount
        #check the amount is greater than 0
        if amount > 0:
            # add the amount to the balance
            self.balance +=amount
        else:
            print('amount must be greater than zero')
            # withdrawal function that subtract from the balance
    def withdraw(self,amount):
        self.amount = amount
        #check if the amount is greater than 0
        if amount > 0:
            #check if balance is greater than amount
            if self.balance >= amount:
                # subtract amount from balance
                self.balance -= amount
            else:
                print('insufficient amount balance')
        else:
            print('amount must be greater than 0')

        #transfer function that withdraw from another account
    def transfer(self,deposit_acct,amount):
        # check if account exist
        if self and deposit_acct:
        # if self.deposit:can i replace this with  the top if statement
            #check balance in withdrawal account is greater than amount specified
            if self.withdraw >= amount:
            #withdraw amount from withdrawer account
                self.withdraw(amount)
            # deposit amount to deposit account
                deposit_acct.deposit(amount)
            else:
                print('insufficient account balance')
        else:
            print('account do not exist')
    def __str__(self):
        return(f'{self.account_name} with account number:{self.account_number} {self.account_type} has a balance of {self.balance}') 

# TESTING OF CLASS ACCOUNT
account1 =Account('rukayya',1120338182,'savings',2500)
print(account1)
account1.deposit(500)
print(account1)
account1.withdraw(3500)
print(account1) """


# employee assignment 2
# class Employee:
#     def __init__(self, name,employee_id,age,department):
#         self.name = name
#         self.employee_id = employee_id
#         self.age = age
#         self.department = department
#     def __str__(self):
#         return f'Employee ({self.name},{self.employee_id},{self.age},{self.department})'
#     class EmployeeManagementSystem:
#         def __init__(self):
#             self.employees = []
#         def create_employee(self,name,employee_id,age,department):
#             new_employee = Employee(name,employee_id,age,department)
#             self.employees.append(new_employee)
#             print (f'Employee {employee_id} created successfully')



