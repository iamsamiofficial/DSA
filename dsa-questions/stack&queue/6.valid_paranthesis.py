#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        close = {")":"(","}":"{","]":"["}
        res = []
        for i in x:
            if i in close:
                if res and res[-1] == close[i]:
                    res.pop()
                else:
                    return False
            else:
                res.append(i)
        return True if not res else False
        # code here
        # res=[]
        # i = 0
        # j = len(x)-1
        # a = '('
        # b = ')'
        # c = '{'
        # d = '}'
        # e = '['
        # f = ']'
        # if len(x)==1:
        #     return False
        # else:
        #     while i<len(x):
        #         if x[i]==a or x[i] == c or x[i] == e:
        #             res.append(x[i])
        #             i+=1
                    
        #         elif (x[i] == b and res[-1] == a):
        #             res.pop()
        #             i+=1
        #         elif (x[i] == d and res[-1] == c):
        #             res.pop()
        #             i+=1
        #         elif (x[i] == f and res[-1] == e):
        #             res.pop()
        #             i+=1
                
                
        #     if len(res) == 0:
        #         return True
        #     else:
        #         return False
        
