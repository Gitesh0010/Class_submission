import pandas as pd

# Input: A DataFrame with sample data (e.g., student names, marks, and cities)
data = {
    "Student": ["Amit", "Bhavna", "Chetan", "Amit", "Diya", "Esha"],
    "Marks": [85, None, 70, 85, 92, None],
    "City": ["Pune", "Mumbai", "Pune", "Pune", "Nashik", "Mumbai"]
}
df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df.head())

print("\n--- Handling Missing Values ---")
# Fill missing Marks with the mean of the column
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)
print(df)

print("\n--- Removing Duplicates ---")
# Identify and remove duplicate records
print(f"Duplicates found: {df.duplicated().sum()}")
df = df.drop_duplicates()
print(df)

print("\n--- Data Selection and Filtering (loc) ---")
# Select students from Pune with marks > 75
filtered_df = df.loc[(df["City"] == "Pune") & (df["Marks"] > 75)]
print(filtered_df)
