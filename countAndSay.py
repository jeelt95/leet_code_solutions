class Solution:
    def getGroups(self, n, res):
        next_res = ""
        if len(res) == 1:
            return "1"+res
        groups = []
        curr_group = ""
        for i in range(0, len(res)):
            if i == 0:
                pass
            if(res[i] == res[i-1]):
                curr_group += res[i]
            else:
                if curr_group != "":
                    groups.append(curr_group)
                curr_group = res[i]

        if curr_group != "":
            groups.append(curr_group)
        for group in groups:
            next_res += str(len(group))+group[0]
        return next_res

    def countAndSay(self, n: int) -> str:
        if (n==1):
            return "1"
        return self.getGroups(n-1, self.countAndSay(n-1))

s = Solution()
print("result", s.countAndSay(5))