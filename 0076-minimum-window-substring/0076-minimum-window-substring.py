class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt={}
        for ch in t:
            dt[ch]=dt.get(ch,0)+1
        start,matched=0,0
        minwindow=s
        minwindowlen=len(s)+1
        for end in range(len(s)):
            rightchar=s[end]
            if rightchar in dt:
                dt[rightchar]-=1
                if dt[rightchar]==0:
                    matched+=1
            while matched==len(dt):
                if end-start+1<minwindowlen:
                    minwindow=s[start:end+1]
                    minwindowlen=len(minwindow)
                leftchar=s[start]
                start+=1
                if leftchar in dt:
                    if dt[leftchar]==0:
                        matched-=1
                    dt[leftchar]+=1
        if minwindowlen==len(s)+1: return ""
        return minwindow
        