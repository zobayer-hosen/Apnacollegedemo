a=[1,5,7,2,9,4,5]
max_value =0
for i in a:
  if i >max_value:
    max_value = i
second_max = 0
for j in a:
  if j != max_value and j>second_max:
    second_max = j
print("the second largest value",second_max)    
