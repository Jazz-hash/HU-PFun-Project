
# ? imports ( Flask, Selectorlib)
from flask import Flask, render_template, request
from selectorlib import Extractor
import requests 
import json 

# ? Creating app with Flask
app = Flask(__name__)

# ? YML string to grab data from website
# ? Specifying css classes, ids and attributes of text to get from the site.
yml_string = """
products:
    css: 'div[data-component-type="s-search-result"]'
    xpath: null
    multiple: true
    type: Text
    children:
        title:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Text
        url:
            css: 'h2 a.a-link-normal.a-text-normal'
            xpath: null
            type: Link
        rating:
            css: 'div.a-row.a-size-small span:nth-of-type(1)'
            xpath: null
            type: Attribute
            attribute: aria-label
        reviews:
            css: 'div.a-row.a-size-small span:nth-of-type(2)'
            xpath: null
            type: Attribute
            attribute: aria-label
        price:
            css: 'span.a-price:nth-of-type(1) span.a-offscreen'
            xpath: null
            type: Text
"""

# ? Created extractor from YML string with the help of Selectorlib.
e = Extractor.from_yaml_string(yml_string)

# ? Scraping function to make the thing work modular.
def scrape(url):  
    # ? Defining headers to bypass "Are you Robot" verifications.
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # ? Sending request to the url.
    r = requests.get(url, headers=headers)
    # ? Verifying sever response Error with codes.
    if r.status_code > 500:
        return None
    # ? Extrating data from the repsonse obtained from the request.
    return e.extract(r.text)

# ? Index page route.
@app.route('/')
def index():
    # ? rendering htm file.
    return render_template('index.htm')

# ? Search page route.
@app.route('/search')
def search_results():
    # ? getting s (search_query) variable from the url.
    search = request.args.get('s')
    # ? defined url
    url_amazon = "https://www.amazon.com/s?k=" + search
    full_dict = []
    # ? storing data returned from the function.
    data_amazon = scrape(url_amazon) 
    # ? pushing data to dict for better error handling.
    if data_amazon:
        for product in data_amazon['products'][:12]:
            product['search_url'] = url_amazon
            full_dict.append(product)
    prices = sorted([float(item["price"][1:].replace(",", "")) for item in full_dict if item["price"]])
    
    # ? Getting max, mid and min prices from the data.
    max_price = "${:,.2f}".format(max(prices))
    mid_price = "${:,.2f}".format(prices[len(prices) // 2])
    min_price = "${:,.2f}".format(min(prices))
    print(min_price, max_price, mid_price)

    # ? finally rendering everything to the htm file.
    return render_template('search.htm', search=search, products=full_dict, min_price=min_price, max_price=max_price, mid_price=mid_price)