import re
text = """
Contact us at student@gmail.com or admin@college.edu.
Call us at 9876543210 or 9123456789.
"""
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)
phones = re.findall(r'\b\d{10}\b', text)
print("Email Addresses:")
for email in emails:
    print(email)
print("\nPhone Numbers:")
for phone in phones:
    print(phone)