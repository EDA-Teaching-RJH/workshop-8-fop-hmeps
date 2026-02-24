import re
email = input("What's your email? ").strip()
if re.search(r"^\w+@\w+\.(ac.uk | icloud.com | yahoo.com)$", email):
    print("Valid.")
else:
    print("Invalid.")