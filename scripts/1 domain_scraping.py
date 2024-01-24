import pandas as pd
import requests
import os
import re
import csv
from zipfile import ZipFile
import zipfile
import json
from collections import defaultdict
from bs4 import BeautifulSoup
from json import dump
from urllib.request import urlopen



# built-in imports
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
# constants
BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 5) # update this to your liking
Postcode = range(3000, 4000)

USER_AGENT = 'Mozilla/5.0'
session = requests.Session()
session.headers.update({'User-Agent': USER_AGENT})

########################################  domain website scraping  ########################################
# begin code
url_links = []
property_metadata = defaultdict(dict)
# generate list of urls to visit
for postcode in Postcode:
    #url = BASE_URL + f"/rent/melbourne-region-vic/?sort=price-desc&page={page}"
    print(f"Processing postcode {postcode}...")

    url = BASE_URL + f"/rent/?excludedeposittaken=1&postcode={postcode}"
    for page in N_PAGES:  # Loop through pages 1 to 15
        url = BASE_URL + f"/rent/?excludedeposittaken=1&postcode={postcode}&page={page}"
        response = requests.get(url, headers=headers)
        bs_object = BeautifulSoup(requests.get(
            url, headers=headers).text, "html.parser")
    # find the unordered list (ul) elements which are the results, then
    # find all href (a) tags that are from the base_url website.
        try:
            index_links = bs_object \
            .find(
                "ul",
                {"data-testid": "results"}
            ) \
            .findAll(
                "a",
                href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
            )
            for link in index_links:
            # if its a property address, add it to the list
                if 'address' in link['class']:
                    url_links.append(link['href'])
        except AttributeError:
            pass
    print(f"finish postcode {postcode}...")
    
    
# for each url, scrape some basic metadata
for property_url in url_links[1:]:
    bs_object = BeautifulSoup(session.get(property_url).text, "html.parser")
        
    try: 
        # looks for the header class to get property name
        property_metadata[property_url]['name'] = bs_object \
            .find("h1", {"class": "css-164r41r"}) \
            .text

        # looks for the div containing a summary title for cost
        property_metadata[property_url]['cost_text'] = bs_object \
            .find("div", {"data-testid": "listing-details__summary-title"}) \
            .text

        # get rooms and parking
        rooms = bs_object \
            .find("div", {"data-testid": "property-features"}) \
            .findAll("span", {"data-testid": "property-features-text-container"})
            

        # rooms
        property_metadata[property_url]['rooms'] = [
            re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Bed' in feature.text or 'Bath' in feature.text
        ]

        # parking
        property_metadata[property_url]['parking'] = [
            re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Parking' in feature.text
        ]

        # Extract coordinates from the href attribute
        coord_match = re.search(r'destination=([-\s,\d\.]+)', bs_object\
            .find("a", {"target": "_blank", 'rel': "noopener noreferrer"})\
            .get('href'))

        if coord_match:
            # Split and convert coordinates to floats
            coordinates = [float(coord) for coord in coord_match.group(1).split(',')]
            property_metadata[property_url]['coordinates'] = coordinates
        else:
            # Handle the case where the regular expression did not match
            property_metadata[property_url]['coordinates'] = []  # or handle the error appropriately

            
        property_metadata[property_url]['desc'] = re \
            .sub(r'<br\/>', '\n', str(bs_object.find("p"))) \
            .strip('</p>')
            
            

    except AttributeError:
        continue

# output to example json in data/raw/
with open('../data/raw/domain.json', 'w') as f:
    dump(property_metadata, f)