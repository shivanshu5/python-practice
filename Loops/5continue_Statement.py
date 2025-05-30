#Q. Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.

i=1
while (i<11):
    if(i==5):
        i=i+1
        continue
    print("number",i)
    i=i+1

'''i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print("number", i)
    i += 1'''
