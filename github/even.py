class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in s :
            if abs(s[i]-s[i+1]) <=2 :
                return True
            else :
                return False
s=Solution(123)
s.isAdjacentDiffAtMostTwo()