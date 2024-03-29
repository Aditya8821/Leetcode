#User function Template for python3

class Solution:
    def moveRobots (self, s1, s2):
        # code here 
        if len(s1)!=len(s2):
            return "No"
        bots=[]
        for i in range(len(s1)):
            if s1[i]=="A" or s1[i]=="B":
                bots.append(i)
        b=0
        for j in range(len(s2)):
            if s2[j] == "A" or s2[j]=="B":
                if b==len(bots) or s1[bots[b]]!=s2[j] or \
                (s2[j]=="A" and j>bots[b]) or \
                (s2[j]=="B" and j<bots[b]):
                    return "No"
                b+=1
        return "Yes" if b==len(bots) else "No"

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s1 = input()
        s2 = input()

        ob = Solution()
        print(ob.moveRobots(s1, s2))

# } Driver Code Ends