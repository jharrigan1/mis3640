import bs4 
import requests

def getWalmartPrice(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.findAll("span", { "class" : "Price-characteristic" })
    elem = soup.findAll("span", { "class" : "Price-mantissa" })
    whole = elems[0].text
    fraction = elem[0].text
    return whole +"." + fraction

def getWalmartName(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.findAll("a", { "class" : "product-title-link" })
    return elems[0].text.strip()
