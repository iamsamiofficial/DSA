#User function Template for python3


#dq : deque in which element is to be pushed
#x : element to be pushed


#Function to push element x to the front of the deque.
def push_front_pf(dq,x):
    #code 
    dq.append(x)
    dq = dq.reverse()
    

#Function to push element x to the back of the deque.
def push_back_pb(dq,x):
    #code here
    dq.append(x)
    
#Function to return element from front of the deque.
def front_dq(dq):
    #code here
    return dq[0] if dq else -1
    
#Function to pop element from back of the deque.
def pop_back_ppb(dq):
    #code here
    dq.pop() if dq else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    from collections import deque

    tcs=int(input())

    for _ in range(tcs):

        dq=deque()

        n=int(input())

        for _ in range(n):
            qry=input().split()

            if qry[0]=='pf':
                x=int(qry[1])
                push_front_pf(dq,x)
                print(dq[0])

            elif qry[0]=='pb':
                x=int(qry[1])
                push_back_pb(dq,x)
                print(dq[-1])

            elif qry[0]=='pp_b':
                pop_back_ppb(dq)
                print(len(dq))

            else:
                x=front_dq(dq)
                print(x)

# } Driver Code Ends