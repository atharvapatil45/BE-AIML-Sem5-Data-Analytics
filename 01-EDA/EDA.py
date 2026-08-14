# Exploratory Data Analysis:
# Descriptive Statistics, Histogram and Correlation Matrix

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Dataset.csv")

# Display first 5 rows
print(data.head())

# Display column names
print(data.columns)

# Calculate Mean, Median and Mode
Mean_value = data["Balance"].mean()
print(f"Mean Value = {Mean_value}")

Median_value = data["Balance"].median()
print(f"Median Value = {Median_value}")

Mode_value = data["Balance"].mode()[0]
print(f"Mode Value = {Mode_value}")

# Plot histogram
plt.hist(data["Balance"], bins=20, color="pink")

# Display Mean, Median and Mode
plt.axvline(
    Mean_value,
    color="skyblue",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {Mean_value}"
)

plt.axvline(
    Median_value,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Median: {Median_value}"
)

plt.axvline(
    Mode_value,
    color="yellow",
    linestyle="--",
    linewidth=2,
    label=f"Mode: {Mode_value}"
)

plt.title("Balance Distribution")
plt.xlabel("Balance")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Calculate correlation matrix
correlation_matrix = data.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation_matrix)
