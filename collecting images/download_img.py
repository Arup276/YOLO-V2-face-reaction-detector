from selenium import webdriver
import os
import ast
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup

driver = webdriver.Chrome("chromedriver.exe")

url = 'https://www.google.com/search?rlz=1C2CHZL_enIN799IN815&biw=1366&bih=657&tbm=isch&sa=1&ei=qAqWXN-BD4HHvgSGhKOABA&q=sad+people+faces&oq=sad+people+faces&gs_l=img.3..0j0i8i30l2.8855278.8866576..8867376...4.0..0.405.2885.2-5j2j2......0....1..gws-wiz-img.......0i7i30j0i7i5i30j0i8i7i30j0i67.eAaFlHk83vc'

directory = 'sad'

def find_urls(url):
    driver.get(url)
    wait = input('lol...')
    page = driver.page_source

    soup = Soup(page,'lxml')
    urls = soup.find_all('div',{'class':'rg_meta notranslate'})

    all_urls = []
    for i in urls:
        link = i.text
        link = ast.literal_eval(link)['ou']
        #print(link)
        all_urls.append(link)
    return all_urls

URLs = find_urls(url)

def save_img(url,directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i,link in enumerate(url):
        path = os.path.join(directory,'{:06}.jpg'.format(i))
        try:
            ulib.urlretrieve(link,path)
        except:
            print('Failed: ')

save_img(URLs,directory)
