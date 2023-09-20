import re

email = input("Email? ").strip()
    
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")