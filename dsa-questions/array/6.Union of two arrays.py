#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        return len(set(a+b))
        

        
        
        # for i in b:
        #     if i not in a:
        #         n+=1
        #     else:
        #         continue
        # return n
        # for i in b:
        #     if i not in a:
        #         a.append(i)
        #     else:
        #         continue
        # return len(a)
