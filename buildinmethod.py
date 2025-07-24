name = "zobayer"
age = 21
print("my name is ",name , "i am ",age ," years old" ,sep=",")

print(" hello every one", end=" ")
print("i am here")

def test_func(a,b):
  """a: value 1
  b: value 2
  return: int """
  return a+b

help(test_func)

ran = range(10,0,-2)
print(list(ran))

string = ["my","name","is","zobayer"]

length= map(len,string)
length = map(lambda x:x+"s",string)

def add_s(string):
  return string +"s"
length = map(add_s,string)
print(list(length)) 

# filter method

def longer_then_4(string):
  return len(string) >4
string = ["my", "world", "apple", "pear"]
filtered = filter(longer_then_4,string)
filtered = filter(lambda x:len(x)>4, string)
print(list(filtered))

numbers = {1,4.5,5,23,2}
print(sum(numbers,start= 10))


#sorted list
list= [ 1,3,-3,5,9,1,4]
another_list = sorted(list, reverse=True)
print("this list is decending order",another_list)
new_list = sorted(list)
print("this new list is aciending order", new_list)

people = [
  {"name": "zobayer", "age": 22},
  {"name": "alice", "age": 23},
  {"name": "david", "age": 25},
  {"name": "chairle", "age": 21}
]

another_new_list = sorted(people, key=lambda x: x["age"],reverse=True)
print(another_new_list)


#enumerate
tasks = ["write report","Attend meeting","Review code","Submit timesheet"]
# for index in  range(len(tasks)):
#   task = tasks[index]
#   print(f"{index+1},{task}")


for indax,value in enumerate(tasks):
    print(f"{indax+1}.{value}")


#
names = ["Alice","Bob","Charlie","David"]
ages =[30,45,60,16]

# for idx in range(min(len(names),len(ages))):
#    name = names[idx]
#    age = ages[idx]
#    print(f"{name} is {age} years old")

combined = list(zip(names, ages))
print(combined)




