import re
pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url = input()
if re.match(pattern,url):
    print("Valid URL")
else:
    print("Invalid URL")
    