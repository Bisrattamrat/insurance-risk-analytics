from data_loader import load_data
from eda_utils import missing_values, descriptive_stats

# 1. Load the data file
file_path = "data/insurance_data.csv.txt"
df = load_data(file_path)

# 2. Run the missing values check and print it
print("--- Missing Values ---")
print(missing_values(df))

# 3. Run the descriptive statistics and print it
print("\n--- Descriptive Statistics ---")
print(descriptive_stats(df))