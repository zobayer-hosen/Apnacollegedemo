a=[1,2,4,7,9,1,0,3]

max_value =0
for i in a:
  if i>max_value:
    max_value = i

second_value =0
for j in a:
  if j != max_value and j>second_value:
    second_value = j
third_value = 0
for k in a:
  if k != max_value and k != second_value and k>third_value:
    third_value = k
print("third largest value ", third_value) 


#another way largest element of the array
def  largestelement(value):
  arr = len(value)

  value.sort()

  return value[arr-3]
if __name__ == "__main__":
 print(largestelement([1,2,4,6,8,4]))
