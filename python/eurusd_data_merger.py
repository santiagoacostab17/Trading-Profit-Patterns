import pandas as pd
import glob
import os

# -----------------------------
# 1️⃣ Set the path to your CSV files
# -----------------------------
# Change 'data/' to the folder where your CSVs are located
csv_path = 'data/*.csv'

# List all CSV files in the folder
csv_files = glob.glob(csv_path)
print(f"{len(csv_files)} files found:")
for f in csv_files:
    print(f)

# -----------------------------
# 2️⃣ Read and combine all CSVs
# -----------------------------
dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames into one
full_df = pd.concat(dfs, ignore_index=True)
print(f"\nCombined DataFrame created with {full_df.shape[0]} rows and {full_df.shape[1]} columns.")

# -----------------------------
# 3️⃣ (Optional) Convert date and time
# -----------------------------
# Change column names according to your CSV
print("Original columns:")
print(list(full_df.columns))
full_df = full_df.drop(columns=['Volume'])
full_df.columns = ["datetime","open","high","low","close"]  # replace all column names
full_df = full_df.sort_values("datetime").reset_index(drop=True)
print("Final columns:")
print(list(full_df.columns))

# -----------------------------
# 4️⃣ Save the final DataFrame to CSV
# -----------------------------
output_file = 'EURUSD_1m_complete.csv'
full_df.to_csv(output_file, index=False)  # index=True if you want to keep Datetime as index
print(f"\nFinal file saved as: {os.path.abspath(output_file)}")
