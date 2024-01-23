"""
1. Create a class Employee and then do the following
    • Create a data member to count the number of Employees
    • Create a constructor to initialize name, family, salary, department
    • Create a function to average salary
    • Create a Fulltime Employee class and it should inherit the properties of Employee class
    • Create the instances of Fulltime Employee class and Employee class and call their member functions.
"""


class Employee:
    """
    Employee class
    """
    employee_count = 0

    def __init__(self, name, family, salary, department):
        """
        Initiates Employee object

        :param name: The name of the Employee
        :param family: The family of the Employee
        :param salary: The salary of the Employee
        :param department: The department of the Employee
        """
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        """
        The employee count

        :return: The count of employees
        """
        return Employee.employee_count

    @staticmethod
    def average_salary(employees):
        """
        Computes the average salary for the list of employees provided

        :param employees: List of employees
        :return: average salary
        """
        salary = 0
        for employee in employees:
            salary += employee.salary
        return salary / len(employees)

    def __str__(self):
        return "Employee: [name: {}, family: {}, salary: {}, department: {}]".format(self.name,
                                                                                     self.family,
                                                                                     self.salary,
                                                                                     self.department)


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        """
        Initiates FullTimeEmployee object

        :param name: The name of the FullTimeEmployee
        :param family: The family of the FullTimeEmployee
        :param salary: The salary of the FullTimeEmployee
        :param department: The department of the FullTimeEmployee
        """
        super().__init__(name, family, salary, department)

    def __str__(self):
        """
        FullTimeEmployee details

        :return: FullTimeEmployee details as string
        """
        return "FullTimeEmployee: [name: {}, family: {}, salary: {}, department: {}]".format(self.name,
                                                                                             self.family,
                                                                                             self.salary,
                                                                                             self.department)


def main():
    # Create instance of Employee
    employee_1 = Employee("Employee 1", "Family 1", 100000, "CS")
    # Create instance of FullTimeEmployee
    employee_2 = FullTimeEmployee("Employee 2", "Family 2", 120000, "IT")

    # Call member functions
    employees = [employee_1, employee_2]
    # Print Employee
    print(employee_1)
    # Print FullTimeEmployee
    print(employee_2)
    # Get total employees using Employee instance
    print('Total employees (using Employee instance): {}'.format(Employee.get_employee_count()))
    # Get average salary using Employee instance
    print('Average salary (using Employee instance): {}'.format(Employee.average_salary(employees)))
    # Get total employees using FullTimeEmployee instance
    print('Total employees (using FullTimeEmployee instance): {}'.format(FullTimeEmployee.get_employee_count()))
    # Get average salary using FullTimeEmployee instance
    print('Average salary (using FullTimeEmployee instance): {}'.format(FullTimeEmployee.average_salary(employees)))


# call main
if __name__ == '__main__':
    main()


