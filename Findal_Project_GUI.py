# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:32:06 2020

@author: ryanm
"""

from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 

import pandas as pd
import json
  
root = Tk() 
root.geometry('200x200') 


  
# This function will be used to open 
# file in read mode and only Python files 
# will be opened 


def selectFile(): 
    file = askopenfile(mode ='r', filetypes =[('Comma-Delimited', '*.csv')]) 
    if file is not None: 
        content = file.read() 
        csvFile = pd.read_csv(content)
        df = pd.DataFrame(content)
        jsonFile = df.to_json(orient="split")
        json.dumps(jsonFile)
        return(content) 
    
    def convertFile():
        csvFile = pd.read_csv(content)
        df = pd.DataFrame(content)
        jsonFile = df.to_json(orient="split")
        print(content)
        return(jsonFile)
    
       
       
        
convertButton = Button(root, text = "Convert", command = lambda:convertFile())      
btn = Button(root, text ='Open', command = lambda:selectFile()) 

btn.pack(side = TOP, pady = 10) 
convertButton.pack(side = TOP, pady = 10)
  
mainloop() 