import pandas as pd
import random

names = [
    "Rahul Sharma", "Priya Patil", "Amit Desai", "Sneha Joshi", "Rohit Kulkarni",
    "Pooja Nair", "Vikas Mehta", "Anjali Singh", "Karan Verma", "Neha Gupta",
    "Suresh Yadav", "Divya Reddy", "Manish Tiwari", "Riya Shah", "Arjun Mishra",
    "Kavya Menon", "Deepak Pandey", "Simran Kaur", "Nikhil Bose", "Tanvi Doshi",
    "Aakash Patel", "Shweta More", "Raj Thakur", "Meera Iyer", "Sumit Chauhan",
    "Pallavi Nair", "Gaurav Jain", "Shruti Pillai", "Hardik Solanki", "Ankita Roy",
    "Yash Bhatt", "Nisha Rao", "Vishal Dubey", "Kritika Sen", "Mohit Agarwal",
    "Swati Malik", "Pranav Ghosh", "Ishita Das", "Saurabh Sinha", "Ruksar Khan",
    "Tejas Pawar", "Ashwini Hegde", "Kunal Kapoor", "Vrinda Sharma", "Parth Joshi",
    "Madhuri Patil", "Sanket Desai", "Leena Nambiar", "Aditya Saxena", "Farhana Sheikh"
]

subjects = ["Maths", "Science", "English", "History", "Computer"]

random.seed(42)

data = []
for name in names:
    marks = [random.randint(20, 100) for _ in subjects]
    total = sum(marks)
    percentage = round(total / (len(subjects) * 100) * 100, 2)
    grade = (
        "A+" if percentage >= 90 else
        "A"  if percentage >= 75 else
        "B"  if percentage >= 60 else
        "C"  if percentage >= 50 else
        "D"  if percentage >= 40 else "F"
    )
    result = "Pass" if percentage >= 40 else "Fail"
    data.append([name] + marks + [total, percentage, grade, result])

columns = ["Name"] + subjects + ["Total", "Percentage", "Grade", "Result"]
df = pd.DataFrame(data, columns=columns)
df.to_csv("students.csv", index=False)

print("✅ students.csv generated with", len(df), "students!")
print(df.head())