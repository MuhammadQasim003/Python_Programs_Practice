import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.whatmobile.com.pk/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

div = soup.find('div', style='width:680px;display: inline-block')
try:
    sections = div.find_all('section')
    mobile_data = []
    for section in sections:
        container = section.find('ul')
        if container:
            for mobile in container.find_all('li'):
                model = mobile.find('a')
                titles = model.get('href') 
                title = str(titles)
                title = title.replace("/","")
                title = title.replace("_"," ")
                price_tag = mobile.find('span')
                price = price_tag.text.strip()
                mobile_data.append([title, price])
    csv_file = 'mobile_data.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Model', 'Price'])
        writer.writerows(mobile_data)
    print('Mobile data has been scraped and saved to {}.'.format(csv_file))

except ValueError:
    print('Div not found. Please check the website structure.')
