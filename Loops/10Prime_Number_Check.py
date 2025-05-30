#Q. Write a program that checks if a number input by the user is a prime number using a for loop.

n=int(input("enter the range"))
divisor_count=0
if (n==1):
    print("number is prime ")

else:
    for i in range (1,n+1):
        if(n%i==0):
            divisor_count+=1
    if (divisor_count==2):
            print("Number is  prime")
    else:print("number is not prime ")




