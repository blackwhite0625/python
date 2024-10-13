import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('DCF現金流估值模型.xlsx - 工作表1.csv', header=9)

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

# Get all unique non-numeric values from `2025`
non_numeric_values = df[pd.to_numeric(df['2025'], errors='coerce').isna()]['2025'].unique()
if (len(non_numeric_values) > 20):
  # Sample 20 of them if there are too many unique values
  print(f"Non-numeric values in `2025`: {np.random.choice(non_numeric_values, 20, replace=False)}")
else:
  # Otherwise print all unique non-numeric values from `2025`
  print(f"Non-numeric values in `2025`: {non_numeric_values}")

# Remove rows with null values in the `Year` column
df.dropna(subset=['Year'], inplace=True)

# Drop the first column
df.drop(df.columns[0], axis=1, inplace=True)

# Transpose the table, set the first row as header
df_t = df.set_index('Year').T

# Reset the index of the transposed DataFrame
df_t = df_t.reset_index()

# Rename the first column to `Year` and remove the last row
df_t = df_t.rename(columns={'index': 'Year'})[:-1]

# Display the first 5 rows
print(df_t.head().to_markdown(index=False, numalign="left", stralign="left"))

# Fill missing values in `自由現金流`, `終值（Terminal Value）`, and `總和` with 0
df_t['自由現金流'] = df_t['自由現金流'].fillna(0)
df_t['終值（Terminal Value）'] = df_t['終值（Terminal Value）'].fillna(0)
df_t['總和'] = df_t['總和'].fillna(0)

# Convert columns `自由現金流`, `終值（Terminal Value）`, and `總和` to numeric
df_t['自由現金流'] = pd.to_numeric(df_t['自由現金流'], errors='coerce')
df_t['終值（Terminal Value）'] = pd.to_numeric(df_t['終值（Terminal Value）'], errors='coerce')
df_t['總和'] = pd.to_numeric(df_t['總和'], errors='coerce')

# Replace the values in the `Year` column
df_t['Year'] = df_t['Year'].replace({
    '2023': 'FCF Growth',
    '2024': 'Discount Rate',
    '2025': 'Fair Value',
    '2026': 'Market Value'
})

# Display the first 5 rows
print(df_t.head().to_markdown(index=False, numalign="left", stralign="left"))

# Drop columns
df_t = df_t.drop(columns=['FCF Margin', '估值', '企業價值 (EV)', '(+) 現金及其他投資', '(-) 總負債', '股權價值', '流通股數', '股票合理價', '股票當前價格', '安全邊際', '買進 / 賣出'])

# Display the final dataframe
print(df_t.to_markdown(index=False, numalign="left", stralign="left"))