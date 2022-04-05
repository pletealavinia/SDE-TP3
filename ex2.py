def nrprime(n): 
   if n==0 or n==1:
    return False
   for i in range(2,n): 
      if n%i==0: 
        return False 
   return True 
 
m = int(input()) 
for i in range(m+1): 
   if nrprime(i): 
       print(i) 