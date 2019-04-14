import urllib,urllib.request
from bs4 import BeautifulSoup

def cel(f):
    if f == "--":
        return None
    else:
        f=int(f)
        return int((f-32)*(5/9))

url = "https://www.wunderground.com/weather/in/panvel"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
temp = soup.find('span',{'class':'wu-value wu-value-to'}).text
temp_low = soup.find('span',{'class':'lo'}).text
temp_low = temp_low.replace("°","")
temp_high = soup.find('span',{'class':'hi'}).text
temp_high = temp_high.replace("°","")

class Wunder:
    def status(self):
        if (page.code==200): #status code of the site
            print("wunderground is live\nExtracting data........")
        else:
            print("The site is not live....")
            print("please try again")
    def __init__(self):
        self.temp=cel(temp)
        self.temp_low=cel(temp_low)
        self.temp_high=cel(temp_high)


