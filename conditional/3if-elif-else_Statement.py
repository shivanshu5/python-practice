#Q. Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero.

n= int(input("give a number for check"))
print(n)
if(n>0):
    print("number is positive")
elif(n==0):
    print("number is zero")
else:
    print("number is negative")