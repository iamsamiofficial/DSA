#User function Template for python3

def reverseWord(s):
    #your code here
    j = ""
    i = len(s)-1
    while i>=0:
        j+= s[i]
        i-=1
    return j
