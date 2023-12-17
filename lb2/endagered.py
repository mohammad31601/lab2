import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage
url = "https://www.pagasa.dost.gov.ph/flood#flood-information"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the specified class
    table = soup.find('table', class_='table')

    # Create a CSV file and write the header
    with open('flood_information.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['River Basin', 'Status'])

        # Find all rows in the table body
        rows = table.tbody.find_all('tr')

        # Iterate through each row and extract data
        for row in rows:
            columns = row.find_all(['td', 'th'])
            basin = columns[0].get_text(strip=True)
            status = columns[1].a.get_text(strip=True) if columns[1].a else columns[1].get_text(strip=True)
            csvwriter.writerow([basin, status])

    print("Scraping and CSV creation successful.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
