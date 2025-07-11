### Assignment submitted by me ---> a question given by the chatGpt###

### Defining the class for this program as given

class Student:

### This is the magic method we call by the name "Constructors" 

  def __init__(self):
    
    self.name = "Sourit Nandy"
    self.roll = 34600120001
    self.branch = "CSE"
    self.cgpa = 8.5


### This is the list of methods / functions we are given
  def introduce(self):
    print(f"I am {self.name} from {self.branch} and my roll number is {self.roll}")

  def apply_for_internship(self, company_name):
    print(f"{self.name} with CGPA {self.cgpa} wants to apply for internship at {company_name}")



### Here Comes the objects section we are calling now###
ME = Student()
# print(ME.cgpa)
ME.introduce()
ME.apply_for_internship("Google")