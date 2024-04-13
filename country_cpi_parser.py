from bs4 import BeautifulSoup
import csv

# Load the HTML content from the file
with open('cpi.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all list items containing country information
country_items = soup.find_all('li')

# Initialize a list to store country dictionaries
countries = []

# Iterate through each country item
for item in country_items:
    # Extract the score
    score = item.find('span', class_='font-bold').text.strip()
    # Extract the country name
    country = item.find('span', class_='flex-1 truncate pr-2').text.strip()
    # Create a dictionary for the country
    country_dict = {'country': country, 'score': score}
    # Append the dictionary to the list
    countries.append(country_dict)

# Define the file name for the CSV
csv_file = 'countries.csv'

# Define the field names for the CSV
field_names = ['country', 'score']

# Write the country list to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)

    # Write the header row
    writer.writeheader()

    # Write each country as a row in the CSV file
    for country in countries:
        writer.writerow(country)

print(f"Country list has been written to {csv_file}")
