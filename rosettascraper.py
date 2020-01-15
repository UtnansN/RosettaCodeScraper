import random
from bs4 import BeautifulSoup, NavigableString
from requests import get

url = 'https://rosettacode.org/wiki/Category:Programming_Tasks'
response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')

categories = soup.find_all('div', class_='mw-category-group')

tasks = []
for i in range(len(categories)):
    for entry in categories[i].ul:
        if isinstance(entry, NavigableString):
            continue
        data = entry.find('a', href=True, title=True)
        tasks.append((data['title'], data['href']))

while (True):
    task = random.choice(tasks)
    print('Your task is: ' + task[0])
    print('URL: https://rosettacode.org' + task[1])
    cont = input('Pick another task? (y/n): ')
    if cont.lower() == 'y':
        continue
    else:
        break

print('Exited')
