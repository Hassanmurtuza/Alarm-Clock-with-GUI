from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime
from time import sleep

from threading import Thread

#colors
bg_color = 'white'
co1 = 'black'
co2 = 'blue'

#window
window = Tk()
window.title("Alarm Clock")
window.geometry('350x150')
window.configure(bg=bg_color)

#Frame up 
frame_line = Frame(window, width=400, height =5, bg=co1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height =290, bg=bg_color)
frame_body.grid(row=1, column=0)

#configure frame body
img = Image.open('icon.png')#image added
img.resize((100,100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10 ,y=10)

#Alarm Lable
name = Label(frame_body, text ="Alarm", height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125, y=10)

#Clock Hours 
hour = Label(frame_body, text ="Hour", height=1, font=('Ivy 10 bold'), bg=bg_color)
hour.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=130, y=58)

#Clock Minutes
min = Label(frame_body, text ="min", height=1, font=('Ivy 10 bold'), bg=bg_color)
min.place(x=177, y=40)
c_min = Combobox(frame_body, width=2, font=('arial 15'))
c_min['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_min.current(0)
c_min.place(x=180, y=58)

#Clock Seconds
sec = Label(frame_body, text ="sec", height=1, font=('Ivy 10 bold'), bg=bg_color)
sec.place(x=227, y=40)
c_sec = Combobox(frame_body, width=2, font=('arial 15'))
c_sec['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=230, y=58)

#Clock Period AM ,PM
period = Label(frame_body, text ="Period", height=1, font=('Ivy 10 bold'), bg=bg_color)
period.place(x=277, y=40)
c_period = Combobox(frame_body, width=3, font=('arial 15'))
c_period['values'] = ("AM","PM")
c_period.current(0)
c_period.place(x=280, y=58)

#Define Set Alarm Button Function 
def activate_alarm():
    t = Thread(target=alarm)
    t.start()

#Defining Dismiss Button Function
def deactivate_alarm():
    print('Deactivate alarm: ', selected.get())
    mixer.music.stop()

#Clock alarm set , dismiss Button
selected = IntVar()
#Set Alarm Button
red1 = Radiobutton(frame_body, font=('arial 10 bold'), value = 1, text ="Set Alarm" , bg =bg_color, command=activate_alarm, variable=selected)
red1.place(x=125, y=95)

#Copied from demo and make some changes here
def sound_alarm():
    mixer.music.load('alarmringtone.mp3')
    mixer.music.play()
    selected.set(0)
    #Dismiss button is made here
    red2 = Radiobutton(frame_body, font=('arial 10 bold'), value = 2, text ="Dismiss" , bg =bg_color, command=deactivate_alarm, variable=selected)
    red2.place(x=187, y=95)

#Alarm Main function 
def alarm():
    while True:
        control = selected.get() 
        print(control)
        #using get() functon 
        alarm_hour=c_hour.get()
        alarm_minute =c_min.get()
        alarm_sec =c_sec.get()
        alarm_period =c_period.get()
        alarm_period = str(alarm_period).upper() #AM , PM is a string so using str and upper caseletter

        now = datetime.now()
        #Current Time in world
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a brake!")
                            sound_alarm()
        sleep(1)

# t = Thread(target=alarm)
# t.start()

mixer.init()

window.mainloop()