marks = int(input())
if marks > 90 or marks == 100:
    print("A")
elif marks > 70 or marks == 80:
    print("B")
elif marks > 60 or marks == 70:
    print("C")
else:
    print("Fail")