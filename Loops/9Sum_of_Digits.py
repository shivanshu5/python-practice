#Q.  Write a program that calculates the sum of the digits of a number input by the user using a while loop.

num = int(input("enter a number "))
sum_of_digits=0
while(num>0):
    digit=num%10
    sum_of_digits+=digit
    num=num//10
print("sum of digit",sum_of_digits)
