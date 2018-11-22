from selenium import webdriver
from bs4 import BeautifulSoup as bs

url = 'https://detail.tmall.com/item.htm?'+\
      'spm=a230r.1.14.6.6dfd7a034i9jDW&id=43515741382&cm_id=140105335569ed55e27b&abbucket=4'

chromedriver = r'C:\Users\ynats\AppData\Local\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.implicitly_wait(10)
browser.get(url=url)

html = browser.page_source
soup = bs(html, 'lxml')

for i in soup.select('.tm-rate-fulltxt'):
    print(i.string)
    print()

