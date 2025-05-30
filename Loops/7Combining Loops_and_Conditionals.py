#Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.

n = int(input("enter a num"))
for i in range (1,n):
    if (i%2==0):
        print("even number is ",i)