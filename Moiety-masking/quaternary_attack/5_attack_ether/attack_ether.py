import pandas as pd
import re

# Function to replace the specified patterns with '<missing>'
def replace_co_and_extended_variants_with_missing(row):
    mofid = row['mofid-v1']
    # Replace the first occurrence of 'CO', 'C*O', 'cO', 'Oc*', 'c*O', 'OC*', or 'O*C'
    mofid = re.sub(r'CO|C[\d()]*O|cO|Oc[\d()]*|c[\d()]*O|OC[\d()]*|O[\d()]*C', '<missing>', mofid, count=1)
    return mofid

# Load the CSV file
file_path = 'path_to_your_file/!binary.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Apply the function to the dataset
data['mofid-v1'] = data.apply(replace_co_and_extended_variants_with_missing, axis=1)

# Save the processed dataset
output_path = 'path_to_your_file/new_modified_binary_replace_co_and_extended_variants.csv'  # Replace with your output path
data.to_csv(output_path, index=False)

print(f"Processed dataset saved to: {output_path}")
