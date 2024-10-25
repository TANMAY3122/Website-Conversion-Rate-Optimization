import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

# Step 1: Load the Data
data = pd.read_csv("ab_test_data.csv")  # Change the path if necessary

# Step 2: Exploratory Data Analysis
# Check for missing values
print("Missing values in each column:\n", data.isnull().sum())

# Check for duplicate rows based on user_id
duplicates = data[data.duplicated(subset="user_id", keep=False)]
print("Duplicate rows based on user_id:\n", duplicates)

# Summary statistics of the data
print("Summary statistics:\n", data.describe())

# Count the number of users in each variation group
print("Variation distribution:\n", data["variation"].value_counts())

# Unique values in 'converted' column
print("Unique values in 'converted':", data["converted"].unique())

# Step 3: Calculate Conversion Rates for Each Group
control_group = data[data["variation"] == "control"]
treatment_group = data[data["variation"] == "treatment"]

control_conversion_rate = control_group["converted"].mean()
treatment_conversion_rate = treatment_group["converted"].mean()

print(f"Control Group Conversion Rate: {control_conversion_rate * 100:.2f}%")
print(f"Treatment Group Conversion Rate: {treatment_conversion_rate * 100:.2f}%")

# Step 4: Formulate Hypotheses
# H₀: There is no difference in conversion rates.
# H₁: There is a difference in conversion rates.

# Step 5: Conduct the Statistical Test
# Sample sizes
n_control = control_group.shape[0]
n_treatment = treatment_group.shape[0]

# Number of conversions
conversions_control = control_group["converted"].sum()
conversions_treatment = treatment_group["converted"].sum()

# Run the two-proportion z-test
count = [conversions_control, conversions_treatment]
nobs = [n_control, n_treatment]
z_stat, p_value = proportions_ztest(count, nobs)

# Step 6: Interpret Results
print(f"Z-Statistic: {z_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

# Step 7: Conclusion
if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference in conversion rates.")
else:
    print("Fail to reject the null hypothesis: No significant difference in conversion rates.")

# Step 8: Visualization (Optional)
# Bar plot of conversion rates
labels = ['Control', 'Treatment']
conversion_rates = [control_conversion_rate, treatment_conversion_rate]

plt.bar(labels, conversion_rates, color=['blue', 'green'])
plt.ylabel('Conversion Rate')
plt.title('Conversion Rates for Control and Treatment Groups')
plt.ylim(0, 1)
plt.axhline(0.05, color='red', linestyle='dashed', label='Significance Level (α = 0.05)')
plt.legend()
plt.show()
