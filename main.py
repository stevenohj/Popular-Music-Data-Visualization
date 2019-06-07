import tkinter
from tkinter import *
import datetime
import calendar
import Spotify_Charts_Scraper as scraper
import music_data_bubble_plot as bubbles


def display_bubbles(event):
    music_data = scraper.scrape_music_data(int(year_var.get()), month_var.get(), int(day_var.get()))
    bubbles.display_artist_bubbles(music_data)


window = tkinter.Tk()

# CONFIGURE WINDOW
window.geometry("400x400")
window.resizable(0, 0)
rows = 0
cols = 0
while rows < 15:
    window.rowconfigure(rows, weight=1)
    rows += 1
    if cols < 15:
        window.columnconfigure(cols, weight=1)
        cols += 1

window.title('Musical Time Machine')
window.configure(background='light sky blue')

# WELCOME LABEL
tkinter.Label(window, text='Welcome to the Musical Time Machine!', background='light cyan').grid(row=2, column=2, columnspan=10)
# DATE QUESTION LABEL
tkinter.Label(window, text='What day would you like to travel to?', background='light cyan').grid(row=4, column=2, columnspan=10)
# COUNTRY QUESTION LABEL (WORK IN PROGRESS)
"""tkinter.Label(window, text='Where would you like to travel to?', background='light cyan').grid(row=12, column=3, columnspan=15)"""

# POSITION WINDOW AT CENTER OF SCREEN
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)
window.geometry("+{}+{}".format(positionRight, positionDown))

# GET TODAY'S DATE
d = datetime.datetime.today()

# DAILY/WEEKLY MENU (WORK IN PROGRESS)
"""period_var = StringVar(window)
period_var.set('Daily')  # DEFAULT SET TO TODAY'S DATE
period_menu = OptionMenu(window, period_var, 'Daily', 'Weekly')
period_menu.grid(row=8, column=5, columnspan=5)"""

# YEAR MENU
year_var = StringVar(window)
year_var.set(d.year)  # DEFAULT SET TO TODAY'S DATE
year_menu = OptionMenu(window, year_var, 2017, 2018, 2019)
year_menu.grid(row=8, column=5, columnspan=1)

# MONTH MENU
month_var = StringVar(window)
month_var.set(calendar.month_name[d.month])  # DEFAULT SET TO TODAY'S DATE
month_menu = OptionMenu(window, month_var, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
month_menu.grid(row=8, column=9, columnspan=1)

# DAY MENU
day_var = StringVar(window)
day_var.set(d.day)  # DEFAULT SET TO TODAY'S DATE
day_menu = OptionMenu(window, day_var, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
day_menu.grid(row=8, column=10, columnspan=1)

# COUNTRY MENU (WORK IN PROGRESS)
"""country_var = StringVar(window)
country_var.set('All Countries')  # DEFAULT SET TO TODAY'S DATE
country_menu = OptionMenu(window, country_var, 'All Countries', 'United States','United Kingdom','Argentina','Austria','Australia','Belgium','Bulgaria','Bolivia','Brazil','Canada','Chile','Colombia','Costa Rica','Czech Republic','Germany','Denmark','Dominican Republic','Ecuador','Estonia','Finland','France','Greece','Guatemala','Hong Kong','Honduras','Hungary','Indonesia','Ireland','Israek','India','Iceland','Italy','Japan','Lithuania','Luxembourg','Latvia','Malta','Mexico','Malaysia','Nicaragua','Netherlands','Norway','New Zealand','Panama','Peru','Philippines','Poland','Portugal','Paraguay','Romania','El Salvador','Singapore','Slovakia','South Africa','Sweden','Switzerland','Taiwan','Thailand','Turkey','Uruguay','Vietnam')
country_menu.grid(row=16, column=9)"""

btn = tkinter.Button(window, text="Go back in time!")
btn.bind("<Button-1>", display_bubbles)
btn.grid(row=12, column=10)

window.mainloop()
