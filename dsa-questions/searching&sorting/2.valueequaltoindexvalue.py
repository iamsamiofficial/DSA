#User function Template for python3
class Solution:

    def valueEqualToIndex(self,arr, n):
        # code here
        sami = []
        i = 0
        while i <len(arr):
            if (i+1) == arr[i]:
                sami.append(i+1)
                i+=1
            else:
                i+=1
        return sami
