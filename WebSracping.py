import time
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html').text
print(html_text)
soup = BeautifulSoup(html_text,'lxml')
books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for book in books:
    name = book.find('h3').text
    Available = book.find('p', class_='instock availability').text
    price = book.find('p', class_='price_color').text.replace('Â£','$')
    
    #print(f'Book Name: {name}')
    #print(f'Price: {price}')
    #print(f'Availability: {Available}')






