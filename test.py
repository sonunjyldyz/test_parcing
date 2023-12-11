from bs4 import BeautifulSoup as BS 


with open('test.html', encoding='utf-8') as file:
    html = file.read()

soup = BS(html, 'html.parser')


container = soup.find('div', class_='container')
novigation = container.find('div', class_='novigation')
list = novigation.find('ul', class_='list')
li = list.find_all('li')

# for item in li:
#     print(item.text)



content = container.find('div', class_='content')
post = content.find('div', class_='post')
h2 = post.find_all('h2', class_='title')

for item in h2:
    print(item.text.strip())

# команда strip убирает пробелы из строки. 
