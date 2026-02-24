import re
uk_number  = input("What is your phone number? ").strip()
if re.search(r"^\+?(0|7)\d{10,12}$", uk_number):
    print("Valid.")
else:
    print("Invalid.")