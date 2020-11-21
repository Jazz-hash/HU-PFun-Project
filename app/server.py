from flask import Flask, render_template, request
from selectorlib import Extractor
import requests 
import json 

app = Flask(__name__)


e = Extractor.from_yaml_file('selectors/amazonSelector.yml')

def scrape(url):  
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

    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    return e.extract(r.text)


@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/search')
def search_results():
    search = request.args.get('s')
    print(search)
    product = search
    url_amazon = "https://www.amazon.com/s?k=" + product
    full_dict = []
    data_amazon = scrape(url_amazon) 
    if data_amazon:
        for product in data_amazon['products'][:12]:
            product['search_url'] = url_amazon
            full_dict.append(product)
    prices = sorted([float(item["price"][1:].replace(",", "")) for item in full_dict if item["price"]])
    max_price = "${:,.2f}".format(max(prices))
    mid_price = "${:,.2f}".format(prices[len(prices) // 2])
    min_price = "${:,.2f}".format(min(prices))
    print(min_price, max_price, mid_price)

    return render_template('search.htm', search=search, products=full_dict, min_price=min_price, max_price=max_price, mid_price=mid_price)