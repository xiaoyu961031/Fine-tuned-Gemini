import pandas as pd
import re

# Define the function to replace one instance of the metal in 'mofid-v1' with "<missing>"
def replace_metal_with_missing(row):
    if row['metal'] in row['mofid-v1']:
        # Replace only one occurrence of the metal with "<missing>"
        return re.sub(re.escape(row['metal']), '<missing>', row['mofid-v1'], count=1)
    return row['mofid-v1']

# Load the first dataset
file_path_binary = 'path_to_your_file/!binary.csv'  # Replace with the actual path
binary_data = pd.read_csv(file_path_binary)

# Process the first dataset
binary_data['mofid-v1'] = binary_data.apply(replace_metal_with_missing, axis=1)

# Save the modified first dataset
binary_output_path = 'path_to_your_file/modified_binary.csv'  # Replace with your desired output path
binary_data.to_csv(binary_output_path, index=False)

# Load the second dataset
file_path_4c = 'path_to_your_file/!4c.csv'  # Replace with the actual path
data_4c = pd.read_csv(file_path_4c)

# Process the second dataset
data_4c['mofid-v1'] = data_4c.apply(replace_metal_with_missing, axis=1)

# Save the modified second dataset
data_4c_output_path = 'path_to_your_file/modified_4c.csv'  # Replace with your desired output path
data_4c.to_csv(data_4c_output_path, index=False)

print("Processing complete.")
print(f"Modified binary dataset saved to: {binary_output_path}")
print(f"Modified 4c dataset saved to: {data_4c_output_path}")
