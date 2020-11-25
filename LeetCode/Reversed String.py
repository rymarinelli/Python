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
        
        # Look if negative
        if(result.endswith("-") == True):
            result = "-" + result[0:-1]
            
            # Removes last zero and slices position after
            if(result.startswith("0") == True and len(result) > 1):
                result = result[(result.rfind("0") + 1): len(result)]
                result = "-" + result[0:-1]
                print(result)
            return(result)
        
        #If not negative
        else:
            if(result.startswith("0") == True and len(result) > 1):
                result = result[(result.rfind("0") + 1): len(result)]
                return(result)
            
        return(result)
        
        