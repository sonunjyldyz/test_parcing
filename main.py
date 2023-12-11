from bs4 import BeautifulSoup as BS
import requests 

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_data(html):
    soup = BS(html, 'html.parser')
    container = soup.find('div', class_= 'container body-container')
    main = container.find('div', class_ = 'main-content')
    wrapper = main.find('div', class_ = 'listings-wrapper')
    post = wrapper.find_all('div', class_ = 'listing')
    for i in post:
        left_side = i.find('div', class_ = 'left-side') 
        title = left_side.find('p', class_ = 'title')
        address = left_side.find('div', class_ = 'address')
        link = left_side.find('a').get('href')
        full_link = f'https://www.house.kg{link}' 
        right_side = i.find('div', class_ = 'right-side')
        price = right_side.find('div', class_ = 'price')
        price_addition= right_side.find('div', class_ = 'price-addition')
        description = i.find('div', class_ = 'description')
        span = i.find('div', class_ = 'description')

        # print(description.text.strip())
        # if span == None:
        #     print('Нет подробностей об объявлении')
        # else:
        #     print(span.text.strip())

        
        # info = i.find('div', class_ = 'additional-info').find('div', class_ = 'left-side')
        # view = info.find('span', {"data-placement":"top"}).text.strip()
        # blank = []
        # blank.append(view)
        # print(f'Просмотров: {sorted(blank)}') 

        

        # print(info.text.strip())


        # print(price_addition.text.strip())
        # print(price.text.strip())
      
        
        # print(full_link)

        
        # print(title.text.strip())
        # print(address.text.strip())


    
def main():
    URL = 'https://www.house.kg/kupit-uchastok?region=1&town=2&sort_by=upped_at+desc'
    html = get_html(URL)
    get_data(html)


if __name__ == '__main__':
    main() 
