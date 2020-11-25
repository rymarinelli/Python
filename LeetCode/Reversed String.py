# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:46:33 2020

@author: ryanm
"""


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        val = list()
        reversed_val = list()
        result = str()
        
        for i in range(len(x)):
            val.append(x[i])
        
        for i in range(len(val)):
            reversed_val.append(val.pop())
            
        for i in reversed_val:
            result += i
        
        if(result.endswith("-") == True):
            result = "-" + result[0:-1]
            if(result[1] == "0"):
                result = result[0] + result[2:]
            
        
        if(result.startswith("0") == True and len(result) > 1):
            result = result[(result.rfind("0") + 1): len(result)]
            print(result)
            return(result)
        
        
            
        return(result)
        
        