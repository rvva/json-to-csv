# General information
Python script that converts JSON to CSV format. 

# Usage
<pre>
$ python3 json-to-csv.py -h
usage: json-to-csv.py [-h] --input INPUT --output OUTPUT [--delimiter DELIMITER] [--quoting {MINIMAL,ALL,NONNUMERIC,NONE,NOTNULL,STRINGS}]

Convert JSON data to CSV format.

options:
  -h, --help            show this help message and exit
  --input INPUT         Input JSON file
  --output OUTPUT       Output CSV file
  --delimiter DELIMITER
                        CSV delimiter
  --quoting {MINIMAL,ALL,NONNUMERIC,NONE,NOTNULL,STRINGS}
                        CSV quoting method (MINIMAL, ALL, NONNUMERIC, NONE, NOTNULL, STRINGS)
</pre>

## Basic use
1. Clone repository
<pre>
git clone https://github.com/rvva/json-to-csv
</pre>
2. Run script with python3.
<pre>
python3 json-to-csv.py --input source.json --output converted.csv
</pre>

## Advanced use
### Delimiter
The script according to RFC 4180 uses a comma as a separator by default. 
If you want to use a different spearator, use the delimeter switch. 
<pre>
python3 json-to-csv.py --input source.json --output converted.csv --delimiter ';'
</pre>
### Quoting
<p>According to the RFC 4180, fields that contain a special character (comma, CR, LF or double quotation marks) must be "avoided" by enclosing them in double quotation marks (Hex 22).</p>
<p>By default, the script runs in MINIMAL mode, which means that only fields containing a special character will be enclosed in double quotes.</p>

Avalaible options:

+ QUOTE_ALL - quote all fields
+ NONNUMERIC - quote all non-numeric fields
+ NONE - never quote fields
+ NOTNULL - quote all fields which are not None.
+ STRINGS -  always place quotes around fields which are strings. This is similar to QUOTE_NONNUMERIC, except that if a field value is None an empty (unquoted) string is written.

More information about quoting: https://docs.python.org/3/library/csv.html

Examples:
<pre>
python3 python3 json-to-csv.py --input source.json --output converted.csv --quoting ALL
python3 python3 json-to-csv.py --input source.json --output converted.csv --quoting NOTNULL
</pre>
