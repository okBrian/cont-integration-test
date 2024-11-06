import json
import hashlib

# Read the raw output from the file
with open("raw_output.txt", "r") as file:
    output = file.read().strip()

# Generate a hash based on the output
output_hash = hashlib.sha256(output.encode()).hexdigest()
file_name = "out.json"

# Write output to JSON with the hash as filename
with open(file_name, "w") as json_file:
    json.dump({
        "name": output_hash,
        "unit": "wow",
        "result": output
    }, json_file)

print(f"::set-output name=file_name::{file_name}")  # Pass the JSON filename back to GitHub Actions
