#Sum all the items in a list
def sum_list(items):
  
  sum_numbers = 0

  for x in items:
    sum_numbers += x

  return sum_numbers
print(sum_list([2,3,4,5]))  

#MUltiply items in list

def multiple_list(items):
  multiple_numbers = 1

  for x in items:
    multiple_numbers *= x

  return multiple_numbers
print(multiple_list([2,3,4,5,6]))
  
#Get Largest number in the list 

def Max_value(list):
  max_value = 0
  
  for x in list:
    if x > max_value:
      max_value = x
    else:
      continue
  return max_value
print(Max_value([4,7,1,5,0,3,6,9]))    


#Get Smallest Number in list 
def small_value(list):
  min_value = 0

  for x in list:
    if x < min_value:
      min_value = x
    else:
      continue
  return min_value
print(small_value([-1,3,4,6,-2,6,9,0]))  

#Count Strings with same start and End

def Count_string(list):
  count = 0

  for i in list:

    if len(i)>0 and i[0]==i[-1]:
      count +=1

  return count
print(Count_string(["aba","ccc","abc","xyx","121"]))    


#Sort Tuples by last Element 
def last(n):
  return n[1]
def sort_list_last(tuples):
  return sorted(tuples,key=last)
print(sort_list_last([(2,5),(1,2),(4,4),(2,3)]))

#remove Duplicate from list
a = [1, 2, 3, 4, 5, 6, 3, 4, 2, 8, 6]
new_list = []

for i in a:
    if i not in new_list:
        new_list.append(i)

print(new_list)


#Check a list is empty or not
a=[]
b=[1,2,3,4,3,6]

if not a:
  print("List is Empty")
else:
  print("List is empty")  

#clone or Copy a list
b=[1,2,3,4,3,6]
a=[]
for i in b:
  a.append(i)
print("this is a list of a ",a)  
new_list = list(b)
print(new_list)


#list greater than n

def list(n,value):
  new_list=[]

  value = str.split(" ")

  for i in value:
    if len(value) == n:
      new_list.append(i)
    return new_list  

    
  print(list(4,"my name is zobayer hosen"))


