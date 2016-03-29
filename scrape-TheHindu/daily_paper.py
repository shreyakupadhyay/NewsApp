from lxml import html
import requests
import sys
import time

"""Using lxml for finding the data inside a tag and the link inside it."""

"""Getting today's date"""

today_date = (time.strftime("%Y-%m-%d"))
print (time.strftime("%H:%M:%S"))

"""Changing date before 9 am"""

if(int(time.strftime("%H"))>9):
    today_date = (time.strftime("%Y-%m-%d"))
    print today_date
else:
    today_date = int((time.strftime("%d"))) - 1
    print today_date

"""getting daily newspaper according to date"""

page = requests.get('http://www.thehindu.com/todays-paper/tp-index/?date='+str(today_date))

"""page.content rather than page.text because html.fromstring excepts bytes as input"""

tree = html.fromstring(page.content)

"""traversing to that tag which contains the link and the text"""

array_titles = tree.xpath('/html/body//div[@class="tpaper"]/a[@href]/text()')
array_links = tree.xpath('/html/body//div[@class="tpaper"]/a/@href')
print array_titles , len(array_titles)
print array_links , len(array_links)

"""WORKING"""
