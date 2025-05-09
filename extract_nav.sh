#!/bin/bash

# Download the data
curl -s https://www.amfiindia.com/spages/NAVAll.txt -o nav_raw.txt

# Filter lines that contain data (skip headers/empty lines), extract Scheme Name and NAV, and output as TSV
awk -F ';' 'NF > 5 && $1 ~ /^[0-9]+$/ { print $4 "\t" $5 }' nav_raw.txt > nav_data.tsv

echo "✅ Extracted Scheme Name and NAV to nav_data.tsv"
