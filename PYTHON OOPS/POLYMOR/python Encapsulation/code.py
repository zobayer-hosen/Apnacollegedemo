#Encapsulation: Hides internal data. protects it from unwanted change
#validation: you can add checks before setting a value
#read-only or Write-only: You can allow read-only or write-only access to some attributes
#Futures: you can later change how data is stored without changing interface


class Dog:
  def __init__(self,name,breed, age):
    self.name = name
    self._breed = breed 
    self.__age = age # private attribute
# public method
  def get_info(self):
    return f"Name: {self.name},Breed:{self._breed},Age:{self.__age}"
  
  #getter and setter for private attribute:
  def get_age(self):
    return self.__age
  def set_age(self, age):
    if age>0:
      self.__age = age
    else:
      print("Invalid age!")

dog = Dog("buddy","Labrador",3)

print(dog.name)  #accessing public member

print(dog._breed)# accessing protected member

print(dog.get_age())
dog.set_age(0)
print(dog.get_info())

 