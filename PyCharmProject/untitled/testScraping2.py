import requests
from bs4 import BeautifulSoup
import csv
import pprint
import lxml

BASE_URL = 'http://www.pythonscraping.com'


def create_list_from_table(table_tag):
    gifts = []
    headers = []
    header_tag = table_tag.find('tr')
    for th_tag in header_tag.find_all('th'):
        headers.append(th_tag.text.strip())
    gifts.append(headers)

    for tr_tag in table_tag.find_all('tr'):
        gift = []
        for td_tag in tr_tag.find_all('td'):
            if td_tag.text.strip() != '':
                gift.append(td_tag.text.strip().replace('\n',' '))
            else:
                gift.append(BASE_URL + td_tag.find('img').get('src')[2:])

        if not gift:
            continue
        gifts.append(gift)

    return gifts

def create_csv_file(lol, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for l in lol:
            writer.writerow(l)

def main():
    res = requests.get(BASE_URL + '/pages/page3.html')
    soup = BeautifulSoup(res.text, 'lxml')

    table_tag = soup.find(id='giftList')

    print(table_tag)

    gifts = create_list_from_table(table_tag)
    create_csv_file(gifts, 'gifts.csv')

    print('job completed..')

if __name__ == '__main__':
    main()