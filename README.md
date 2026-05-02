# 📊 Student Result Analyzer

A Python-based data analysis tool that generates student data and produces visual reports with charts and statistics.

---

## 🚀 Features

- 📁 Auto-generates realistic student dataset (50 students, 5 subjects)
- 📊 Analyzes total marks, percentage, grades, and pass/fail status
- 🏆 Displays top 5 and top 10 performers
- 📚 Calculates subject-wise average marks
- 📈 Generates 4 visual charts saved as PNG files

---

## 📈 Sample Output Charts

| Chart | Description |
|-------|-------------|
| `pass_fail.png` | Pie chart of pass vs fail ratio |
| `grade_distribution.png` | Bar chart of grade distribution |
| `subject_averages.png` | Average marks per subject |
| `top10_students.png` | Top 10 students by percentage |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-orange?style=flat)

---

## 📦 How to Run

1. Clone the repository
2. Install dependencies:
```
pip install pandas matplotlib
```
3. Generate student data:
```
python generate_data.py
```
4. Run the analyzer:
```
python analyzer.py
```
5. Check the `output/` folder for generated charts

---

## 📁 Project Structure

```
student-result-analyzer/
├── generate_data.py   # Generates fake student dataset
├── analyzer.py        # Main analysis + visualization script
├── students.csv       # Generated dataset
└── output/            # Generated chart images
```

---

## 📄 License

Open source for educational use.
```

