class Employee:
  
  def __init__(self,rcv_emp_id,rcv_emp_salary,rcv_mgr_id) -> None:
    # instance variables 
    self.emp_id = rcv_emp_id
    self.emp_salary= rcv_emp_salary
    self.mgr_id = rcv_mgr_id

 # class variable 
  department_name = "Tata"
  department_name = "Wipro"
  department_name = "cisco"
  # instance methods
  def get_emp_salary(self):
      return self.emp_salary
  
  def set_emp_salary(self,rcv_salary):
   self.emp_salary = rcv_salary

  # class method 
  @classmethod
  def get_department_name(cls) :
    return cls.department_name
  
  # static method
  @staticmethod
  def field_expertise():
      print("just displays some expertise for all my employees")

def main():
    # 1) create an object employee(100,1000,1)  
    # employee_1 = input("Enter emp_id").emp_id
    # employee_1 = input("Enter emp_salary").get_emp_salary
    # employee_1 = input("Enter emp_id").mgr_id
    employee_2 = Employee(101,1001,2)
    # 2) do the following for the created object
    #  direct access using .notation
    print("employee_1.empid:",employee_1.emp_id)
    print("employee_1.get_emp_salary():",employee_1.get_emp_salary())
    print("employee_1.mgr_id:",employee_1.mgr_id)
    print("employee_2.empid:",employee_2.emp_id)
    print("employee_2.get_emp_salary():",employee_2.get_emp_salary())
    print("employee_2.mgr_id:",employee_2.mgr_id)
    # 3) print the department name 
    print(Employee.get_department_name())
    
    # 4) display the expertise for the employees 
    Employee.field_expertise()
    # 5) Deleting Attributes and Objects