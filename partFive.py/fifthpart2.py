import re
student_ID  = input("What is your student ID? ").strip()
if re.search(r"^[A-Za-z]{4}\d{4}$", student_ID):
    print("Valid.")
else:
    print("Invalid.")