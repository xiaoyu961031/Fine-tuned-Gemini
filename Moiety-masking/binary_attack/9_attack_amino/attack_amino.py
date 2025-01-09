import pandas as pd
import re

# Function to replace patterns 'O*=C*N', 'C(=O)N', 'N2C(=O)', and '[N]C(=O)'
def replace_extended_patterns_with_missing(row):
    mofid = row['mofid-v1']
    # Patterns to match 'O*=C*N', 'C(=O)N', 'N2C(=O)', and '[N]C(=O)'
    pattern = r'O[\d()]*=C[\d()]*N|C\(=O\)N|N2C\(=O\)|\[N\]C\(=O\)'
    # Replace the first occurrence of the pattern with '<missing>'
    return re.sub(pattern, '<missing>', mofid, count=1)

# Load the CSV file
file_path = 'path_to_your_file/!4c.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Apply the function to the dataset
data['mofid-v1'] = data.apply(replace_extended_patterns_with_missing, axis=1)

# Save the processed dataset
output_path = 'path_to_your_file/modified_4c_replace_extended_patterns.csv'  # Replace with your output path
data.to_csv(output_path, index=False)

print(f"Processed dataset saved to: {output_path}")
