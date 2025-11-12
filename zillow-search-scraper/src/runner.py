thonimport requests
import json
from extractors.zillow_parser import parse_zillow_listing
from outputs.exporters import export_to_json, export_to_csv
from config.settings import PROXY, USER_AGENT

def fetch_data(query, location, output_format='json'):
    url = f"https://www.zillow.com/homes/{query}_{location}"
    headers = {
        'User-Agent': USER_AGENT,
    }
    proxies = {
        'http': PROXY,
        'https': PROXY
    }

    response = requests.get(url, headers=headers, proxies=proxies)
    listings = parse_zillow_listing(response.text)

    if output_format == 'json':
        export_to_json(listings, 'sample_output.json')
    elif output_format == 'csv':
        export_to_csv(listings, 'sample_output.csv')

    return listings

if __name__ == "__main__":
    query = 'apartments'
    location = 'San-Francisco'
    fetch_data(query, location)