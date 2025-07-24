class Greeter:
  def greet(self,name):
    print(f"Hello,{name}")

g = Greeter()
g.greet("zobayer")    

print("\n")

class Calculator:
  def add(self,a,b):
    return a+b
  def subtract(self,a,b):
    return a-b
cal = Calculator()
print("sum :",cal.add(4,5))
print("sub",cal.subtract(5,3))  

print("\n")
class Employee:
  def __init__(self,name,id= None,department=None):
    self.name = name
    self.id = id
    self.department = department
  def display_details(self):
    print(f"name:,{self.name}") 
    if self.id:
      print(f"ID: {self.id}")
    if self.department:
      print(f"Department: {self.department}")
emp1 = Employee("zobayer")
emp1.display_details()
emp2 = Employee("Doe",101)
emp2.display_details()
emp3= Employee("jane",102,"HR")
emp3.display_details() 

print("\n")

class SeriesCalculator:
  def calculate_sum(self,n,a=1,b=2):
    return n*(2*a+(n-1)*b)//2
sc = SeriesCalculator()
print("Sum of series :",sc.calculate_sum(5))  



#Create a class MaxFinder that identifies the largest number in a list

class MaxFinder:
  def __init__(self,numbers):
    self.num = numbers

  def maxnumber(self):
    if not self.num:
      return "List is empty"
    return max(self.num)  
  

finder = MaxFinder([1,2,3,4,5,6])
print(f"the max number is ",{finder.maxnumber()})
finder2 = MaxFinder([])
print(f"{finder2.maxnumber()}")

#MULTIPLY THE TWO NUMBER 

class Rectangale:
  def __init__(self,first_num=1,second_num=1):
    self.first_num = first_num
    self.second_num = second_num
  def set_dimention(self,first_num,second_num):
    self.first_num = first_num
    self.second_num = second_num

  def rect(self):
    return self.first_num* self.second_num
ans = Rectangale()
print(ans.rect())
  
#define grade

class Grade:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks

  def average(self):
    return sum(self.marks)/len(self.marks)
  def grade(self):
    average = self.average()
    if average >= 90:
      return 'A'
    elif average >=80:
      return 'B'
    elif average >=70:
      return 'C'
    else:
      return 'Fail'
result = Grade("zobayer",[80,70,90])
print(result.name," " ,result.grade())    


#after remider write the remider word
class Remider:
  def __init__(self ,numbers):
    self.numbers = numbers
    
    

  def x(self):
     remider = self.numbers % 10
     word = ['gero','one','two','three','four','five','six','seven','eight','nine']
     return word[remider]
y = Remider(2345)
print(y.x())  


#counter

class CounterMehtod:
  count =0
  def __init__(self):
    CounterMehtod.count +=1
  @staticmethod  
  def x():
    return  "the number is",CounterMehtod.count

y = CounterMehtod()
z= CounterMehtod()
CounterMehtod.x()

#STATIC METHOD
from datetime import date
class Age:

  def __init__(self,name,age):
    self.name = name
    self.age = age
    pass
  @classmethod
  def x(cls,name,year):
    return cls(name, date.today().year - year)
  @staticmethod
  def y(age):
    return age>18
xy = Age("zobayer",22)  
xy = Age.x("zobayer",2002)
print(xy.x())



# THIS IS A CLASS AND STATIC METHOD

class Multiplication:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  @classmethod
  def change_value(cls,x,z):
    return cls()






    



    






    