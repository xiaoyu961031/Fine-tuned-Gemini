import pandas as pd
import re

# Function to replace one occurrence of halogens [I, F, Cl, Br], including at the start of the string
def replace_halogen_with_missing_refined(row):
    mofid = row['mofid-v1']
    # Replace the first occurrence of any halogen, even at the start of the string
    return re.sub(r'^(I|F|Cl|Br)|\b(I|F|Cl|Br)\b', '<missing>', mofid, count=1)

# Load the CSV file
file_path = 'path_to_your_file/!4c.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Apply the function to the dataset
data['mofid-v1'] = data.apply(replace_halogen_with_missing_refined, axis=1)

# Save the processed dataset
output_path = 'path_to_your_file/new_modified_4c_replace_halogen_refined.csv'  # Replace with your output path
data.to_csv(output_path, index=False)

print(f"Processed dataset saved to: {output_path}")
