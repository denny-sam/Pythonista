import sys
import requests
from bs4 import BeautifulSoup


if len(sys.argv)>2:
    print("Enter a single URL of the playlist!")
    sys.exit()


url=sys.argv[1]

res=requests.get(url)
f=BeautifulSoup(res.text,'html.parser')
title=f.findAll('h1',{'class':'pl-header-title'})
title=title[0].text

mins=0
secs=0
hrs=0
for x in f.findAll('div',{'class':'timestamp'}):
    x=x.text
    wesplit=x.split(':')
    minute=0
    seconds=0
    hours=0

    if len(wesplit)==2:
        minute=int(wesplit[0])
        seconds=int(wesplit[1])
    elif len(wesplit)==3:
        hours=int(wesplit[0])
        minute=int(wesplit[1])
        seconds=int(wesplit[2])

    hrs+=hours
    mins+=minute
    secs+=seconds

addMin=secs//60
realSecs=secs%60

mins+=addMin
addHours=mins//60

hours+=addHours
realMins=mins%60

print("The playlist {3} is {0} hours, {1} minutes and {2} seconds long!".format(hours,realMins,realSecs,title))





