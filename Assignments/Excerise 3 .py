#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import numpy as np
import re
import string


# In[7]:


#cwd = os.getcwd()
#cwd = cwd + "\Python"
#os.chdir(cwd)
print(cwd)


# In[15]:


text = open("data.txt", "r") 
  
# Create an empty dictionary 
d = dict() 
  
# Loop through each line of the file 
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary 
for key in list(d.keys()): 
    print(key, ":", d[key]) 


# In[17]:


for key in list(d.keys()): 
    print(key, ":", d[key]) 


# In[ ]:




