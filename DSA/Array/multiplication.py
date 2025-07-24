def multiplication(n):
  for i in range(1,11):
    print("%d * %d = %d" % (n,i ,n*i))
if __name__ == "__main__":
  n = 15
  multiplication(n)



print("\n")
# another one is recursive Aproch

def multi(n, i=1):
  
   if (i ==11): # base case 
     return
   print(n, "*", i ,"=", n*i)
   i +=1
   multi(n,i)
if __name__== "__main__":
  n = 4
  multi(n)   

   