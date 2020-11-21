from flask import Flask, render_template, request
from scrapper.amazon import scrape
import json

app = Flask(__name__)


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