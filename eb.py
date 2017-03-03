import requests
import csv
from bs4 import BeautifulSoup

import pandas as pd
count=0
while count<10:
    page = requests.get("http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=10&_nkw=supreme+abstract&_pgn=" + str(count) + "&_skc=50&rt=nc")#get page that has forecast
    soup = BeautifulSoup(page.content, 'html.parser')#creat bs class to parse the page
    seven_day = soup.find(id="CenterPanel")#find div for seven day forecast

    forecast_items = seven_day.find_all(class_="lvprices left space-zero")#extract data to print
    tonight = forecast_items[0]
#print(tonight.prettify())
    price = tonight.find(class_="bold").get_text()
#print(price)
    period_tags = seven_day.select(".clearfix .lvtitle")#where the price is

    periods = [pt.get_text() for pt in period_tags]
    periods = [w.replace('\t', '') for w in periods]#getting rid of any \t
    periods = [w.replace('\n', '') for w in periods]#rid of any \n
    periods = [w.replace('New listing\r', '') for w in periods]

#periods = periods.replace('\t', ',')
#print(periods)

    temps = [t.get_text() for t in seven_day.select(".clearfix .lvprice")]
    temps = [w.replace('\t', '') for w in temps]
    temps = [w.replace('\n', '') for w in temps]
#print(temps)

    with open('results.csv', 'w') as o:
        writer = csv.writer(o, delimiter=',')
        writer.writerows(zip(temps))
    count = count+1
