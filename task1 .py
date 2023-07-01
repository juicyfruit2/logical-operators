# Declared three variables and assigned each variable a number value.
num1 = 2
num2 = 400
num3 = 12

# Compared two variables using if,else statements 
if num1 > num2:
    print(num1)
else:
    print(num2)

# Using if,else statements to determine if a number is odd or even 
if num1 % 2 == 0:
    print(num1," is an even number:" )
else:
    print(num1,"is an odd number:")

# wrote conditional statements to sort three numbers from largest to smallest

largest = (num1, num2, num3)
if num1 > num2 and num1 > num3 :
    largest_number = num1

elif  num2 > num1 and num2 > num3:
   largest_number = num2 
    
else:
    largest_number = num3 
 
print(f"The largest of these 3 numbers are",largest_number)   
    
smallest = (num1 , num2, num3)
if num1 < num2 and num1 < num3:
    smallest_number = num1 

elif num2 < num1 and num3 < num3:
    smallest_number = num2 

else:
    smallest_number = num3 
    
print(f"The smallest of these 3 numbers are",smallest_number)

     

     











# from pyton programing (You tube) - how to get the largest - smallest number 
 # I watched this video as it gave me and idea on how to begin my program 
 # I changed the variables and the structure of the code.
 # just wanted to bring it to your attention ! 







