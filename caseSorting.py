
#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,S,n):
        u = []
        l = []
        for i in S:
            if i.isupper():
                u.append(i)
            else:
                l.append(i)
        l.sort()
        u.sort()
        r = ''
        for i in S:
            if i.islower():
                r = r + l[0]
                del l[0]
            else:
                r = r + u[0]
                del u[0]
        return r
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends
