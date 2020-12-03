
from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import asksaveasfile 

import pandas as pd
import json
  
root = Tk() 
root.geometry('200x200') 


  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 




class File():
    
    def __init__(self):
        self.content = ""
        
    def setFile(self):
        file = self.selectFile()
        self.content = file
           
        
        
    def getFile(self):
        print("Getting value...")
        return self.content


    def selectFile(self):
        file = askopenfile(mode ='r', filetypes =[('Comma-Delimited', '*.csv')]) 
        if file is not None: 
           content = file.read() 
           return(content)
    
       
    def toJSON(self):
        content = self.getFile()
        csvFile = pd.read_csv(content)
        df = pd.DataFrame(csvFile)
        jsonFile = df.to_json(orient="split")
        return(jsonFile)
        
       
    fileProperty = property(getFile, setFile)

file = File()
convertButton = Button(root, text = "Convert", command = lambda: file.toJSON())      
btn = Button(root, text ='Open', command = lambda: file.setFile()) 
btnTwo = ttk.Button(root, text = 'Save', command = lambda : file.getFile()) 
btnTwo.pack(side = TOP, pady = 20) 
  


btn.pack(side = TOP, pady = 10) 
convertButton.pack(side = TOP, pady = 10)
  
mainloop() 