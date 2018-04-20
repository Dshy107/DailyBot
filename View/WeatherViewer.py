# Project: DailyBot
# FileName: WeatherViewer
# Current User: Rasmus laptop
# Date Created: 13/04/2018
# Developed in PyCharm

import tkinter.font
from tkinter import *

import theme as Theme

from Controller import WeatherApiController

#EARLY DEVELOPMENT, USING: https://stackoverflow.com/questions/43843624/create-textbox-widgets-in-tkinter-of-different-length-for-multiple-labels-in-dif

win = Tk()
WAC = WeatherApiController.WeatherApiController()

#Create N frames on top of each other
N = 1
frames = []

for n in range(N):
    frame = Frame(win)
    frame.pack(side = 'top', anchor = 'w')

    #Store the current frame reference in "frames
    frames.append(frame)

    #Widgets that can go into each frame
    entryboxes = {frame: [] for frame in frames}
    for i, frame in enumerate(frames):
        label = tkinter.Label(frame, text = 'Label '+str(i+1))
        label.pack(side = 'left')
        # Add 5 Entry boxes with random widths
        for i in range(2):
            e = Entry(frame, width = 20)
            e.pack(side = 'left')
            # Store the current entrybox reference in "entryboxes"
            entryboxes[frame].append(e)
    def press():
        message = 'Button Pressed'
        win.update()

        b = Button(win, command=press).pack()

# Add some text in the 4th box of the 3rd frame
entryboxes[frames[0]][1].insert(0,WAC.getTemp())

#Launch the app
win.configure(background=Theme.GUI_bg)
win.mainloop()