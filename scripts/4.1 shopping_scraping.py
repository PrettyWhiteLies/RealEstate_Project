import requests
from bs4 import BeautifulSoup
import csv
import re  

url = 'https://www.australia-shoppings.com/malls-centres/victoria'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Define a regular expression pattern to extract GPS coordinates from mall information
gps_pattern = r'GPS:\s*(-?\d+\.\d+),\s*(-?\d+\.\d+)'

# Create a CSV file for writing mall coordinates
with open('../data/landing/mall_coordinates.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Mall Name', 'Longitude', 'Latitude']) 

    
    malls_list = soup.find('ul', class_='malls-list')

    # Iterate through each mall in the list
    for mall in malls_list.find_all('li'):

        # Extract the mall name from the <h3> element
        mall_name = mall.find('h3', class_='tit').find('a').text

        # Extract the mall information from the <p> element
        mall_info = mall.find('p', class_='st').text
        
        match = re.search(gps_pattern, mall_info)
        
        # If GPS coordinates are found, extract and write them to the CSV file
        if match:
            latitude, longitude = map(float, match.groups())
            csv_writer.writerow([mall_name, longitude, latitude])
        else:
            print(f"Skipping '{mall_name}' due to missing or invalid GPS information")

print("Data has been written to 'mall_coordinates.csv'.")