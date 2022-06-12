# program to display the grade of a student
print("Please enter your marks")
marks = int(input())
if(marks<25):
    print("F grade")
elif(marks>=25 and marks<45):
    print("E grade")
elif(marks>=45 and marks<50):
    print("D grade")
elif(marks>=50 and marks<60):
    print("C grade")
elif(marks>=60 and marks<80):
    print("B grade")
elif(marks>=80 and marks<=100):
    print("A grade")
else:
    print("Invalid input")
