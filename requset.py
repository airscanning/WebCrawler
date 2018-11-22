import requests
from bs4 import BeautifulSoup as bs
import pymysql
import time

db = pymysql.connect('localhost', 'root', '123456', 'AirPollution')
cursor = db.cursor()


def GetRequests(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = requests.get(url=url, headers=headers)
    return request.content


name = ['wuhan']

for n in name:
    url = 'http://www.pm25.in/' + n
    print(n)
    request = GetRequests(url)
    soup = bs(request, 'lxml')
    tbody = []
    item = []

    t = 0
    for i in soup.select('tbody tr td'):
        t += 1
        s = i.string
        if s == '_' or s == None:
            s = -1

        item.append(s)

        if t % 11 == 0:

            tbody.append(item)

            item = []

    for id, i in enumerate(tbody):
        if i[0] == '东湖高新' or i[0] == '东湖梨园':
            pass
        else:
            sql = 'insert into APDATA value (' + \
              '\'{}\',\'{}\',{},\'{}\',{},\'{}\',{},{},{},{},{},{},{});'.format(
                  n.upper(), time.strftime('%Y-%m-%d', time.localtime(time.time())),
                  id, i[0], i[1], i[2], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
            print(sql)

    # cursor.execute(sql)
    db.commit()
    db.rollback()
    db.close()
