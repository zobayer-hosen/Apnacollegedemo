# compile- Time polymorphism:
#this type of polymorphism is determined during the compilation of the program.it allows method
#methods or operators with the same name to behave differently based on their input parameters or usage.
#its a method overloading


#Run Time polymorphism:
#this type of polymorphism is determined during the 
#execution of the program. it occurs when a subclass 
#provides a specific implementation for a method already 
#defined in its parent class, commonly as method overriding

class Dog:
  def sound(self):
    print("dog sound")# Default implementation
class Labrador(Dog):
  def sound(self):
    print("Labrador woofs")# override the parent method
class Beagle(Dog):
  def sound(self):
    print("Beagle Barks")# overriding parent method
#Compile-Time polymorphism : method overloading mimic
class Calculator:
  def add(self,a, b=0,c=0):
    return a+b+c #supports multiples ways to call add()
#Run-Time polymorphism
dogs = [Dog(),Labrador(),Beagle()]
for dog in dogs:
  dog.sound()# Calls the appropriate method based on the object type

calc = Calculator()
print(calc.add(5,10))
print(calc.add(5,6,15))
     


