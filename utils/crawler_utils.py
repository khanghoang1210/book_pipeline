import requests
from bs4 import BeautifulSoup


def crawl_data(url):
    book_info = []
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')
    ol = soup.find("ol")
    articles = ol.find_all("article", {'class': "product_pod"})    


    for article in articles:
        book_item = {}
        img = article.find('img')
        book_item['book_name']= img.attrs['alt']
        star = article.find('p')['class']
        book_item['star'] = star[1]
        book_item['price'] = article.find('p',{'class':'price_color'}).text[2:]
        status = article.find('p',{'class':'instock'}).text
        book_item['status'] = status.replace(" ","").replace("\n","")
        img_link = img.attrs['src'][2:]
        book_item['poster_link'] = url[:26] + img_link
        book_info.append(book_item)
    return book_info
