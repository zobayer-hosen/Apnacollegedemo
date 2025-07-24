a = [1,2,4,6,8,3,7,9]
b=[2,5,6,8,9,2,4]
c =[]
for i in a:
 
  for j in b:

    if i==j:
      if i not in c:
         c.append(i)

print(c)

#Another Way
def common_value(v1,v2):
  result = False
  for i in v1:
    for i in v2:
      if i==j:
        result = True
  return result
print(common_value([1,4,7,3,6,],[2,4,7,1,4]))
print(common_value([1,2,3,4,5],[6,7,8,9,0]))



      
  

