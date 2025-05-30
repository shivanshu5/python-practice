#Q.Write a program that prints the first n Fibonacci numbers, where n is input by the user.

n=int(input("enter the range"))
a=0
b=1
print(a,end=" ")
for i in range(1,n+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c