import re 
pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&+=!]).{6,}$'
password = input()
if re.fullmatch(pattern,password):
    print("Valid Password")
else:
    print("Invalid password")