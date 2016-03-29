import re
import urllib

html = urllib.urlopen("http://www.thehindu.com/?service=rss")
htmltext = html.read()
htmltext = htmltext.replace('\n','')
regex_item = re.escape('<item>')+'(.+?)'+re.escape('</item>')
regex_title = '<title><' + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>') + '</title>'
regex_category = '<category><' + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>') + '</category>'
regex_link = '<link>(.+?)' + re.escape("utm_source=RSS_Feed&amp;utm_medium=RSS&amp;utm_campaign=RSS_Syndication</link>")
regex_description = '<description><' + '(' + re.escape('![CDATA[') + '|' + re.escape('![CDATA[')+ ')'+ '(.+?)' + re.escape(']]>') +'</description>'
regex_pub_date = '<pubDate><' + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>') + '</pubDate>'
#regex_title = '<title><![CDATA[(.+?)]]</title>'
pattern_item = re.compile(regex_item)
pattern_title = re.compile(regex_title)
pattern_category = re.compile(regex_category)
pattern_link = re.compile(regex_link)
pattern_description = re.compile(regex_description)
pattern_pub_date = re.compile(regex_pub_date)

results_item = re.findall(pattern_item,htmltext)
results_title = re.findall(pattern_title,htmltext)
results_category = re.findall(pattern_category,htmltext)
results_link = re.findall(pattern_link,htmltext)
results_description = re.findall(pattern_description,htmltext)
results_pub_date = re.findall(pattern_pub_date,htmltext)

print "ITEMS" , len(results_item)
print results_item
print "TITLES" , len(results_title)
print results_title 
print "CATEGORY" , len(results_category)
print results_category 
print "LINK" , len(results_link)
print results_link 

"""These fields are not required now"""

#print "DESCRIPTION" , len(results_description)
#print results_description 
#print "DATE AND TIME OF PUBLISHTION"  , len(results_pub_date)
#print results_pub_date

"""ALL IN ONE but its giving less number of results"""
#regex = re.escape('<item><title><') + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>') + re.escape('</title><author><') + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>') + re.escape('</author><category><') + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>') + '</category>' + re.escape('<link>')+'(.+?)' + re.escape("utm_source=RSS_Feed&amp;utm_medium=RSS&amp;utm_campaign=RSS_Syndication</link>") + re.escape('<description><') + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>')+ '</description>' + '<pubDate><' + re.escape('![CDATA[') + '(.+?)' + re.escape(']]>') + re.escape('</pubDate></item>')
#pattern = re.compile(regex)
#results = re.findall(pattern,htmltext)
#print "ALL IN ONE"  , len(results)
#print results
