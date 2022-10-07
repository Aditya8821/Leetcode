class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxw=0
        for i in sentences:
            words=i.split(" ")
            maxw=max(maxw,len(words))
        return maxw