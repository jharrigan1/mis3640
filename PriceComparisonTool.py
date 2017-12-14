from Costcoprices import getCostcoName 
from Costcoprices import getCostcoPrice
from Walmartprices import getWalmartName   
from Walmartprices import getWalmartPrice   
from Amazonprices import getAmazonName
from Amazonprices import getAmazonPrice


def main():
    itemname = input('Product Name: ')
    curl = "https://www.costco.com/CatalogSearch?dept=All&keyword={itemname}&pageSize=96" .format(itemname=itemname)
    wurl = "https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname)
    aurl = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=srs%3D7301146011%26search-alias%3Dpantry&field-keywords={itemname}" .format(itemname=itemname)
    costconame = getCostcoName(curl)
    costcoprice = getCostcoPrice(curl)
    walmartname = getWalmartName(wurl)
    walmartprice = getWalmartPrice(wurl)
    amazonname = getAmazonName(aurl)
    amazonprice = getAmazonPrice(aurl)
    print( ' Amazon Product Title: ' + amazonname)
    print( ' The Amazon price is $' + amazonprice)
    print(' ')
    print('-------------------------------------------------')
    print( ' Wal-Mart Product Title: ' + walmartname)
    print( ' The Wal-Mart price is $' + walmartprice)
    print(' ')
    print('-------------------------------------------------')
    print( ' Costco Product Title: ' + costconame)
    print( ' The Costco price is $' + costcoprice)
    print(' ')
    print('-------------------------------------------------')

    numamazonprice = float(amazonprice)
    numcostcoprice = float(costcoprice)
    numwalmartprice = float(walmartprice)
    if numamazonprice > numwalmartprice:
        if numwalmartprice > numcostcoprice:
            print("Based on your search of " + itemname + ", Costco sells " + costconame + " at the lowest price of $" + costcoprice + ".")
        else:
            print("Based on your search of " + itemname + ", Wal-Mart sells " + walmartname + " at the lowest price of $" + walmartprice + ".")
    else:
        if numamazonprice > numcostcoprice:
            print("Based on your search of " + itemname + ", Costco sells " + costconame + " at the lowest price of $" + costcoprice + ".")
        else:
            print("Based on your search of " + itemname + ", Amazon sells " + amazonname + " at the lowest price of $" + amazonprice + ".")

main()