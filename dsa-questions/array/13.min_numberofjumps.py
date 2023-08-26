#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        #code here
        hold = 0
        maxi =0
        res = 0
        i = 0
        while i<len(arr):
            
            if hold>= len(arr)-1:
                break
            if maxi == hold and arr[maxi] == 0:
                return -1
            elif i==hold:
                maxi = max(maxi,arr[i]+i)
                hold = maxi
                i+=1
                maxi = max(maxi,arr[i]+i)
                res+=1
                
            else:
                maxi = max(maxi,arr[i]+i)
                i+=1
        return res
