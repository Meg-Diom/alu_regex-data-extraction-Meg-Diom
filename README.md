REGULAR EXPRESSION EXTRACTION


PROJECT OVERVIEW

This project is a Python-based data extraction tool that uses Regular Expressions (Regex) to extract different types of information from large amounts of text.

The program can accept data entered manually by the user or read data from a source file.

DATATYPES EXTRACTED

The program extracts the following:

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Time
- HTML tags
- Hashtags
- Currency amounts

HOW IT WORK

The user first chooses how they want to provide the data.

1. Enter data manually
2. Provide a source file

The program then processes the data using predefined Regular Expression patterns and displays the information it finds.

PROJECT STRUCTURE

alu_regex-data-extraction-Meg-Diom/
│
├── main.py
├── extractor.py
├── patterns.py
├── sample_data.txt
└── README.md

FILE DESCRIPTION

main.py
Controls the program and handles user interaction.

extractor.py  
Contains the functions responsible for extracting information from the provided text.

patterns.py  
Contains the Regular Expression patterns used by the extractor functions.

sample_data.txt  
Contains sample bulk data used for testing the program.

README.md  
Contains information about the project and how to use it.

REQUIREMENTS

- Python 3

The project uses Python's built-in re module for Regular Expressions.

HOW TO RUN

Clone the repository and open the project directory.

Run:

python main.py

The program will ask whether you want to enter the data manually or provide a source file.

EXAMPLE

The program can extract information such as:

Email: example@gmail.com
URL: https://example.com
Phone: +237 656 337 111
Time: 14:30
Hashtag: #Python
Currency: $1,500.00

PURPOSE

The purpose of this project is to demonstrate how Regular Expressions can be used in Python to identify and extract useful information from unstructured or bulk text data.

AUTHOR
NGUM DIOM MEG

Created as part of an ALU Regex Data Extraction assignment.
