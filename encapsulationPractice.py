class Employee:

  def __init__(self, name, salary):
    self.name = name  # Public attribute
    self.__salary = salary  # Private attribute (double underscore)

  # Getter method to read the private salary
  def get_salary(self):
    return self.__salary

  # Setter method to update the private salary with validation
  def set_salary(self, amount):
    if amount > 0:
      self.__salary = amount
    else:
      print("Salary must be positive.")


# Create an object
emp = Employee("Alice", 50000)

# Access public attribute
print(emp.name)  # Output: Alice

# Access private attribute via getter method
print(emp.get_salary())  # Output: 50000

# Modify private attribute via setter method
emp.set_salary(55000)
print(emp.get_salary())  # Output: 55000
