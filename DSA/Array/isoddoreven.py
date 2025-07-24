def iseven(n):

  rem = n%2

  if rem == 0:
    print("this value is even")
  else:
    print("this value is odd")
  
iseven(5)

# bit wise connection 
def isodd(n):

  if(n & 1)==0:
    return False
  else:
    return True
if __name__ == "__main__":
  n=16
  if isodd(n):
    print("this is a odd number ")
  else:
    print("this is even number")      


  

  