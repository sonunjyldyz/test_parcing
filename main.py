from bs4 import BeautifulSoup as BS
import requests 
import openpyxl   # для сохранение в эксель.
from openpyxl import Workbook
import csv

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def view_sort(view):
    view_list = []
    for i in view:
        sorted(view_list.append(i.text.strip())) 
    return view_list 


def get_post_link(html):
    soup = BS(html, 'html.parser')
    links = []
    container = soup.find('div', class_= 'container body-container')
    main = container.find('div', class_ = 'main-content')
    wrapper = main.find('div', class_ = 'listings-wrapper')
    post = wrapper.find_all('div', class_ = 'listing')
    views = []
    lins = []
    for i in post:
        left_side = i.find('div', class_ = 'left-side') 
        # title = left_side.find('p', class_ = 'title')
        # address = left_side.find('div', class_ = 'address')
        link = left_side.find('a').get('href')
        full_link = f'https://www.house.kg{link}' 
        links.append(full_link)
    return links
#         right_side = i.find('div', class_ = 'right-side')
#         price = right_side.find('div', class_ = 'price')
#         price_addition= right_side.find('div', class_ = 'price-addition')
#         description = i.find('div', class_ = 'description')
#         span = i.find('div', class_ = 'description')

#         view = info.find('span', {"data-placement":"top"}).text.strip()
#         views.append(int(view))
# sorted_views = sorted(views, reverse=True)
# for view in sorted_views:
#      print(view)

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



def post_detail_data(html):
    soup = BS(html,'html.parser')
    main = soup.find('div', class_ = 'main-content')
    header = main.find('div', class_ = 'details-header')
    title = header.find('div', class_ = 'left').find('h1')
    print(title.text.strip())
    address = header.find('div', class_ = 'address')
    dollar = header.find('div', class_ = 'price-dollar')
    som = header.find('div', class_ = 'price-som')
    description = main.find('div',class_ = 'description')
    if description == None:
        description = 'Описание отсутствует'
    else:
        description = main.find('div',class_ = 'description').find('p').text.strip()
    
    number = main.find('div', class_ = 'phone-fixable-block').find('div', class_ = 'number')
    # number = number if number else 'Номер отсутствует'
    # phone = []
    # for i in number:
    #     phone.append(i.text.strip())
    data = {
            'title':title.text.strip(),
            'address':address.text.strip(),
            'dollar':dollar.text.strip(),
            'som':som.text.strip(),
            'phone':number.text.strip(),
            'description':description,
        }
    return data


def get_last_page(html):
    soup = BS(html, 'html.parser')
    main = soup.find('div', class_ = 'main-content')
    pagination = main.find('ul', class_ = 'pagination')
    pages = pagination.find_all('a', class_ = 'page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)



def save_to_exe(data):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet['A1'] = 'Название'
    worksheet['B1'] = 'Адрес'
    worksheet['C1'] = 'Цена в долларах'
    worksheet['D1'] = 'Цена в сомах'
    worksheet['E1'] = 'Телефон'
    worksheet['F1'] = 'Описание'

    for key,value in enumerate(data,2):
        worksheet[f'A{key}'] = value['title']
        worksheet[f'B{key}'] = value['address']
        worksheet[f'C{key}'] = value['dollar']
        worksheet[f'D{key}'] = value['som']
        worksheet[f'E{key}'] = value['phone']
        worksheet[f'F{key}'] = value['description']
    
    workbook.save('hause_kg.xlsx')
        
 
def main():
    URL = 'https://www.house.kg/kupit-uchastok?region=1&town=2&sort_by=upped_at+desc'
    html = get_html(URL)
    page = get_last_page(html)
    for i in range(1,2):
        html = get_html(f'{URL}&page={i}')
        links = get_post_link(html)
        data = []
        for link in links:
            detail_html = get_html(link)
            data.append(post_detail_data(detail_html))
    save_to_exe(data)


if __name__ == '__main__':
    main() 
