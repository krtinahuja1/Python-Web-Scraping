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
print('\nRunning the GUI')

window = Tk()
frame= Frame(window)
frame.pack()
window.title("Weather Scraper")
window.geometry('500x300')

w.temp=str(w.temp)
s.temp=str(int(s.temp))
y.temp=str(int(y.temp))

greet = Label(window, text="Weather Scraper", font=("Arial Bold", 35), fg="red", )
w1 = Label(window, text="Wunderground\n"+w.temp+"°C", font=("Arial Bold", 11), bg= "white")
y1 = Label(window, text="Yahoo\n"+s.temp+"°C", font=("Arial Bold", 11) ,bg= "white")
s1 = Label(window, text="Skymetweather\n"+y.temp+"°C", font=("Arial Bold", 11) ,bg= "white")
 
greet.pack(side = TOP)
w1.pack(side = LEFT, padx = 10)
y1.pack(side = RIGHT, padx = 10)
s1.pack(side = BOTTOM, pady=10)
 
window.mainloop()
print('GUI stopped')
