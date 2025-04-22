import pandas as pd
import re

# Function to replace 'n' unless immediately followed by ']'
def replace_lowercase_n_with_missing_ignore_right_bracket(row):
    mofid = row['mofid-v1']
    # Replace 'n' unless it is immediately followed by ']'
    return re.sub(r'n(?!\])', '<missing>', mofid, count=1)

# Load the CSV file
file_path = 'path_to_your_file/!4c.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Apply the function to the dataset
data['mofid-v1'] = data.apply(replace_lowercase_n_with_missing_ignore_right_bracket, axis=1)

# Save the processed dataset
output_path = 'path_to_your_file/new_modified_4c_ignore_right_bracket.csv'  # Replace with your output path
data.to_csv(output_path, index=False)

print(f"Processed dataset saved to: {output_path}")
