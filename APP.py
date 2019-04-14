import time
import datetime
from tkinter import *
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
print('\nRunning the app')

w.temp=float(w.temp)
s.temp=float(s.temp)
y.temp=float(y.temp)
temp = int((w.temp+s.temp+y.temp)/3)
samay = str(datetime.date.today().strftime("%d") +"  "+ datetime.date.today().strftime("%B") + " " + datetime.date.today().strftime("%Y") + " , " +datetime.date.today().strftime("%A") )

window = Tk()
frame= Frame(window)
frame.pack()

window.title("Panvel : Weather")
window.geometry('500x350')
t = Label(window, text=str(temp)+"°c", font=("Arial Bold", 35), fg="blue", )
d = Label(window, text=str(y.desc), font=("Arial Bold", 11), fg="black",bg="yellow" )
d2 = Label(window, text=str(y.hum[2]), font=("Arial Bold", 11), fg="black",bg="yellow" )
d3 = Label(window, text=str(y.hum[1]), font=("Arial Bold", 11), fg="black",bg="yellow" )
de = Label(window, text=samay, font=("Arial Bold", 12), fg="black",bg="yellow" )
t.pack(side = TOP, pady = 10)
d.pack(side = TOP)
d2.pack(side = LEFT, padx = 10)
d3.pack(side = RIGHT, padx = 10)
de.pack(side = BOTTOM, pady = 10)



