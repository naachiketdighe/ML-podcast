import re

input_file = "data.json"
output_file = "data_preprocessed.json"

with open(input_file, "r") as f:
    content = f.read()

objects = re.findall(r'(\{.*?\})(?=\s*\{|\s*$)', content, re.DOTALL)

# Join with commas and wrap in brackets
json_array = "[\n" + ",\n".join(objects) + "\n]"

with open(output_file, "w") as f:
    f.write(json_array)

print(f"Fixed JSON written to {output_file}")