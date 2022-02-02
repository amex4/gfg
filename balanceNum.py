#User function Template for python3
class Solution:
    def balancedNumber(self, N):
        s = str(N)
        l = 0
        r = 0
        mid = int(len(s)/2)
        for i in range(len(s)):
            if i < mid:
                l += int(s[i])
            if i > mid:
                r += int(s[i])
        if l == r:
            return True
        else :
            return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int (input ())
    for tc in range (t):
        N = input ()
        ob = Solution()
        if ob.balancedNumber(N):
            print (1)
        else:
            print (0) 
# } Driver Code Ends
