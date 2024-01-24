import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://localfoodconnect.org.au/links/national-parks-in-victoria/"


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

script_texts = soup.find_all('script', type='text/javascript')

for script_text in script_texts:
    if script_text.string and 'markers' in script_text.string:
        json_str = script_text.string
        pattern = r'markers\s*:\s*(\[[\s\S]*\])'
        matches = re.findall(pattern, json_str, re.DOTALL)

        for match in matches:
            markers_data = match.strip()
            markers_list = json.loads(markers_data)

        
            extracted_data = []

            for marker in markers_list:
                title = marker.get('title')
                latitude = marker.get('latitude')
                longitude = marker.get('longitude')

        
                extracted_data.append({
                    "title": title,
                    "latitude": latitude,
                    "longitude": longitude
                })


with open('../data/landing/parks.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_data, f, ensure_ascii=False, indent=4)