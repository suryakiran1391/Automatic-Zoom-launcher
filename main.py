import time
import data
from data import *
from datetime import date, datetime
from pynput.keyboard import Controller, Key
from data import timetable
import webbrowser

keyboard = Controller()

isStarted = False

for i in timetable:
    while True:
        if not isStarted:
                if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                    if i[0] is subject1:
                        subject1()
                        print("subject1 class is opened")
                    if i[0] is subject2:
                        subject2()
                        print("subject2 class is opened")
                    #Add the If statement according to the number of subjects
                    
                    isStarted = True
                else:
                    if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                        keyboard.press('w') #Rebind this key so this key will leave the meeting
                        time.sleep(1)
                        keyboard.press(Key.enter) #Enter is pressed if the meeting is ended by host
                        isStarted = False
                        break
                    time.sleep(5)
