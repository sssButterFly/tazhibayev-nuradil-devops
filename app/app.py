import os

name = os.getenv("STUDENT_NAME", "Nuradil")
surname = os.getenv("STUDENT_SURNAME", "Tazhibayev")
group = os.getenv("STUDENT_GROUP", "IT2-2310")
student_id = os.getenv("STUDENT_ID", "34608")

print("================================")
print("DevOps Student Application")
print("================================")
print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Group: {group}")
print(f"Student ID: {student_id}")
print("Application is running successfully!")
