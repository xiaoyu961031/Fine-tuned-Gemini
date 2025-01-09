import pandas as pd
import re

# Function to replace patterns including 'Nc1c'
def replace_patterns_with_nc1c(row):
    mofid = row['mofid-v1']
    # Extend the pattern to include 'Nc1c' alongside other patterns
    pattern = r'[\d()]*c[\d()]*c[\d()]*N[\d()]*|[\d()]*N[\d()]*c[\d()]*c[\d()]*|[\d()]*N[\d()]*C[\d()]*=C[\d()]*|[\d()]*C[\d()]*=C[\d()]*N[\d()]*|Nc1c'
    # Replace the first occurrence of the pattern with '<missing>'
    return re.sub(pattern, '<missing>', mofid, count=1)

# Load the CSV file
file_path = 'path_to_your_file/!binary.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Apply the function to the dataset
data['mofid-v1'] = data.apply(replace_patterns_with_nc1c, axis=1)

# Save the processed dataset
output_path = 'path_to_your_file/modified_binary_replace_patterns_with_nc1c.csv'  # Replace with your output path
data.to_csv(output_path, index=False)

print(f"Processed dataset saved to: {output_path}")
