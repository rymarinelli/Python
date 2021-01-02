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
from tkinter import messagebox
import sys
import sqlite3

# The input is going to be three csv files
# You will need to prompt for input and join them
# Use try catch logic


def popup_bonus():
    value = File()
    value.process = True
    win = Toplevel()
    win.wm_title("Window")

    l = Label(win, text="Input")
    l.grid(row=0, column=0)

    b = Button(win, text="Okay", command=win.destroy)
    b_1 = Button(win, text="Add_Data", command= lambda: file.setFile())
    b.grid(row=1, column=0)
    b_1.grid(row=2,column=0)


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

    l = Label(win, text="Group By")
    l.grid(row=0, column=0)

    b = Button(win, text="Finished", command=win.destroy)
    b_1 = Button(win, text="Seating", command=lambda:set_Query())
    b_2 = Button(win, text="Zip Codes", command=lambda:set_Query_1())
    b_3 = Button(win, text="Seating & Zip Codes", command=lambda: set_Query())

    b.grid(row=1, column=0)
    b_1.grid(row=2, column=0)
    b_2.grid(row=3, column = 0)
    b_3.grid(row=4, column = 0)

def set_Query():
    conn = sqlite3.connect('TestDB.db')
    df = pd.read_csv('C:\\Users\\rmarinelli4\\Downloads\\combined_test.csv')
    df.columns = df.columns.str.replace(' ', '_')
    try:
        df.to_sql('DATASET', conn, if_exists='append', index=False)
    except:
        pass
    test = conn.execute('''SELECT AVG(Score)
                            FROM DATASET
                            GROUP BY Year, Seating ''')
    test = test.fetchall()
    print(test)

def set_Query_1():
    conn = sqlite3.connect('TestDB.db')
    df = pd.read_csv('C:\\Users\\rmarinelli4\\Downloads\\combined_test.csv')
    df.columns = df.columns.str.replace(' ', '_')
    try:
        df.to_sql('DATASET', conn, if_exists='append', index=False)
    except:
        pass
    test = conn.execute('''SELECT AVG(Score)
                            FROM DATASET
                            GROUP BY Year, Zip_Codes ''')
    test = test.fetchall()
    print(test)

def set_Query_2():
    conn = sqlite3.connect('TestDB.db')
    df = pd.read_csv('C:\\Users\\rmarinelli4\\Downloads\\combined_test.csv')
    df.columns = df.columns.str.replace(' ', '_')
    try:
        df.to_sql('DATASET', conn, if_exists='append', index=False)
    except:
        pass
    test = conn.execute('''SELECT AVG(Score)
                            FROM DATASET
                            GROUP BY Year, Zip_Codes, Seating ''')
    test = test.fetchall()
    print(test)


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
button_Query = Button(root, text="Query_Button", command=generate_Report)


# This function will be used to open
# file in read mode and only Python files
# will be opened

file_list = list()

class File():

    def __init__(self):
        self.content = ""
        self.filePath = ""
        self.process = True


    def setFile(self):
        downloads = str(os.path.join(Path.home(), "Downloads"))
        file_path = downloads + "\combined_test.csv"
        #file = self.selectFile(file_list)


        print('Making sure there are no None values in file_path')
        [path for path in file_list if path is not None]

        while len(file_list) <= 2:
            print("Trying to add file")
            file = self.selectFile(file_list)
            try:
                df = pd.read_csv(file_list[0])
            except:
                df = pd.read_csv(self.filePath)

            try:
                df_2 = pd.read_csv(file_list[-1])
            except:
                continue


            print("Waiting for the for loop")
            for f in range(1,len(file_list)):
                print("Entering for loop")
                try:
                    print(file_list)
                    df_1 = pd.read_csv(file_list[f])

                    df_2 = pd.concat([df.reset_index(drop=True), df_1], axis=1)
                    print('File finished combining')
                except:
                    print(file_list)
                    self.selectFile(file_list)

                #combined_csv = df_2
                #combined_csv.to_csv(file_path, index=False)

            if len(file_list) >= 3:
                print("This is when we are finished the loop")
                combined_csv.to_csv(file_path, index=False)
                break

            else:
                file = self.selectFile(file_list)

            combined_csv = df_2
            combined_csv.to_csv(file_path, index=False)
            #break


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
    def selectFile(self, file_list):
        if len(file_list) < 3 and self.process is True:
            file = askopenfile(mode='r', filetypes=[('Comma-Delimited', '*.csv')])
            print(file.name)
            try:
                self.filePath = file.name
            except:
                file.name = ""
        else:
            messagebox.showwarning("Warning", "File Limit reached ")
            print("I should close the window")
            #root.quit()
            #root.update()

        if len(file_list) == 3:
            print("I should warn the end user")
            messagebox.showwarning("Warning", "File Limit reached")

        try:
            if file is not None and self.process is True:
                content = file.read()
                file_list.append(self.filePath)
                self.filePath = None

            if len(file_list) >= 3 and self.process is True:
                file_list.clear()
                print("Assign File Path")
                downloads = str(os.path.join(Path.home(), "Downloads"))
                file_path = downloads + "\combined_test.csv"
                self.filePath = file_path

                test = File()
                print("Cleaning File")
                test.data_Cleaner(file_path)
                print("File Cleaned")
                content = pd.read_csv(file_path)
                print(content)
                self.process = False
        except:
            self.process = True
            return self.process

            #return self.content

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

    def data_Cleaner(self, path):
        df = pd.read_csv(path)
        def program_Status(df):
            program_status = df['PROGRAM STATUS'] == 'ACTIVE'
            df = df[program_status]
            return df

        program_Status(df)

        def extract_Data(df):
            establishment_list = list()
            risk_list = list()
            value_list = list()

            for i in range(0, len(df)):
                try:
                    description = df['PE DESCRIPTION'][i]
                    inspect_match = re.findall('[A-Z]+', description)
                    establishment = inspect_match[0]
                    risk = inspect_match[2] + " " + inspect_match[3]
                    value = description[description.find("(") + 1:description.find(")")]

                    establishment_list.append(establishment)
                    risk_list.append(risk)
                    value_list.append(value)
                except:
                    establishment_list.append("Place-Holder")
                    risk_list.append("Place-Holder")
                    value_list.append(0)
                    continue

            est = pd.Series(establishment_list)
            r = pd.Series(risk_list)
            val = pd.Series(value_list)

            df['Establishment'] = est.values
            df['Risk'] = r.values
            df["Seating"] = val.values

            return (df)

        extract_Data(df)

        def extract_Year(df):
            selected_columns = df[['SCORE', 'Zip Codes', 'Seating', 'ACTIVITY DATE']]
            year_list = list()

            for i in df['ACTIVITY DATE']:
                year = re.findall(r'[0-9][0-9][0-9][0-9]', i)
                year_list.append(year[0])
            year_series = pd.Series(year_list)
            df['Year'] = year_series.values
            return (df)

        extract_Year(df)

        df.to_csv(path)

def plot(root, canvas):
    df = pd.read_csv(file.getPath())
    df = pd.DataFrame(df)
    df.plot.bar(ax=ax)
    canvas.draw()


file = File()
queryButton = Button(root, text="Query", command=lambda: file.toJSON())
convertButton = Button(root, text="Convert", command=lambda: file.toJSON())
selectButton = Button(root, text='Open', command=lambda: file.selectFile(file_list))
saveButton = Button(root, text="Back-up", command=lambda: file.saveFile())
plotButton = Button(root, text="Plot", command=lambda:plot(root,canvas))

selectButton.grid(row=1, column=1)
convertButton.grid(row=2, column=1)
saveButton.grid(row=3, column=1)
plotButton.grid(row=4, column=1)
button_bonus.grid(row=5, column =1)
button_Query.grid(row=6,column=1)

canvas.get_tk_widget().grid(row=0, column=0)
mainloop()