def binarySearch(arr,low,high,x):
  while low<= high:
    mid = low +(high - low)//2

    #check if x is present at mid
    if arr[mid] ==x:
      return mid
    #if x is greater,ignore left half
    elif arr[mid]<x:
      low = mid+1
    #If x is smaller,ignore right half
    else:
      high = mid -1
#if we reach here ,then the element was not present 
  return -1

if __name__ == "__main__":
  arr=[1,2,3,43,5,6,7,87]
  x= 87

  result = binarySearch(arr,0,len(arr)-1,x)
  if result != -1:
    print("Element is present at index",result)
  else:
    print("Element is not present in array")  


# check Even or odd
def isEven(n):
  rem = n%2
  if rem == 0:
    return True
  else:
    return False
if __name__ == "__main__":
  n=15
  if isEven(n):
    print("true")
  else:
    print("false")  

 #BITWISE OPERATION 
def isEven(n):
  if(n & 1 )== 0:
    return True
  else:
    return False
  
if __name__ =="__main__":
  n =44

  if isEven(n):
    print("this number is Even")
  else:
    print("this is not a even number s")    
  
def printTable(n):
  for i in range(1,11):
    #Multiple from i to 10
    print("%d * %d = %d"%(n,i,n*i))
if __name__ =="__main__":
  n =5
  printTable(n)

print("\n")
#Recursive Approach
def printTable(n,i=1):
  if(i==11):
    return
  print(n,"*",i,"=",n*1)
  i+=1
  printTable(n,i)
if __name__ == "__main__":
  n =5
  printTable(n)

print("\n")
#program for sum of n natural numbers
def findSum(n):
  sum = 0
  x=1

  while x<=n:
    sum +=x
    x+=1
  return sum
if __name__ == "main":
  n = 5
  print(findSum(n)) 

# PROGRAM FOR SUM of squares of first n natural numbers

#[naive approach]
def summation(n):
  return sum([i**2 for i in range(1,n+1)])

if __name__ =="__main__":
  n =2
  print(summation(n))
#[Expected Approach]

def summation(n):
  a = (n*(n+1)*(2*n+1))/6
  return a
if __name__ == "__main__":
  n = 10
  print(summation(n))

#Avoiding the overflow 
# In the above method, sometimes due to large value of n, the value of
# (n*(n+1)*(2*n+1)) would overflow . We can avoid this overflow up to 
# some extent using the fact that n*(n+1) must be divisible by 2 and restructuring 
# the formula as(n*(n+1)/2)*(2*n+1)/3

def summation(n):
  #to avoid overflow
  return (n*(n+1)//2)*(2*n+1)//3
def main():
  n = 10
  print(summation(n))
if __name__ == "__main__":
  main()    


# swapping tuple unpacking 
if __name__ == "__main__":
  a=2
  b=3
  print("a =",a,"b =",b)

  #tuple unpacking
  a,b = b,a
  print("a =",a," b =",b)


  #THE DICE PROBLEM
  def oppositeFaceofDice(n):
    if n ==1:
      return 6
    elif n==2:
      return 5
    elif n==3:
      return 4
    elif n==4:
      return 3
    elif n==5:
      return 2
    else:
      return 1
    
  n = 2
  print(oppositeFaceofDice(n))  

  #[Expected Approach] Using Sum of two Sides
  def oppsiteFaceofDice(n):
    ans= 7-n
    return ans
  n = 2
  print(oppsiteFaceofDice(n))

  #Nth term of AP from first two terms
  def nthTermOfAP(a1,a2,n):
    nthTerm = a1
    d = a2-a1
    for i in range(1, n):
      nthTerm += d
    return nthTerm
  a1 = 2
  a2 = 2
  n = 4
  print(nthTermOfAP(a1,a2,n))


  #another approach
  def nthTermOfAP(a1,a2,n):
    return a1 + (n-1)*(a2-a1)
  
  a1 = 2
  a3 = 3
  n =4
  print(nthTermOfAP(a1,a2,n))
    

  





       

  
  

        
