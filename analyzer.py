import pandas as pd
import matplotlib.pyplot as plt
import os

# ── Load Data ──────────────────────────────────────────
df = pd.read_csv("students.csv")
os.makedirs("output", exist_ok=True)

print("=" * 50)
print("       STUDENT RESULT ANALYZER REPORT")
print("=" * 50)

# ── Basic Stats ────────────────────────────────────────
total_students = len(df)
passed = len(df[df["Result"] == "Pass"])
failed = len(df[df["Result"] == "Fail"])

print(f"\n📊 Total Students  : {total_students}")
print(f"✅ Passed          : {passed}")
print(f"❌ Failed          : {failed}")
print(f"📈 Pass Percentage : {round(passed/total_students*100, 2)}%")

# ── Grade Distribution ─────────────────────────────────
print("\n📋 Grade Distribution:")
print(df["Grade"].value_counts().to_string())

# ── Top 5 Students ─────────────────────────────────────
print("\n🏆 Top 5 Students:")
top5 = df.nlargest(5, "Percentage")[["Name", "Percentage", "Grade"]]
print(top5.to_string(index=False))

# ── Subject Averages ───────────────────────────────────
subjects = ["Maths", "Science", "English", "History", "Computer"]
print("\n📚 Subject Averages:")
for sub in subjects:
    print(f"  {sub:10} : {round(df[sub].mean(), 2)}")

# ── Plot 1: Pass vs Fail ───────────────────────────────
plt.figure(figsize=(5, 5))
plt.pie([passed, failed], labels=["Pass", "Fail"],
        autopct="%1.1f%%", colors=["#4CAF50", "#F44336"])
plt.title("Pass vs Fail")
plt.savefig("output/pass_fail.png")
plt.close()
print("\n✅ Saved: output/pass_fail.png")

# ── Plot 2: Grade Distribution Bar Chart ──────────────
grade_counts = df["Grade"].value_counts().sort_index()
plt.figure(figsize=(7, 4))
grade_counts.plot(kind="bar", color="#2196F3", edgecolor="black")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("output/grade_distribution.png")
plt.close()
print("✅ Saved: output/grade_distribution.png")

# ── Plot 3: Subject Average Bar Chart ─────────────────
avg_marks = df[subjects].mean()
plt.figure(figsize=(7, 4))
avg_marks.plot(kind="bar", color="#FF9800", edgecolor="black")
plt.title("Average Marks per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("output/subject_averages.png")
plt.close()
print("✅ Saved: output/subject_averages.png")

# ── Plot 4: Top 10 Students ────────────────────────────
top10 = df.nlargest(10, "Percentage")
plt.figure(figsize=(10, 5))
plt.barh(top10["Name"], top10["Percentage"], color="#9C27B0")
plt.xlabel("Percentage")
plt.title("Top 10 Students")
plt.tight_layout()
plt.savefig("output/top10_students.png")
plt.close()
print("✅ Saved: output/top10_students.png")

print("\n🎉 Analysis Complete! Check the output/ folder for graphs.")