import bs4
import requests

def getAmazonPrice(ProductURL):
    res = requests.get(ProductURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#priceblock_ourprice')
    return elems[0].text

price = getAmazonPrice('https://www.amazon.com/Nutella-26-5-Ounce-Jar-Plastic/dp/B01LZKD7EO/ref=pd_lpo_vtph_325_tr_t_2?_encoding=UTF8&refRID=32MJ8A3X7M8MYDC5MK2W&th=1')
print( ' The price is ' + price)
