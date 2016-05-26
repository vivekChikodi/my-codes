def query1 (kw):
    str1 = 'http://www.shopping.com/products?KW='+kw
    with urllib.request.urlopen(str1) as response:
       html = response.read()
    soup = BeautifulSoup(html,"html.parser")
    try:
        print (soup.find(class_="numTotalResults").string)
    except AttributeError:
        print ("Sorry there were no matches for:",kw)    
    
def query2(kw,pg):
    str2 = 'http://www.shopping.com/products~PG-'+pg+'?KW='+kw
    with urllib.request.urlopen(str2) as response:
       html = response.read()
    soup = BeautifulSoup(html,"html.parser")
    name = soup.find_all(class_ = "quickLookGridItemFullName hide")
    price = soup.find_all(class_ = "productPrice")
    try:
        for n,p in zip(name,price):
            print ("Product name = ",n.string,'Price = ',p.string)
    except AttributeError:
        print ("Sorry there were no matches for:",kw)    
    

from bs4 import BeautifulSoup
import urllib.request
pg = input('Enter the page number: ')
kw = input('Enter the keyword: ')
query1(kw)
query2(kw,pg)
