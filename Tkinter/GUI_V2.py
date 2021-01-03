import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfile
import os
import sqlite3
from pathlib import Path
import tkinter.scrolledtext as st
from File import *
from Functions import *

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

LARGEFONT = ("Verdana", 35)


file_list = list()

class RestaurantApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # first window frame startpage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Frame.config(self,background = '#add8e6')
        self.Font = Font(family="Helvetica", size=36)

        style = ttk.Style(self)
        style.configure('TLabel', background='#add8e6', foreground='#FF69B4')
        style.configure('TFrame', background='#add8e6')
        style.configure("TButton", padding= 10, relief="flat",
                              background="yellow")

        frame = ttk.Frame(self)
        frame.grid(column=0, row=0)

        div = ttk.Label(frame)
        div.grid(column=1, rows=1, padx = 60)

        div_1 = ttk.Label(frame)
        div_1.grid(column=2, rows=1, pady = 50)

        button = ttk.Button(frame, text="Start", command= lambda : controller.show_frame(Page1))
        button.grid(column=2, row=3, pady = 20)

        button_1 = ttk.Button(frame, text="Close", command=lambda: app.destroy())
        button_1.grid(column=2, row=4, pady=20)

        lab = ttk.Label(frame, text="Welcome \n to the App", font = self.Font, background = '#33D1F6')
        lab.grid(column=2, row=2)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, background='#add8e6')


        style = ttk.Style(self)
        style.configure('TLabel', background='#add8e6', foreground='#FF69B4')
        style.configure('TFrame', background='#add8e6')
        style.configure("Bold.TButton", font=('Sans', '10', 'bold'))


        div = Label(self)
        div.grid(row=0, column=1, padx=60, pady = 60)

        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=2, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage), style = "Bold.TButton")

        button_bonus = ttk.Button(self, text="Add Data ", command=popup_bonus, style = "Bold.TButton")
        button_bonus.grid(row=1, column=1)

        label = ttk.Label(self)
        label.grid(row=1, column=0, padx=15, pady=10)

        saveButton = ttk.Button(self, text="Save", command=lambda: file.saveFile(), style = "Bold.TButton")
        saveButton.grid(row=2, column=1, pady = 50)

        #div = Label(self)
        #div.grid(row=1, column=2, padx = 100)

        button_Query = ttk.Button(self, text="Query", command=generate_Report, style = "Bold.TButton")
        button_Query.grid(row=1, column=3)

        convertButton = ttk.Button(self, text="Convert", command=lambda: file.toJSON(), style = "Bold.TButton")
        convertButton.grid(row=2, column=3)


        # putting the button in its place
        # by using grid
        button1.grid(row=3, column=1, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2), style = "Bold.TButton")

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=3, padx=10, pady=10)

        file = File()



        #selectButton = ttk.Button(self, text='Open', command=lambda: file.selectFile(file_list))

        #queryButton = Button(self, text="Query", command=lambda: file.toJSON())


        #selectButton.grid(row=1, column=1)






        # third window frame page2


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def plot(self, canvas):

            print('File Selected')
            df = pd.read_csv(file_path)
            print('print file read in')
            df = pd.DataFrame(df)
            print('converted to data frame')
            ax = fig.add_subplot(111)
            print('selecting subplot')
            print('Making a bar graph')
            df.plot.bar(ax=ax)
            canvas.draw()

        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=0, padx=10, pady=10)

        lf = Labelframe(self, text='Plot Area')
        lf.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)
        matplotlib.use("TkAgg")
        lf = Labelframe(self, text='Plot Area')
        lf.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)

        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=self)



        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=0, padx=10, pady=10)



    # Driver Code




def popup_bonus():
    value = File()
    value.process = True
    win = Toplevel()
    win.wm_title("Window")

    l = Label(win, text="Input")
    l.grid(row=0, column=0)

    b = Button(win, text="Completed", command=win.destroy)
    b_1 = Button(win, text="Add_Data", command= lambda: value.setFile())
    b_2 = Button(win, text="Restart", command= lambda: value.restart())

    b.grid(row=1, column=0)
    b_1.grid(row=2,column=0)
    b_2.grid(row=3,column =0)


def generate_Report():
    value = File()
    value.process = True
    win = Toplevel()
    win.wm_title("Window")

    l = Label(win, text="Input")
    l.grid(row=0, column=0)

    b = Button(win, text="End", command=win.destroy)
    b_1 = Button(win, text="Set_Query", command= lambda: generate_Query())
    b.grid(row=1, column=0)
    b_1.grid(row=2,column=0)

def generate_Query():
    value = File()
    value.process = True
    win = Toplevel()
    win.wm_title("Window")

    select = Query()
    l = Label(win, text="Group By")
    l.grid(row=0, column=0)

    b = Button(win, text="Finished", command=win.destroy)
    b_1 = Button(win, text="Aggregate", command= lambda:aggregate(select))
    b_2 = Button(win, text="Seating", command=lambda:select.group_By_1(parameter_list))
    b_3 = Button(win, text="Zip Codes", command=lambda:select.group_By_2(parameter_list))
    b_4 = Button(win, text="Seating & Zip Codes", command=lambda: select.group_By(parameter_list))


    b.grid(row=1, column=0)
    b_1.grid(row=2,column=1)
    b_2.grid(row=2, column=0)
    b_3.grid(row=3, column = 0)
    b_4.grid(row=4, column = 0)


def aggregate(select):
    value = File()
    value.process = True
    win = Toplevel()
    win.wm_title("Window")

    l = Label(win, text="Input")
    l.grid(row=0, column=0)


    b = Button(win, text="End", command=win.destroy)
    b_1 = Button(win, text="Mean", command= lambda: select.mean())
    b_2 = Button(win, text="Median", command=lambda: select.median())
    b_3 = Button(win, text="Mode", command=lambda: select.mode())
    b_4 = Button(win, text="Review Query", command=  lambda: review(win,select))

    b.grid(row=1, column=0)
    b_1.grid(row=2,column=0)
    b_2.grid(row=3,column=0)
    b_3.grid(row= 4, column =0 )
    b_4.grid(row=5, column=0)

def review(win,select):

    # Title Label
    tk.Label(win,
             text="Reviewing Query",
             font=("Times New Roman", 15),
             background='pink',
             foreground="blue").grid(column=0,
                                      row=0)

    # Creating scrolled text area
    # widget with Read only by
    # disabling the state
    text_area = st.ScrolledText(win,
                                width=30,
                                height=8,
                                font=("Times New Roman",
                                      15))

    text_area.grid(column=0, pady=10, padx=10)

    # Inserting Text which is read only
    text_area.insert(tk.INSERT, select.query_print())


    # Making the text read only
    text_area.configure(state='disabled')


app = RestaurantApp()
app.minsize(500,500)
app.maxsize(500,500)
app.mainloop()
