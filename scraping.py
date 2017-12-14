import bs4
import requests

def getAmazonPrice(ProductURL):
    res = requests.get(ProductURL)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#priceblock_ourprice')
    return elems [0].text.strip()


price = getAmazonPrice('https://www.amazon.com/Nutella-Hazelnut-Spread-13-Oz/dp/B0014E84TK/ref=sr_1_4_s_it?ie=UTF8&qid=1512400582&sr=1-4&keywords=nutella')
print( ' The price is ' + price)