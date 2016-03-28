import urllib
import re

"""scraping from most commented link"""

"""scraping from most commented section with anytime link"""
print "ANYTIME COMMENTED"
html = urllib.urlopen("http://timesofindia.indiatimes.com/mostcommented.cms")
htmltext = html.read()
regex_anytime = '<strong>(.+?)</strong>'
pattern_anytime = re.compile(regex_anytime)
results_anytime  = re.findall(pattern_anytime,htmltext)
for i in range(0,len(results_anytime)):
    print results_anytime[i]

"""scraping from most commented section with anytime link"""
print "LAST 24 HRS"
html_last_24_hrs = urllib.urlopen("http://timesofindia.indiatimes.com/mostcommented.cms?day=1")
htmltext_last_24_hrs = html_last_24_hrs.read()
regex_last_24_hrs = '<strong>(.+?)</strong>'
pattern_last_24_hrs = re.compile(regex_last_24_hrs)
results_last_24_hrs = re.findall(pattern_last_24_hrs,htmltext_last_24_hrs)
for i in range(0,len(results_last_24_hrs)):
    print results_last_24_hrs[i]

"""scraping from most commented section with past 4 days link"""
print "LAST 4 DAYS"
html_last_4_days = urllib.urlopen("http://timesofindia.indiatimes.com/mostcommented.cms?day=4")
htmltext_last_4_days = html_last_4_days.read()
regex_last_4_days = '<strong>(.+?)</strong>'
pattern_last_4_days = re.compile(regex_last_4_days)
results_last_4_days = re.findall(pattern_last_4_days,htmltext_last_4_days)
for i in range(0,len(results_last_4_days)):
    print results_last_4_days[i]


"""scraping from most commented section with past week link"""
print "LAST 7 DAYS"
html_last_week = urllib.urlopen("http://timesofindia.indiatimes.com/mostcommented.cms?day=7")
htmltext_last_week = html_last_week.read()
regex_last_week = '<strong>(.+?)</strong>'
pattern_last_week = re.compile(regex_last_week)
results_last_week = re.findall(pattern_last_week,htmltext_last_week)
for i in range(0,len(results_last_week)):
    print results_last_week[i]

"""scraping from most commented section with past month link"""

print "LAST 30 DAYS"
html_last_30_days = urllib.urlopen("http://timesofindia.indiatimes.com/mostcommented.cms?day=30")
htmltext_last_30_days = html_last_30_days.read()
regex_last_30_days = '<strong>(.+?)</strong>'
pattern_last_30_days = re.compile(regex_last_30_days)
results_last_30_days = re.findall(pattern_last_30_days,htmltext_last_30_days)
for i in range(0,len(results_last_30_days)):
    print results_last_30_days[i]



#html = urllib.urlopen("http://timesofindia.indiatimes.com/mostcommented.cms")
#htmltext = html.read()
for val in range(0,len(results_anytime)):
    regex_1 = '<a pg="#'+str(val+1)+ '" title="(.+)" href="(.+)"'
    #regex_1 = '<a pg=".[0-9]{1-2}" title="(.+)" href="(.+)">(.+)</a>'
    pattern_1 = re.compile(regex_1)
    results_1 = re.findall(pattern_1,results_anytime[val])
    print results_1, results_anytime[val]
    


