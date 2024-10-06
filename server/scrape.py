import requests
from bs4 import BeautifulSoup
from model import db, Product
from app import app
def scrape_products(search_term):

    #search_term = input('What do you want to scrape ?')
    print(f'Searching for: {search_term}')
    url = f'https://www.jumia.co.ke/catalog/?q={search_term}'
    print(url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, Like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        doc = BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error occured: {err}') 
        return   
    except Exception as err:
        print(f'An error occured: {err}')
        return
    else: 
        product_data = []    
        product_titles = doc.find_all('h3', class_='name') 
        product_prices = doc.find_all('div', class_='prc') 
        product_imgs = doc.find_all('img', class_='img')
    if not product_titles or not product_imgs or not product_prices:
        print('No products found.')
        return 
    
    for title, price, img in zip(product_titles, product_prices, product_imgs):
            img_url = img['data-src'] if 'data-src' in img.attrs else ''
            product_data.append(Product(
                title=title.get_text().strip(),
                price=price.get_text().strip(),
                img_src=img_url
            ))
    with app.app_context():
        db.session.bulk_save_objects(product_data)
        db.session.commit()
    for item in product_data:
        print(f'Title: {item.title}')
        print(f'Price: {item.price}')
        print(f'Image_url: {item.img_src}')
        print("-" * 40)

if __name__ == "__main__":
    search_term = input('What do you want to scrape? ')
    scrape_products(search_term)
   


    