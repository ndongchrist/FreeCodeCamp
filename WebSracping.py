import time
from bs4 import BeautifulSoup
from requests import request
def find_books():
    html_text = request.get('https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html').text
    #print(html_text.text)
    soup = BeautifulSoup(html_text,'lxml')
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for book in books:
        name = book.find('h3').text
        Available = book.find('p', class_='instock availability').text
        price = book.find('p', class_='price_color').text.replace('Â£','$')
        
        print(f'Book Name: {name}')
        print(f'Price: {price}')
        print(f'Availability: {Available}')


if __name__ == '__main__':
    while True:
        find_books()
        time.sleep(5)



