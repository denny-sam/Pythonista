import requests
from bs4 import BeautifulSoup


def get_points(url):
    r=requests.get(url)
    x= BeautifulSoup(r.text,'html.parser')
    user=x.findAll('span',{'class':'titles'})

    for f in x.findAll('td'):
        for n in f.findAll('span'):
            print(user[0].text,':',n.text)

for q in range(2,40):
    get_points("https://www.thenewboston.com/profile.php?user="+str(q))
