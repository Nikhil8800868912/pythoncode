givnumber = int(input("input the number(n): "))  
count = 0 
for num in range(givnumber + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           count +=1
print("Number of prime numbers which are less thanor equal to n:" ,count) 
