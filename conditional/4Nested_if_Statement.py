#Q.Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative

n=int(input("give a number "))
print(n)
if(n>0):
    print("number is positive ")
    if(n%2==0):
        print("number is even ")
    else: print("number is odd ")
else:
    print("number is negative ")
    if(n%2==0):
        print("number is even ")
    else: print("number is odd ")