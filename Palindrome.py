str = input()
lower = str.lower()
reverse = lower[::-1]
if lower == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")