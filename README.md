URL Extractor
=============

This Python script is designed to extract URLs from a given input text and store them in a CSV file. It provides functions to parse input data, extract URLs using regular expressions, and write the extracted URLs to a CSV file.

Features
--------

-   Extracts URLs from input text data.
-   Supports various types of URLs with different top-level domains.
-   Outputs the extracted URLs to a CSV file.

How to Use
----------

### 1\. Installation

No installation is required as this is a standalone Python script. However, ensure you have Python installed on your system.

### 2\. Usage

1.  Prepare Input Data: Place your text data containing URLs in a the file named `input_data.txt`. 

2.  Run the Script: Execute the script `python url_extractor.py`. It will read the input data, extract URLs, and save them in a CSV file.

4.  Output: The extracted URLs will be displayed on the console, and a CSV file containing the URLs will be generated in the same directory. The CSV file name will be in the format `filtered_urls_<timestamp>.csv`, where `<timestamp>` is the current date and time.

### 3\. Example

Suppose `input_data.txt` contains the following text:

`Visit our website at www.example.com or check out our blog at blog.test.org.`

Running the script will produce the following output:

`Filtered URLs: ['www.example.com', 'blog.test.org']
Output written to: filtered_urls_<timestamp>.csv`

A CSV file named `filtered_urls_<timestamp>.csv` will be created with the following content:

`www.example.com,
blog.test.org,`
