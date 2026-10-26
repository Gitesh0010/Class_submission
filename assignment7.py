import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Allow the user to provide the CSV file name as input
filename = input("Enter the CSV file name: ")
df = pd.read_csv(filename)

print("\nDataset:")
print(df)

# 2. Calculate and display averages
print("\n--- Class Averages ---")
print(df[["Maths", "Python", "Attendance"]].mean())

# 3. Line Plot
plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o", label="Python Marks", color="blue")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.legend()
plt.grid(True)
plt.show()

# 4. Bar Plot
plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"], label="Maths Marks", color="orange")
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.legend()
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70, label="Student Data", color="red")
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.legend()
plt.grid(True)
plt.show()

# 6. Correlation Matrix and Heatmap
correlation = df[["Maths", "Python", "Attendance"]].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

# 7. Challenge Task: Histogram of Python marks
plt.figure(figsize=(7, 4.5))
plt.hist(df["Python"], bins=5, color="purple", edgecolor="black", label="Frequency")
plt.title("Histogram of Python Marks")
plt.xlabel("Python Marks")
plt.ylabel("Number of Students")
plt.legend()
plt.show()

# 8. Challenge Task: Box plot for Maths and Python marks
plt.figure(figsize=(7, 4.5))
sns.boxplot(data=df[["Maths", "Python"]], palette="Set2")
plt.title("Box Plot: Distribution of Maths and Python Marks")
plt.ylabel("Marks")
plt.show()

# 9. Challenge Task: Pie chart showing the number of students from each city
plt.figure(figsize=(6, 6))
city_counts = df["City"].value_counts()
plt.pie(city_counts, labels=city_counts.index, autopct="%1.1f%%", startangle=140, colors=["lightblue", "lightgreen", "lightcoral"])
plt.title("Distribution of Students by City")
plt.show()
