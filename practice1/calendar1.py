# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
import calendar

def showCalendar():
    gui = Tk()
    gui.config(background='blue')
    gui.title("JG Calendar")
    gui.geometry("600x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text = gui_content, font= "times 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()



if __name__ == "__main__" :
    new = Tk()
    new.config(background = 'green')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="calendar", bg='grey',font="arial 28 bold")
    year = Label(new, text = "Enter year", bg= "yellow")
    year_field=Entry(new)
    button = Button(new, text="show Calendar",
                    fg="red",bg="orange",command=showCalendar)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)


    new.mainloop()
