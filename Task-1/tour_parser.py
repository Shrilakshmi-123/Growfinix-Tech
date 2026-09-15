import argparse
import re


# -------------------------------
# STEP 1: Command Line Arguments
# -------------------------------

parser = argparse.ArgumentParser(
    description="Tour Enquiry Log Parser"
)

parser.add_argument(
    "file",
    help="Path of the tour enquiry text file"
)

args = parser.parse_args()


# -------------------------------
# STEP 2: Read the input file
# -------------------------------

try:
    with open(args.file, "r", encoding="utf-8") as file:
        text = file.read()

except FileNotFoundError:
    print("Error: File not found.")
    exit()


# -------------------------------
# STEP 3: Regular Expressions
# -------------------------------

# Find email addresses
email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

# Find names after Name/Name:
name_pattern = r'(?i)(?:name|customer|client)\s*[:=-]\s*([A-Za-z ]+)'

# Find destinations after Destination/Place/Travel to
destination_pattern = (
    r'(?i)(?:destination|place|travel\s*to|trip\s*to)'
    r'\s*[:=-]\s*([A-Za-z ]+)'
)


# -------------------------------
# STEP 4: Extract information
# -------------------------------

emails = re.findall(email_pattern, text)
names = re.findall(name_pattern, text)
destinations = re.findall(destination_pattern, text)


# -------------------------------
# STEP 5: Display clean summary
# -------------------------------

print("\n======================================")
print("       TOUR ENQUIRY LOG PARSER")
print("======================================")

total = max(len(names), len(emails), len(destinations))

if total == 0:
    print("No enquiries found.")
else:

    for i in range(total):

        name = names[i].strip() if i < len(names) else "N/A"
        email = emails[i].strip() if i < len(emails) else "N/A"
        destination = (
            destinations[i].strip()
            if i < len(destinations)
            else "N/A"
        )

        print(f"\nEnquiry {i + 1}")
        print("-------------------------")
        print("Name        :", name)
        print("Email       :", email)
        print("Destination :", destination)

print("\n======================================")
print("Parsing completed successfully!")
print("======================================")
