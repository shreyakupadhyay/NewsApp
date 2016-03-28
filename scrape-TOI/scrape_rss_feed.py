from lxml import html
import requests
import urllib
import re

"""Using selenium for opening today's newspaper"""
"""
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.thehindu.com/")
eleml = driver.find_element_by_link_text("Today's Paper")
eleml.click()
"""

page = requests.get('http://timesofindia.indiatimes.com/rss.cms')
tree = html.fromstring(page.content)

#array = tree.xpath('/html/body/div[@id="main-copy"]/p/table/tbody/tr/td[@width="120"]/a/text()')
"""Getting all the links and text from the TOI news feed"""

array_titles = tree.xpath('//*[@width="120"]/a[@href]/text()')
array_links = tree.xpath('//*[@width="120"]/a/@href')
print array_titles , len(array_titles)
print array_links , len(array_links)
"""Getting data from the subsequent links from the array_links"""

"""Till 71 it is text and working and after that from 72 to 80 we have video feeds"""
#for i in range(0,len(array_links)):
html = urllib.urlopen(array_links[71])
htmltext = html.read()
htmltext.replace('\n','')
regex = '<item><title>(.+?)</title><link>(.+?)</link><description>(.+?)</description><pubDate>(.+?)</pubDate><guid isPermaLink="false">(.+?)</guid></item>'
pattern = re.compile(regex)
results = re.findall(pattern,htmltext)
for i in range(0,len(results)):
    print results[i] 
print len(results)
#page_2 = requests.get(array_links[0])
#tree_2 = html.fromstring(page_2.content)
#array_title = tree_2.xpath('//*div[@id="items"]//h3/@class')
#array_title = tree_2.xpath('//*[@id="items"]/div[1]/h3/a')
