import json
import random

# Generate a random number between 0 and 100
random_value = random.randint(0, 100)

# Define the JSON structure
data = [
    {
        "name": "My Custom Smaller Is Better Benchmark - CPU Load",
        "unit": "Percent",
        "value": random_value
    },
    {
        "name": "hallo",
        "unit": "asd",
        "value": random_value % 50
    }
]
  
# Write to a JSON file
with open('benchmark.json', 'w') as f:
    json.dump(data, f, indent=4)