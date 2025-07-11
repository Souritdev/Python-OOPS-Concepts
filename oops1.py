###Defining the class###
class Employee:
  ###now its time for the magic method ---> constructor to come###

  def __init__(self):


    print("Data Attributes are being defined properly")
    self.id = "1234DDGFXM"
    self.salary = 45000
    self.designation = "AIE"
    print("Data Attributes have been defined properly")



  def travel(self, destination):
    print("The methods have been properly set up by us")
    print(f"Employee need to travel all along to {destination} tomorrow.")



### Create an object / instance of the class Employee
Sourit = Employee()


# # print(Sourit.id)
Sourit.travel("Hyderabad")