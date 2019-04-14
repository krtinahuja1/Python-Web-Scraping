import urllib,urllib.request
from bs4 import BeautifulSoup

def cel(f):
    if f == "--":
        return None
    else:
        f=int(f)
        return int((f-32)*(5/9))

url = "https://www.yahoo.com/news/weather/india/panvel-sub-district/panvel-sub-district-90898798"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
temp = soup.find('span',{'class':'Va(t)'}).text
hum=[]
desc = soup.find('span',{'class':'description Va(m) Px(2px) Fz(1.3em)--sm Fz(1.6em)'}).text
det = soup.find('div',{'class':'description Py(10px) Px(4px) Fz(1em)'}).text
for i in range(0,3):
    hum.append(soup.find_all('li',{'class':'item BdB Cf Py(8px) Fz(1.1em) Bds(d) Bdbc(#fff.12)'})[i].text)
class Yahoo:
    def status(self):
        if (page.code==200): #status code of the site
            print("Yahoo is live\nExtracting data........")
        else:
            print("The site is not live....")
            print("please try again")
    def __init__(self):
        self.hum=[]
        self.temp=cel(temp)
        self.desc=desc
        for i in range (0,3):
            self.hum.append(hum[i])
        self.det=det




