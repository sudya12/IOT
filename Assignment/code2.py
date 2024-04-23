"""
2] Write a program to accept a 4 digit number and
a. Display face value of each decimal digit
b. Display place value of each decimal digit
c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
ut should be
a. 9 3 6 1
b. 9361 = 9 000 + 300 + 60 + 9
c. 1639
"""
num=int(input("enter the four digit number:"))
num1=str(num)
print("face value of given digit are: ")
for i in num1:
    print(i)
print("The place value of each digit are: ")
place=1
for j in range(3,-1,-1):
    print(f"{num1[j]}={int(num1[j])*place}")
    place=place*10
print("Digits in reverse order are: ")
for k in range(3,-1,-1):
    print(num1[k] ,end=" ")
print("\nThe number in reverse is: ",num1[::-1])