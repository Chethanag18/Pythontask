a = int(input())
b = int(input())
try:
    c = a/b 
except ZeroDivisionError:
    print("Give valid Input")
else:
    print("No Error")