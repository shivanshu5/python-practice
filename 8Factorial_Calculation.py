#Q. Write a program that calculates the factorial of a number input by the user using a while loop.

n = int(input("Enter a number for factorial"))
fact=1
i=1
while (i<=n):
   
    fact=fact*i
    i=i+1    
print("factorial ", fact) 