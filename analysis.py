import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("data.csv")

print("Original Data:")
print(df)

# Data Cleaning
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nCleaned Data:")
print(df)

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Grouping
dept_avg = df.groupby("Department")["Marks"].mean()
print("\nAverage Marks by Department:")
print(dept_avg)

# Insight
top_student = df.loc[df["Marks"].idxmax()]
print("\nTop Scorer:")
print(top_student)

# Optional Graph
dept_avg.plot(kind="bar", title="Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()
