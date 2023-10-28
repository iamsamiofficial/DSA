class Solution:
    def overlappedInterval(self, Intervals):
        Intervals.sort(key = lambda i : i[0])
        output = [Intervals[0]]
        
        for start,end in Intervals[1:]:
            if start <= output [-1][1]:
                output[-1][1] = max(output[-1][1],end)
            else:
                output.append([start,end])
        return output
		        


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    
    T=int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().strip().split()))
        Intervals = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            Intervals.append([x,y])
        obj = Solution()
        ans = obj.overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j, end = " ")
        print()
# } Driver Code Ends