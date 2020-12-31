import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import pandas as pd

LARGEFONT = ("Verdana", 35)


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


        lab = ttk.Label(frame, text="Welcome \n to the App", font = self.Font, background = '#33D1F6')
        lab.grid(column=2, row=2)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

    # third window frame page2


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

    # Driver Code

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


app = RestaurantApp()
app.minsize(500,500)
app.maxsize(500,500)
app.mainloop()
