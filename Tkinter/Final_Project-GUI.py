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
    
    
    def __init__(self):
        self.content = content
    
    def selectFile():
        file = askopenfile(mode ='r', filetypes =[('Comma-Delimited', '*.csv')]) 
        if file is not None: 
           content = file.read() 
           return(content)
          
     
        def toJSON():    
            content = File.selectFile()
            csvFile = pd.read_csv(content)
            df = pd.DataFrame(csvFile)
            jsonFile = df.to_json(orient="split")
            asksaveasfile(jsonFile, defaultextension = ".JSON") 
        
        toJSON()
       

        
convertButton = Button(root, text = "Convert", command = lambda: File.toJSON())      
btn = Button(root, text ='Open', command = lambda: File.selectFile()) 
btnTwo = ttk.Button(root, text = 'Save', command = lambda : save()) 
btnTwo.pack(side = TOP, pady = 20) 
  


btn.pack(side = TOP, pady = 10) 
convertButton.pack(side = TOP, pady = 10)
  
mainloop() 