import pandas as pd
import re

# Function to replace 'O=C*' and 'C*=O' with '<missing>'
def replace_o_equals_c_star_and_c_star_equals_o_with_missing(row):
    mofid = row['mofid-v1']
    # Pattern to match 'O=C*' and 'C*=O' where * can be digits, '(', ')', or a combination
    pattern = r'O=C[\d()]*|C[\d()]*=O'
    # Replace the first occurrence of the pattern with '<missing>'
    return re.sub(pattern, '<missing>', mofid, count=1)

# Load the CSV file
file_path = 'path_to_your_file/!4c.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Apply the function to the dataset
data['mofid-v1'] = data.apply(replace_o_equals_c_star_and_c_star_equals_o_with_missing, axis=1)

# Save the processed dataset
output_path = 'path_to_your_file/modified_4c_replace_o_equals_c_star_and_c_star_equals_o.csv'  # Replace with your output path
data.to_csv(output_path, index=False)

print(f"Processed dataset saved to: {output_path}")
