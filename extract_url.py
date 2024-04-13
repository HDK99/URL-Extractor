import re
import csv
from datetime import datetime


def extract_urls_from_line(line):
    # Regular expression to match URLs
    url_pattern = r'\b(?:www\.)?[\w-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?\b'
    urls = re.findall(url_pattern, line)
    return urls

def extract_urls_from_data(input_data):
    urls = []
    # Split input data into lines and extract URLs from each line
    for line in input_data.split('\n'):
        urls.extend(extract_urls_from_line(line))
    return urls

def write_urls_to_csv(urls, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for url in urls:
            writer.writerow([url, ''])  # Add description in the empty string, or remove if CSV format doesn't require two columns 

with open('input_data.txt', 'r') as file:
    input_data = file.read()

urls = extract_urls_from_data(input_data)

# Generate timestamp for filename to avoid overwriting
timestamp = datetime.now().strftime('%Y%m%d%H%M')

output_file = f'filtered_urls_{timestamp}.csv'

write_urls_to_csv(urls, output_file)

print("Filtered URLs:", urls)
print("Output written to:", output_file)
