import json
import hashlib

with open("raw_output.txt", "r") as file:
    output = file.read().strip()

output_hash = hashlib.sha256(output.encode()).hexdigest()
file_name = "out.json"

json_data = [
    {
        "name": output_hash,
        "unit": "Percent",
        "value": int(output)
    }
]

with open(file_name, "w") as json_file:
    json.dump(json_data, json_file, indent=4)
