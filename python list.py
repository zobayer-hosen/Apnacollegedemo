#list can contain duplicate item 
#list in python are Mutable . Hence We can modify replace or delete the items
# list are ordered it maintain the order of elements based on they are added
# Accessing items in list can be done directly using their position(index),starting from 0
a = [10,20,"CGF",40,True]

print(a)
print(type(a[0]))
print(type(a[2]))


#we can create a list by passing an iterable (like a string ,tuple , or another list to list () function )

a = list((1,3,3,5,'apple',4.5))
print(a)

# append() adds ab element at the end of the list
# extend() adds multiples elements to the end of the list
#insert() adds an elements at a specific positions

s=[]

s.append(11)
print(s)

#Inserting 5 at index 0
s.insert(0,5)
print(s)

s.extend([5,10,11])
print(s)


#we can change the value of an elements by accessing it using index
a=[10,20,30,40,50]

a[1]=30
print(a)


#remove the first occurrence of an elements 
a.remove(10)
print(a)

# pop() Removes the elements at a specifics index or the last elements if no index is specified
poped_val = a.pop(1)
print(poped_val)
print(a)


r1=0
r2=10

li = list(range(r1,r2))
print(li)


li= [i for i in range(r1,r2)]
print(li)


#Initialize a Dictionary of list
d={
}

d['1']= [1,2]
d["2"]= ["greek",3,5]
d[3]=['abc']
d[4]='apple'

print(d)


#using the ZIp() function 
k = ["fruits ","vegetables","drinks"]
val=[['apple','banana'],["carrot","spinach"],["water","juice"]]
d= dict(zip(k,val))
print(d)


li =[('Fruits',"apple"),("Fruits","Banana"),("Vegetables","Carrot"),("fruits",0)]
d={}

for k ,items in li:
    d.setdefault(k,[]).append(items)
print(d)  



#ANOTHER TOPIC

#using zip for a list to inside list(tuple)
a = [1,2,3]
b= ['apple','banana','cherry']
res = list(zip(a,b))
print(res)

res = dict(zip(a,b))
print(res)
#MAP() is most efficient approach to convert a list of lists 
#into a list of tuples . it applies the tuples() constructor to 
# each sublist,transforming each inner list into a tuple

a =[[1,'apple'],[2,'orange'],[3,'cherry']]

res = list(map(tuple,a))
print(res)

a=[1,2,3]
b=['apple','orange','cherry']
rs = [(x,y) for x,y in zip(a,b)]
print(rs)
result=[]
for i in range(len(a)):
    result.append((a[i],b[i]))
print(result)    


# ANOTHER TOPIC
#how to create list of dictionary in python
a=[{"name":"Alice","age":25},{"name":"Bob","age":30}]
print(a)
print(type(a))

a = []
for i in range(3):
    a.append({"name":f"Person {i+1}","age":20+i})
print(a) 


a= [{"name":f"Person {i+1}","age":20+i} for i in range(3)]
print(a)

names = ["Alice","Bob","Charlie"]
ages =[25,30,22]

a=[{"name":names[i],"age":ages[i]} for i in range(len(names))]
print(a)


lod=[
    {'name':'alice','age':25,'city':"new york"
    },
    {
        'name':"bob","age":30,'city':"Los Angeles"
    },
    {
        'name':"Charlie",'age':35,'city':'Chicago'
    } 
]
d1= lod[0]
print(d1)
print(lod[1]['name'])

#another topic 
n=5
b= list(range(n))
print(b)
a=[0 for i in range(n)]
print(a)


def create_List(n):
    return [0]*n
n= 5
a= create_List(n)

print(a)



#Another Topic
#Create a  list of string in python
d= ["gfg"+str(i) for i in range(3)]
print(d)

c=[]
for i in range(3):
    c.append("gfg"+ str(i))
print(c)    

e=["geeks",'for']
e.extend(["greeks","gfg"])
print(e)

#another topic
#Create a list of tuples with Numbers and Their Cubes _Python

a=[1,2,3,4,5,6]

res=[(n,n**3)for n in a]
print(res)
#creating list of tuples using map and Lambda
res =list(map(lambda n:(n,n**3),a))
print(res)

for n in a:
    res.append(list((n,n**3)))
print(res)   


rs = list((n,n**3)for n in a)
print(rs)

a= list(map(lambda x:x*0.5, range(10)))
print(a)