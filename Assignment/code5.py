
"""
5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
"""
sub1=int(input("sub1= "))
sub2=int(input("sub2= "))
sub3=int(input("sub3= "))
avg=(sub1+sub2+sub3)/3
print("The obtained grade from given marks are: ",end=" ")
if avg>=90:
    print('A')
elif avg>=80:
    print('B')
elif avg>=70:
    print('c')
elif avg>=60:
    print('D')
else:
    print('F')
