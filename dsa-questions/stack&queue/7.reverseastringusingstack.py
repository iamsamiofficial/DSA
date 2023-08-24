#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    
    #Add code here
    # store = ""
    # i = len(S)
    # for i in range(len(S)-1,0,-1):
    #     store+=S[i]
    # store+=S[0]
    # return store
    s = ""
    stack = []
    for i in range(len(S)):
        stack.append(S[i])
    
    while stack:
        s+= stack.pop()
    return s
        

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends