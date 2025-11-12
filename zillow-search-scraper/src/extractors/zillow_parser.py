thonfrom bs4 import BeautifulSoup

def parse_zillow_listing(html):
    soup = BeautifulSoup(html, 'html.parser')
    listings = []

    for item in soup.find_all('li', class_='search-results'):
        try:
            price = item.find('span', class_='price').text.strip()
            address = item.find('address').text.strip()
            detail_url = item.find('a', class_='listing-link')['href']
            latlong = item.get('data-latlong', None)
            status = item.find('span', class_='status').text.strip()
            beds = item.find('span', class_='beds').text.strip()
            baths = item.find('span', class_='baths').text.strip()
            area = item.find('span', class_='area').text.strip()

            listings.append({
                'price': price,
                'address': address,
                'detailUrl': detail_url,
                'latLong': latlong,
                'status': status,
                'beds': beds,
                'baths': baths,
                'area': area
            })
        except AttributeError:
            continue

    return listings