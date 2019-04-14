import urllib,urllib.request
from bs4 import BeautifulSoup

url = "https://www.skymetweather.com/forecast/weather/india/maharashtra/raigad/panvel"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
temp = soup.find('span',{'class':'c'}).text

class Sky:
    def status(self):
        if (page.code==200): #status code of the site
            print("skymetweather is live\nExtracting data........")
        else:
            print("The site is not live....")
            print("please try again")
    def __init__(self):
        self.temp=temp

