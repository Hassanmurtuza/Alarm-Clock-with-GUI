from tkinter.ttk import *
from tkinter import *

from datetime import datetime
from time import sleep

from pygame import mixer

#window
window = Tk()
window.title("")
window.geometry('350x150')

#Alarm Tone defined
def sound_alarm():
    mixer.music.load('alarmringtone.mp3')
    mixer.music.play()

#Bydefault alarm if time is not set
def alarm():
    while True:
        control = 1 #if the alarm is activated then it will start
        print(control)
        #user given time
        alarm_hour='08'
        alarm_minute = '43'
        alarm_sec ='00'
        alarm_period = 'PM'.upper()

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
 

mixer.init()
alarm()

window.mainloop()