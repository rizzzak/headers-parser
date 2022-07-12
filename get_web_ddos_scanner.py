"""

Created on Sun Aug  23 2020
Parser #3: swsu BF 404/not
@author: Ryze
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

import urllib.request
from lxml.html import fromstring # подключаем библиотеку lxml

cntr1 = '_1' #ID банка на сайте banki.ru
cntr2 = 1546

for cntr1 in '','_0', '_1':
    for cntr2 in range(1545,1570,1):
        response = urllib.request.urlopen('https://ee.swsu.ru/Files/orders/2020/Prikaz_zach%s_25.08.2020_%d.pdf' % (cntr1, cntr2)).read()
        page = fromstring(response) # делаем из нашей строки объект для манипулирования страницей
        nameSite = page.xpath('/html/body/main/div/div/h1') # получаем все элементы с переданным xpath
        lenght = len(nameSite)
        if lenght > 0:
            print('str = %s, num = %d' % (cntr1,cntr2),'. Res: 404')
        else:
            print('\tstr = %s, num = %d' % (cntr1,cntr2),'. Res: 200') 
 


# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet':
#     print('#', i, ' color of rainbow is ', color, sep = '')
#     i += 1
# Страница не найдена

# url = 'https://ee.swsu.ru/Files/orders/2020/Prikaz_zach%s_24.08.2020_%d.pdf' % (cntr1, cntr2) # url страницы
# r = requests.get(url)
# code = r.status_code
# print(code)

