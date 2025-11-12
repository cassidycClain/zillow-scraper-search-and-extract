thonimport json
import csv

def export_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)