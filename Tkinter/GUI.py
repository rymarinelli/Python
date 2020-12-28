import json
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
import glob
import matplotlib
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
from pathlib import Path
import os

from tkinter.messagebox import showinfo


# The input is going to be three csv files
# You will need to prompt for input and join them
# Use try catch logic


def popup_bonus():
    win = Toplevel()
    win.wm_title("Window")

    l = Label(win, text="Input")
    l.grid(row=0, column=0)

    b = Button(win, text="Okay", command=win.destroy)
    b_1 = Button(win, text="Add_Data", command= lambda: file.setFile())
    b.grid(row=1, column=0)
    b_1.grid(row=2,column=0)

root = Tk()
#root.geometry('200x200')
lf = Labelframe(root, text='Plot Area')
lf.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)
matplotlib.use("TkAgg")
lf = Labelframe(root, text='Plot Area')
lf.grid(row=0, column=0, sticky='nwes', padx=3, pady=3)

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)

button_bonus = Button(root, text="Bonuses", command=popup_bonus)


# This function will be used to open
# file in read mode and only Python files
# will be opened

file_list = list()

class File():

    def __init__(self):
        self.content = ""
        self.filePath = ""

    def setFile(self):
        downloads = str(os.path.join(Path.home(), "Downloads"))
        file_path = downloads + "\combined_test.csv"
        file = self.selectFile(file_list)


        print(file_list)
        #It might be better to replace pd.concat with join
        #Faculity ID might be a good choice here

        #combined_csv = pd.concat([pd.read_csv(f) for f in file_list])

        #Start loop with the 2nd file
        #Read in the first file based on the zeroth position
        #If join fails, add columns

        df = pd.read_csv(file_list[0])
        while len(file_list) >= 3:
            for f in range(1,len(file_list)):
                print(file_list[f])
                df_1 = pd.read_csv(file_list[f])
                df_2 = pd.concat([df.reset_index(drop=True), df_1], axis=1)
                combined_csv = df_2
                combined_csv.to_csv(file_path, index=False)

            combined_csv = df_2
            combined_csv.to_csv(file_path, index=False)
            break


        file = self.selectFile(file_list)
        self.content = file

    def setPath(self):
        self.selectFile()

    def getPath(self):
        return(self.filePath)

    def getFile(self):
        return self.content


#Working on now
    #Read in data from file
    #Read the file path of the selected file into a list
    # Clear the file path variable
    # Select the Content of the inital file
    def selectFile(self,file_list):
        file = askopenfile(mode='r', filetypes=[('Comma-Delimited', '*.csv')])
        self.filePath = file.name
        if file is not None:
            content = file.read()
            file_list.append(self.filePath)
            self.filePath = None

            if len(file_list) == 4:
                file_list.clear()
                print("Assign File Path")
                downloads = str(os.path.join(Path.home(), "Downloads"))
                file_path = downloads + "\combined_test.csv"
                self.filePath = file_path
                content = pd.read_csv(file_path)
                print(content)
                return content

        return content

    def toJSON(self):
        try:
            csvFile = pd.read_csv(self.filePath)
        except:
            csvFile = pd.read_csv(file_list[-1])
        df = pd.DataFrame(csvFile)
        result = df.to_json(orient="columns")
        parsed = json.loads(result)
        jsonFile = json.dumps(parsed, indent=4)
        self.content = jsonFile

    def saveFile(self):
        fileInput = self.content
        print(fileInput)
        fileOutput = open("Export.txt", "w+")
        value = list()
        for line in fileInput:
            value.append(line)
        for i in value:
            fileOutput.write(i)
        fileOutput.close()

def plot(root, canvas):
    df = pd.read_csv(file.getPath())
    df = pd.DataFrame(df)
    df.plot.bar(ax=ax)
    canvas.draw()





file = File()
convertButton = Button(root, text="Convert", command=lambda: file.toJSON())
selectButton = Button(root, text='Open', command=lambda: file.selectFile(file_list))
saveButton = Button(root, text="Back-up", command=lambda: file.saveFile())
plotButton = Button(root, text="Plot", command=lambda:plot(root,canvas))

selectButton.grid(row=1, column=1)
convertButton.grid(row=2, column=1)
saveButton.grid(row=3, column=1)
plotButton.grid(row=4, column=1)
button_bonus.grid(row=5, column =1)

canvas.get_tk_widget().grid(row=0, column=0)
mainloop()