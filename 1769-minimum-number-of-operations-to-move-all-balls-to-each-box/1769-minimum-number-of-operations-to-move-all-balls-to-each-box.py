class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        sumAhead = ballsAhead = ballsBehind = 0
               
        for i in range(1, len(boxes)):
            if boxes[i] == '1':
                sumAhead += i
                ballsAhead += 1
        
        ans[0] = sumAhead
        
        if boxes[0] == '1':
            ballsBehind += 1
        
        for i in range(1, len(ans)):
            ans[i] = ans[i - 1] + ballsBehind - ballsAhead
            
            if boxes[i] == '1':
                ballsBehind += 1
                ballsAhead -= 1
            
        return ans