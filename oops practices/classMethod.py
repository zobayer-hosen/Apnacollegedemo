class Greeks:
  course = "DSA"
  list_of_instance = []

  def __init__(self,name):
    self.name = name
    Greeks.list_of_instance.append(self.name)
    
  #@classmethod 1.cls ke parameter hisabe nai
  #data access or poribotton ar jonno use hoi
  #use is it for alternative constractor

class Student :
  total_students = 0
  def __init__(self,name):
    self.name = name
    Student.total_students +=1

  @classmethod
  def get_total_students(cls):
    return cls.total_students

s1= Student("Alice")
s2= Student("Bob")
print(Student.get_total_students())    

class Greeks:
  course= 'DSA'
  list_of_instance=[]
  def __init__(self,name,age):
    self.name = name
    self.age = age
    Greeks.list_of_instance.append(self)
    
  @classmethod
  def get_course(cls):
    return f"Course:{cls.course}"

  @classmethod
  def get_instance_count(cls):
    return f"Number of instance:{len(cls.list_of_instance)}"
  @staticmethod
  def Welcome_message():
    return "welcome to Greeks for Greeks" 
#Creating instance
g1 = Greeks("Alice",22)
#

# calling class methods
print(Greeks.get_course())
print(Greeks.get_instance_count())
# Calling static method

print(Greeks.Welcome_message())



class Greeks:
  course = 'DSA'
  list_of_instance = []
  def __init__(self,name,age):
    self.name = name
    self.age = age
    Greeks.list_of_instance.append(self)

  @classmethod
  def x(cls):
    return f"course name is :{cls.course}"
  @classmethod
  def y(cls):
    return f"{cls.list_of_instance}"
  @staticmethod
  def z():
    return f"welcome to my course"
g1 = Greeks("zobayer",22)
g2 = Greeks("raihan",23)

print(Greeks.x())
print(Greeks.y())
print(Greeks.z())



class Uni:
  class_variable = "AIUB"

  def __init__(self,a,b):
    self.name = a
    self.__Id = b

  def x(self):
    print("name:",self.name,"ID:",self.__Id,"University name:",Uni.class_variable)
  @classmethod
  def y(cls,uni_name):
    cls.class_variable = uni_name

c1 =Uni("zobayer",11)
c2 = Uni("hello",23)
c1.x()
Uni.y("AIUB university")
c1.x()
c2.x()


print("\n")   

class University:
  uni_name = "AIUB"

  def __init__(self,name,id):
    self.name = name
    self.__id = id
  def details(self):
    print("name:",self.name ," ID:",self.__id," University name:",self.uni_name)
  @classmethod
  def Uni_name(cls,uni_name):
    cls.uni_name =uni_name 


c1 = University("zobayer",23)   
c1.details()
University.Uni_name("Amrican international university")
c1.details()


#constractor overloading
# class Name:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   def output(self):
#     print("name:",self.name, " age: " ,Name.age) 
 
#   @classmethod
#   def classMethod(cls):
    
#     return
  
class Course:
  course = "DSA"
  list=[]
  def __init__(self,name):
    self.name = name
    Course.list.append(self)

  @classmethod
  def x(cls):
    return f"the name of this course{ cls.course}"
  @classmethod
  def y(cls):
    return f" the total instance object {len(cls.list)}"
  @classmethod
  def WelcomeMessage(cls):
    return f"welcome to my course"

obj = Course("zobayer")
obj = Course("Efat")
print(Course.x())    
print(Course.y())
print(Course.WelcomeMessage())

class Student:
  student = "zobayer"
  def x(obj):
    print("the name of the student ",obj.student)


Student.x = classmethod(Student.x)
Student.x()

class Date:
  def __init__(self,year,month,day):
    self.year =year
    self.month = month
    self.day = day

  @classmethod
  def classmethod(cls,x):
    year,month,day = map(int,x.split('-'))
    return cls( year, month, day)
  
c = Date.classmethod("2025-07-23")
print(c.year,c.month,c.day)  




     
 




     
