from selectorlib import Extractor
import requests 
import json 

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

# with open('results/search_results_amazon.json','w') as outfile:
#     product = "note+20"
#     url = "https://www.amazon.com/s?k=" + product
#     data = scrape(url) 
#     full_dict = []
#     if data:
#         for product in data['products'][:5]:
#             product['search_url'] = url
#             print("Saving Product: %s"%product['title'])
#             full_dict.append(product)
#             json.dump(product,outfile)
#             outfile.write("\n")
#     print(full_dict)
        
    