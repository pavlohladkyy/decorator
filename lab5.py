from abc import ABC, abstractmethod

# Abstract base class for employee salary
class EmployeeSalary(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

# Concrete implementation of an employee
class Employee(EmployeeSalary):
    def __init__(self, name, emp_id, qualification, base_salary):
        # Initialize employee attributes
        self.name = name
        self.emp_id = emp_id
        self.qualification = qualification
        self.base_salary = base_salary
        self.worked_hours = 0

    # Set the number of worked hours
    def set_worked_hours(self, hours):
        self.worked_hours = hours

    # Get the salary multiplier based on qualification
    def get_salary_multiplier(self):
        return {
            "Trainee": 1.0,
            "Junior": 1.2,
            "Middle": 1.5,
            "Senior": 2.0
        }.get(self.qualification, 1.0)

    # Calculate the total salary
    def calculate_salary(self):
        return self.base_salary * self.get_salary_multiplier()

    # Display employee information
    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Qualification: {self.qualification}, "
              f"Base Salary: ${self.base_salary:.2f}, Worked Hours: {self.worked_hours}, "
              f"Total Salary: ${self.calculate_salary():.2f}")

    # Static method to create an employee instance from user input
    @staticmethod
    def create_employee():
        name = input("Full Name: ")
        emp_id = int(input("ID: "))
        qualification = input("Qualification (Trainee, Junior, Middle, Senior): ")
        while qualification not in {"Trainee", "Junior", "Middle", "Senior"}:
            qualification = input("Invalid qualification. Enter again: ")
        base_salary = float(input("Base Salary: "))
        worked_hours = int(input("Worked Hours: "))
        
        # Create and return an Employee instance
        employee = Employee(name, emp_id, qualification, base_salary)
        employee.set_worked_hours(worked_hours)
        return employee

# Decorator class to add bonuses to employee salary
class BonusDecorator(EmployeeSalary):
    def __init__(self, employee_salary, bonus):
        # Initialize with the base employee salary and bonus
        self.employee_salary = employee_salary
        self.bonus = bonus

    # Calculate salary including bonus
    def calculate_salary(self):
        return self.employee_salary.calculate_salary() + self.bonus

    # Display employee information including bonus
    def display_info(self):
        self.employee_salary.display_info()
        print(f"Bonus: ${self.bonus:.2f}")

# Class to manage payroll system
class PayrollSystem:
    def __init__(self):
        # Initialize an empty list of employees
        self.employees = []

    # Add an employee to the payroll system
    def add_employee(self, employee):
        self.employees.append(employee)

    # Calculate bonuses for employees who worked more than 40 hours
    def calculate_bonuses(self):
        for i, employee in enumerate(self.employees):
            if isinstance(employee, Employee) and employee.worked_hours > 40:
                bonus = employee.base_salary * 0.1 * (employee.worked_hours - 40)
                self.employees[i] = BonusDecorator(employee, bonus)

    # Display all employees in the payroll system
    def display_employees(self):
        print("\nEmployee List:")
        for employee in self.employees:
            employee.display_info()

    # Display the top N employees based on worked hours
    def display_top_employees(self, top_n):
        sorted_employees = sorted(
            self.employees, key=lambda emp: emp.worked_hours if isinstance(emp, Employee) else 0, reverse=True
        )
        print(f"\nTop {top_n} Employees by Worked Hours:")
        for employee in sorted_employees[:top_n]:
            employee.display_info()

    # Input employee details from the user
    def input_employees(self, number):
        for _ in range(number):
            print("Enter details for employee:")
            self.add_employee(Employee.create_employee())

# Main program execution
if __name__ == "__main__":
    payroll_system = PayrollSystem()
    num_employees = int(input("Enter number of employees: "))
    payroll_system.input_employees(num_employees)
    payroll_system.calculate_bonuses()
    payroll_system.display_employees()
    top_n = int(input("Enter number of top employees to display: "))
    payroll_system.display_top_employees(top_n)
