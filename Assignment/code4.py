# Write a Python function to find the maximum of three numbers.
print("put the three numbers: ")
x=int(input())
y=int(input())
z=int(input())
print("maximum number from input is: ",end="")
if x>y:
    if y>z:
        print(x)
    else:
        print(z)
else:
    if y>z:
        print(y)
    else:
        print(z)