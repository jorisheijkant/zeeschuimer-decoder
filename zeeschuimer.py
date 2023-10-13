# This is the actual script that converts the data into csv
import sys
import json
import csv

# Import the different parsers
from parsers.tiktok import parse_tiktok
from parsers.twitter import parse_twitter

# Get the arguments provided to the script as terminal arguments
provided_file = sys.argv[1]
provided_type = False

# Check if there is a second argument, if so, use it as type
if(len(sys.argv) > 2):
    provided_type = sys.argv[2]

def convert_zeeschuimer(file, type="tiktok"):
    print(f"Converting {file} to csv, type is {type}")

    # Set up data array
    structured_data = []

    with open(file, 'r') as file_to_read:
        for line in file_to_read:
            data = json.loads(line)
            structured_data.append(data)

    print(f"Read {len(structured_data)} lines from {file}")

    parsed_items = []

    for index, item in enumerate(structured_data):
        parsed_item = {}
        if(type == "tiktok"):
            parsed_item = parse_tiktok(item, index)
        elif(type == "twitter"):
            parsed_item = parse_twitter(item, index)

        parsed_items.append(parsed_item)

    print(f"Parsed {len(parsed_items)} items")

    # Get filename without extension, by chopping off the last 7 characters (.ndjson)
    file_without_ext = file[:-7]
    outfile = f"{file_without_ext}.csv"

    # Write to csv
    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=parsed_items[0].keys())
        writer.writeheader()
        for data in parsed_items:
            writer.writerow(data)

    print(f"Wrote csv to {outfile}")

# Check if there is a file and a type provided, and the file contains .ndjson
if(provided_file and provided_type and provided_file.endswith(".ndjson")):
    convert_zeeschuimer(provided_file, provided_type)
elif(provided_file and provided_file.endswith(".ndjson")):
    convert_zeeschuimer(provided_file)
else:
    print("Please provide a valid ndjson file")