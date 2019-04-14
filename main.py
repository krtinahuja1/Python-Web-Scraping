
import time
import datetime
print("Extracting data from websites please wait.....\n")
from web.wunder import Wunder
w=Wunder()
w.status()
print('\n')
from web.sky import Sky
s=Sky()
s.status()
print('\n')
from web.yahoo import Yahoo
y=Yahoo()
y.status()
w.temp=float(w.temp)
s.temp=float(s.temp)
y.temp=float(y.temp)
temp = int((w.temp+s.temp+y.temp)/3)
samay = str(datetime.date.today().strftime("%d") +"  "+ datetime.date.today().strftime("%B") + " " + datetime.date.today().strftime("%Y") + " , " +datetime.date.today().strftime("%A") )

print("Temprature : " + str(temp))
print(str(y.desc))
print(str(y.hum[2]))
print(str(y.hum[1]))
print(str(y.det))
