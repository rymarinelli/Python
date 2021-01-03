import pandas as pd
import os
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from pathlib import Path
import sqlite3
import json

file_list = list()

class File():
    def __init__(self):
        self.content = "Data Not Selected"
        self.filePath = ""
        self.process = True

    def setProcess(self, complete):
        self.process = complete

    def setContent(self):

        conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
        print("Opened database successfully")

        try:
            conn.execute('''CREATE TABLE DATASET
            (
                ACTIVITY_DATE         date,
                OWNER_ID              text,
                OWNER_NAME            text,
                FACILITY_ID           text PRIMARY KEY,
                FACILITY_NAME         text, 
                RECORD_ID             text,
                PROGRAM_NAME          text,
                PROGRAM_STATUS        text,
                PROGRAM_ELEMENT (PE)  text,
                PE_DESCRIPTION        text,
                FACILITY_ADDRESS      text,
                FACILITY_CITY	      text,
                FACILITY_STATE	      text,
                FACILITY_ZIP          text,
                SERVICE_CODE          text,
                SERVICE_DESCRIPTION   text,	
                SCORE                 integer,
                GRADE                 text,
                SERIAL_NUMBER         text,
                EMPLOYEE_ID           text,
                Location               text,
                2011_Supervisorial_District_Boundaries_(Official)	text,
                Census_Tracts_2010    text,
                Board_Approved_Statistical_Areas	text,
                Zip_Codes	          text,
                Establishment         text,
                Risk                  text,
                Seating               text,
                Year                  date
                );''')
        except:
            print('Updating Database')
            df = pd.read_csv('C:\\Users\\rmarinelli4\\Downloads\\combined_test.csv')
            df.columns = df.columns.str.replace(' ', '_')
            df.to_sql('DATASET', conn, if_exists='replace', index=False)





    def getContent(self):
        conn = sqlite3.connect('TestDB.db')
        content = conn.execute('''SELECT *
                                   FROM DATASET
                                   ''')

        content = content.fetchall()
        return content

    def setFile(self):
        downloads = str(os.path.join(Path.home(), "Downloads"))
        file_path = downloads + "\combined_test.csv"
        #file = self.selectFile()


        print('Making sure there are no None values in file_path')
        [path for path in file_list if path is not None]

        if len(file_list) <= 3 and self.process is True:
            while len(file_list) <= 3 and self.process is True:
                print("Trying to add file")
                self.selectFile(file_list)

                print('Checking status of self.process')
                print(self.process)
                #After the data is created, there is nothing left in the file list
                #This creates a flaw right here
                try:
                    df = pd.read_csv(file_list[0])
                    df_2 = pd.read_csv(file_list[-1])
                except:
                    df = pd.read_csv(file_path)
                    df_2 = pd.read_csv(file_path)

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

                if len(file_list) >= 3 and self.process is True:
                    print('Data is being combined')
                    print(file_list)
                    combined_csv = df_2
                    print('Testing to see if combined csv if here')
                    combined_csv.to_csv(file_path, index=False)
                    combined_csv = self.data_Cleaner(file_path)
                    combined_csv.to_csv(file_path, index=False)
                    self.setContent()
                    return print('Done')




    def setPath(self, path):
        path = self.filePath
        return path

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
        print('Hi, I am at start of the function')
        if self.process is False:
            return('Self Process is still False')

        if len(file_list) <= 3 and self.process is True:
            print('Hi, I am in the  control flow')
            file = askopenfile(mode='r', filetypes=[('Comma-Delimited', '*.csv')])
            print('Seeing if there is a name')
            print(file.name)
            print(self.process)

            if file is not None and self.process is True:
                print('Hi, I am trying to read the file')
                file_list.append(file.name)
                print('Testing that data is appended')
                print(file_list)
                self.filePath = None

            if len(file_list) > 3 and self.process is True:
                file_list.clear()
                print("Assign File Path")
                downloads = str(os.path.join(Path.home(), "Downloads"))
                file_path = downloads + "\combined_test.csv"
                self.filePath = file_path

                print("Cleaning File")
                self.data_Cleaner(file_path)
                print("File Cleaned")
                self.setProcess(False)

            #self.process = True
            #return self.process

            #return self.content

    def toJSON(self):
        print('Getting Content')
        file = self.getContent()
        print('Creating DataFrame')
        df = pd.DataFrame(file)
        print('Convert to JSON')
        downloads = str(os.path.join(Path.home(), "Downloads"))
        file_path = downloads + "\combined_test.json"
        df.to_json(file_path, orient='columns')

    def saveFile(self):
        print('Starting Save file')
        #fileInput = self.getFile()
        print(self.getContent())
        #print("Well it didn't seem to save correctly")
        #fileOutput = open("Export.txt", "w+")
        #value = list()
        #for line in fileInput:
        #    value.append(line)
        #for i in value:
        #    fileOutput.write(i)
        #fileOutput.close()

    def data_Cleaner(self, path):

        print('Starting cleaning in fuction')
        df = pd.read_csv(path)

        df = df.dropna()

        print('Starting fixing program status')
        def program_Status(df):
            program_status = df['PROGRAM STATUS'] == 'ACTIVE'
            df = df[program_status]
            return df

        program_Status(df)

        print('Extracting Data')
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

        print('Extracting year')
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
        print('Setting cleaned data to content')
        return df

    def restart(self):
        self.setProcess(True)
