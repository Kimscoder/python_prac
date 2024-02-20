from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

def MemodeCafe_store(result):
    MemodeCafe_url  = "https://www.mmthcoffee.com/sub/store.html"
    wd = webdriver.Chrome('./chromedriver.exe')
    
   
    wd.get(MemodeCafe_url)
    time.sleep(3)
  
    wd.execute_script("goSearch()")
    time.sleep(3)
    html = wd.page_source
    soupCB = BeautifulSoup(html,'html.parser')
    store_info = soupCB.select("div.right > ul > li")
 
    for store_li in store_info:
        store_name = store_li.select("a div.txt_w div.tit strong")[0].string
        store_address = store_li.select("a div.txt_w div.txt p")[0].string.replace("주소 : ","")
        
        print(store_name,store_address)
        
        result.append([store_name]+[store_address])

def main():
    result = []
    print('MemodCafe store crawling >>>>>>>>>>>>')
    MemodeCafe_store(result)
    
    CB_tbl = pd.DataFrame(result, columns=('store','address'))
    CB_tbl.to_csv('./MemodCafe.csv', encoding= 'cp949', mode = 'w',index=True)        
if __name__ == '__main__':
    main()
