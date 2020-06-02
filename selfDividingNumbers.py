from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        if left == right:
            isValid = True
            while(left > 0):
                r = left % 10
                left = int((left-r) / 10)
                if r == 0:
                    isValid = False
                    break
                else:
                    if right % r != 0:
                        isValid = False
                        break
            if isValid == True:
                res = [right]
                return res
            else:
                return []
        mid = int((left + right)/2)
        
        return self.selfDividingNumbers(left, mid) + self.selfDividingNumbers(mid+1, right)

s = Solution()
left = 1
right = 22
print(s.selfDividingNumbers(1, 22))