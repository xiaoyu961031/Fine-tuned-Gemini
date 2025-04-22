import pandas as pd
import re

# Function to replace 'C=N', 'N=C', 'C*=N*', or 'N*=C*' with '<missing>'
def replace_c_star_equals_n_star_with_missing(row):
    mofid = row['mofid-v1']
    # Replace the first occurrence of 'C=N', 'N=C', 'C*=N*', or 'N*=C*'
    return re.sub(r'C[\d()]*=N[\d()]*|N[\d()]*=C[\d()]*', '<missing>', mofid, count=1)

# Load the CSV file
file_path = 'path_to_your_file/!4c.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Apply the function to the dataset
data['mofid-v1'] = data.apply(replace_c_star_equals_n_star_with_missing, axis=1)

# Save the processed dataset
output_path = 'path_to_your_file/modified_4c_replace_c_star_n_star.csv'  # Replace with your output path
data.to_csv(output_path, index=False)

print(f"Processed dataset saved to: {output_path}")
