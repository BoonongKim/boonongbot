import feedparser
from pprint import pprint
from dateutil import parser
from time import sleep
import telegram


TOKEN = '1771137852:AAGIPBCGtunjq2tMbViqYVBJ2FgeU4Htcbs'
CHAT_ID = '747002087'
bot = telegram.Bot(token=TOKEN)

disclosure_list_old = []  

while True:
    
    rss_info = feedparser.parse("http://dart.fss.or.kr/api/todayRSS.xml")
    disclosure_list = rss_info['entries']

    
    if len(disclosure_list_old) == 0:
        
        for disclosure in disclosure_list:
            company = disclosure['author']
            link = disclosure['link']
            published = parser.parse(disclosure['published'])
            year = published.year
            month = published.month
            day = published.day
            hour = published.hour + 9
            minute = published.minute
            date_info = f'{year}년 {month}월 {day}일 {hour}시 {minute}분'
            title = disclosure['title']
            message = f'{title}\n{link}\n{date_info}'
            
            if '코스닥' in title:
                bot.send_message(chat_id=CHAT_ID, text=message)
                print(company, link, date_info, title)

    else:
        for disclosure in disclosure_list:
            if disclosure['title'] == disclosure_list_old[0]['title']:
                break
        
            company = disclosure['author']
            link = disclosure['link']
            published = parser.parse(disclosure['published'])
            year = published.year
            month = published.month
            day = published.day
            hour = published.hour + 9
            minute = published.minute
            date_info = f'{year}년 {month}월 {day}일 {hour}시 {minute}분'
            title = disclosure['title']
            message = f'{title}\n{link}\n{date_info}'

            if '코스닥' in title:
                bot.send_message(chat_id=CHAT_ID, text=message)
                print(company, link, date_info, title)

    disclosure_list_old = disclosure_list

    sleep(3)