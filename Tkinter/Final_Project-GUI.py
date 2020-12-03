# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:32:06 2020

@author: ryanm
"""

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
    
    def __init__(self, content):
        self.content = content
        
    def setFile(self):
        file = selectFile()
        self.content = file
           
        
        
    def getFile(self):
        print("Getting value...")
        return self.content


    def selectFile():
        file = askopenfile(mode ='r', filetypes =[('Comma-Delimited', '*.csv')]) 
        if file is not None: 
           content = file.read() 
           return(content)
    
       
    def toJSON():
        content = File.getFile()
        csvFile = pd.read_csv(content)
        df = pd.DataFrame(csvFile)
        jsonFile = df.to_json(orient="split")
        return(jsonFile)
        
       
    fileProperty = property(getFile, setFile)

          
convertButton = Button(root, text = "Convert", command = lambda: File.toJSON(File.content))      
btn = Button(root, text ='Open', command = lambda: File.setFile()) 
btnTwo = ttk.Button(root, text = 'Save', command = lambda : File.getFile()) 
btnTwo.pack(side = TOP, pady = 20) 
  


btn.pack(side = TOP, pady = 10) 
convertButton.pack(side = TOP, pady = 10)
  
mainloop() 