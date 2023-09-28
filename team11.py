import time
import pandas as pd
from selenium import webdriver

def readExcel():
    df =pd.read_csv('Amazon Scraping - Sheet1.csv')

    Asin=df['Asin']
    country=df['country']
    return Asin,country

def getUrls(Asins, countries):
    url = "https://www.amazon.{0}/dp/{1}"
    n = len(Asins)
    urls = []
    for i in range(n):
        country = countries[i]
        Asin = Asins[i]
        urls.append(url.format(country, Asin))
    return urls


    

def downloader(url):
    driver=webdriver.Chrome()

    driver.get(url)
    time.sleep(15)
    src=driver.page_source
    driver.quit()
    return src


Asin,country=readExcel()
print(Asin,country)
    

url="https://www.amazon.de/dp/1015"
data=downloadUrl(url)
print(data)
countries, Asins = readExcel()
urls = getUrls(Asins, countries)
print(urls)
    

