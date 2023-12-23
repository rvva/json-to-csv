#!/usr/bin/env python3

import json
import csv
import argparse

# Define quoting options and mapping
QUOTING_OPTIONS = {
    'MINIMAL': csv.QUOTE_MINIMAL,
    'ALL': csv.QUOTE_ALL,
    'NONNUMERIC': csv.QUOTE_NONNUMERIC,
    'NONE': csv.QUOTE_NONE
}

def load_json(input_file):
    try:
        with open(input_file, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Input JSON file not found: {input_file}")
        exit(1)

def write_csv(data, output_file, delimiter, quoting):
    fieldnames = data[0].keys()

    with open(output_file, mode='w', newline='') as csv_file:
        try:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=delimiter, quoting=quoting)

            writer.writeheader()

            for row in data:
                writer.writerow(row)
        except csv.Error:
            print("Error: Generating CSV without quoting is not possible for this type of data.")
            print("A character requiring escaping was encountered. Please consider using a quoting option such as 'MINIMAL', 'ALL'.")
            exit(1)

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Convert JSON data to CSV format.')

    # Add command-line arguments
    parser.add_argument('--input', help='Input JSON file', required=True)
    parser.add_argument('--output', help='Output CSV file', required=True)
    parser.add_argument('--delimiter', help='CSV delimiter', default=',')
    parser.add_argument('--quoting', help='CSV quoting method (MINIMAL, ALL, NONNUMERIC, NONE)', default='MINIMAL', choices=QUOTING_OPTIONS.keys())

    # Parse the command-line arguments
    args = parser.parse_args()

    # Load the JSON data
    data = load_json(args.input)

    # Get the quoting option based on the user's choice
    quoting = QUOTING_OPTIONS[args.quoting]

    # Write the data to the CSV file
    write_csv(data, args.output, args.delimiter, quoting)

    print(f"CSV file '{args.output}' has been created with delimiter '{args.delimiter}' and quoting '{args.quoting}'.")

if __name__ == "__main__":
    main()

