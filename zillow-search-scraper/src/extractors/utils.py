thonimport re

def clean_price(price_str):
    return re.sub(r'\D', '', price_str)

def clean_address(address_str):
    return ' '.join(address_str.split())