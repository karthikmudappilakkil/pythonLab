import requests
from bs4 import BeautifulSoup
import csv

# Get website content
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find headlines
headlines = soup.find_all("span", class_="titleline")

# Create CSV file
file = open("news.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)

# Write heading
writer.writerow(["Headline", "Date", "Category"])

# Extract news details
for news in headlines:
    headline = news.get_text()

    date = "Not available"
    category = "Technology"

    print("Headline:", headline)
    print("Date:", date)
    print("Category:", category)

    writer.writerow([headline, date, category])

# Close file
file.close()

print("Data saved to news.csv")