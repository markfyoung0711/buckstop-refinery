import random
from datetime import datetime, timedelta
from src.stage.quality_cases_scheduling import data_structures


# Function to generate sample data based on data structure
def generate_sample_data(data_structure):
    sample_data = {}
    if not isinstance(data_structure, dict):
        print('is not dict')
        import pdb; pdb.set_trace()
    else:
        print('is dict')
    for key, value in data_structure.items():
        if isinstance(value, dict):
            sample_data[key] = generate_sample_data(value)
        elif isinstance(value, list):
            sample_data[key] = [generate_sample_data(item) for item in value]
        elif value == "string":
            sample_data[key] = "Sample " + key
        elif value == "integer":
            sample_data[key] = random.randint(1, 100)
        elif value == "float":
            sample_data[key] = round(random.uniform(0.1, 10.0), 2)
        elif value == "date":
            sample_data[key] = (
                datetime.now() + timedelta(days=random.randint(1, 30))
            ).strftime("%Y-%m-%d")
        elif value == "boolean":
            sample_data[key] = random.choice([True, False])
    return sample_data


# Generate sample data for each data element
sample_data = {}
for key, value in data_structures.items():
    sample_data[key] = generate_sample_data(value)

# Print sample data
for key, value in sample_data.items():
    print(f"\nSample Data for {key}:")
    print(value)
