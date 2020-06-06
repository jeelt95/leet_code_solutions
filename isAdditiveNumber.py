class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if(len(num) <= 0):
            return False
        if(len(num) <= 2):
            return False
        if(num[0]=='0'and num[1]!='0'):
            return False
        idxx = 0
        isAdditive = True
        isValid = True
        for i in range(len(num)):
            for inc in range(i, len(num)):
                if (i == 0):
                    break
                isValid = True
                i = 0
                idx = 0
                idxx = 0
                third = num[idx:idxx]
                first = int(num[i])
                second = int(num[i+1:i+inc+1])
                while(idxx < len(num)):
                    if isValid == False:
                        break
                    third = str(first + second)
                    first = str(first)
                    second = str(second)
                    idx = i+len(first)+len(second)
                    idxx = i+len(first)+len(second)+len(third)
                    i += 1
                    if(third != num[idx:idxx]):
                        isValid = False
                        break
                    else:
                        first = int(second)
                        second = int(third)

            if isValid == True:
                return isValid
        return isValid

s = Solution()
num = "211738"
print(s.isAdditiveNumber(num))