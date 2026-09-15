import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://scrapifydatalabs.com/playground/nestly/"

# Step 1: Get webpage
response = requests.get(url)

# Check connection
print("Status Code:", response.status_code)

# Step 2: Create BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all property cards
cards = soup.select("article.nl-card[data-home-id]")

print("Properties found:", len(cards))

# Step 4: Create CSV file
with open("properties.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # CSV headings
    writer.writerow(["Property Title", "Price", "Location"])

    # Step 5: Extract data from each card
    for card in cards:

        # Get all text from the card
        lines = card.get_text("\n", strip=True).split("\n")

        # Property title
        title = lines[0]

        # Property price
        price = card.select_one(".nl-price[data-price]").get_text(strip=True)

        # Property location
        location = card.find("a").get_text(strip=True)

        # Save to CSV
        writer.writerow([title, price, location])

        # Display on screen
        print("Title:", title)
        print("Price:", price)
        print("Location:", location)
        print("-------------------------")

print("Data saved successfully to properties.csv")
