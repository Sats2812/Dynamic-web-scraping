from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd
driver=webdriver.Chrome("C:/Users/puroh/Desktop/chromedriver.exe") # Change the path here for where your path for the driver is 
driver.get("https://opensea.io/assets/ens?search[categories][0]=domain-names&search[resultModel]=ASSETS&search[sortAscending]=false&search[sortBy]=LAST_SALE_PRICE")
new=[]
current=[]
last=[]

for i in range(0,5):                #Change the range according to the data required by you for the number of scrolls

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)","return document.documentElement.outerHTML")
    sleep(6)
    soup=BeautifulSoup(driver.page_source,'lxml')
    box=soup.find('div',{'class':'Blockreact__Block-sc-18q9hu0-0 hxevxe AssetsSearchView--assets'})
    all_hackathons =box.find_all('div',{'class': 'Blockreact__Block-sc-18q9hu0-0 hxevxe'})
    for hackathon in all_hackathons:
        h_type=hackathon.find('div',{'class':'AssetCardFooter--name'}).text
        new.append(h_type)
        name=hackathon.find('div',{'class':'Price--amount'}).text
        current.append(name)       
        date=hackathon.find('div',{'class':'Pricereact__DivContainer-t54vn5-0 jsOkdo Price--main'}).text[1:]
        last.append(date)
df = pd.DataFrame(list(zip(new,current,last)),
columns =['Name', 'current','Last'])
df.to_csv("Etherium.csv")
