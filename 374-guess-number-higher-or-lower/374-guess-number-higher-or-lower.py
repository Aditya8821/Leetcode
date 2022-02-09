# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n+1
        while True:
            m = int((l+h)//2)
            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                h = m
            else:
                l = m