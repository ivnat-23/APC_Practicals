#1.Extract All Digits from a String

import re
text = input("Enter a string: ")
digits = re.findall(r'\d', text)
print("Digits:", digits)

#2.Display Words Beginning with A or a

import re
text = input("Enter a sentence: ")
words = re.findall(r'\b[Aa]\w*\b', text)
print("Words:", words)

#3.Count Occurrences of Vowels

import re
text = input("Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', text)
print("Number of vowels:", len(vowels))

#4.Extract All Uppercase Letters

import re
text = input("Enter a string: ")
letters = re.findall(r'[A-Z]', text)
print("Uppercase letters:", letters)

#5.Identify Spaces, Tabs, and Newlines

import re
text = "Hello World\tPython\nProgramming"
matches = re.findall(r'[ \t\n]', text)
print("Whitespace characters:", matches)
print("Total:", len(matches))

#6.Replace Multiple Consecutive Spaces with a Single Space

import re
text = input("Enter a string: ")
result = re.sub(r' {2,}', ' ', text)
print("Result:", result)

#7.Display Words Containing Exactly Five Characters

import re
text = input("Enter a sentence: ")
words = re.findall(r'\b[A-Za-z]{5}\b', text)
print("Five-character words:", words)

#8.Identify Words Ending with the Letter s

import re
text = input("Enter a sentence: ")
words = re.findall(r'\b\w+s\b', text, re.IGNORECASE)
print("Words ending with s:", words)

#9.Remove Special Characters

import re
text = input("Enter a string: ")
result = re.sub(r'[^A-Za-z0-9 ]', '', text)
print("Result:", result)

#10.Count the Number of Words in a Sentence

import re
text = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', text)
print("Number of words:", len(words))

#11.Validate a 10-Digit Indian Mobile Number

import re
mobile = input("Enter mobile number: ")
if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

#12.Validate an Email Address

import re
email = input("Enter email address: ")
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
if re.fullmatch(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

#13.Extract Dates in DD-MM-YYYY Format

import re
text = input("Enter a paragraph: ")
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Dates:", dates)

#14.Identify Web Addresses Beginning with HTTP or HTTPS

import re
text = input("Enter text: ")
urls = re.findall(r'https?://[^\s]+', text)
print("Web addresses:", urls)

#15.Extract Hashtags from a Social Media Post

import re
text = input("Enter a social media post: ")
hashtags = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text)
print("Hashtags:", hashtags)

#16.Validate Password Strength

import re
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])\S{8,}'
if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")

#17.Identify Consecutive Repeated Words Ignoring Case

import re
text = input("Enter a sentence: ")
pattern = r'\b(\w+)\s+\1\b'
words = re.findall(pattern, text, re.IGNORECASE)
print("Repeated words:", words)

#18.Extract Six-Digit Indian PIN Codes

import re
text = input("Enter a paragraph: ")
pins = re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', text)
print("PIN codes:", pins)

#19.Validate an Indian Vehicle Registration Number

import re
number = input("Enter vehicle number: ").upper()
pattern = r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}'
if re.fullmatch(pattern, number):
    print("Valid format")
else:
    print("Invalid format")

#20.Extract File Extensions from Filenames

import re
text = input("Enter filenames: ")
extensions = re.findall(r'\.([A-Za-z0-9]+)\b', text)
print("File extensions:", extensions)

#21.Remove HTML Tags, Extra Whitespace, and Punctuation

import re
text = "<p>Hello!!!   World,   Python.</p>"
text = re.sub(r'<[^>]*>', '', text)
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

print("Clean text:", text)

#22.Extract Invoice Numbers, Dates, and Monetary Amounts

import re
text = """
Invoice No: INV-12345
Date: 16-10-2026
Amount: Rs. 12500.50
"""
invoice = re.findall(r'INV-\d+', text)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'Rs\.?\s*[\d,]+(?:\.\d{2})?', text)
print("Invoice Number:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)

#23.Identify Single-Line Comments in Python Source Code

import re
code = """
# This is a comment
x = 10  # Assigning value
"""
pattern = r'^\s*#.*|(?<=\s)#.*'
comments = re.findall(pattern, code, re.MULTILINE)
print("Comments:")
for comment in comments:
    print(comment.strip())

#24.Validate Product Codes in ABC-1234-XY Format

import re
code = input("Enter product code: ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")

#25.Extract Student Names, Roll Numbers, and Marks

import re
text = """
Name: Rahul, Roll: 101, Marks: 85
Name: Priya, Roll: 102, Marks: 92
"""
pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
students = re.findall(pattern, text)
for name, roll, marks in students:
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print()

#26.Extract DOI, Publication Years, Email Addresses, and URLs

import re

text = """
Research paper (2024)
DOI: 10.1234/abc.5678
Email: author@example.com
URL: https://example.com/paper
"""
doi = re.findall(r'\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text
)
urls = re.findall(r'https?://[^\s]+', text)
print("DOI:", doi)
print("Publication Years:", years)
print("Email Addresses:", emails)
print("URLs:", urls)
