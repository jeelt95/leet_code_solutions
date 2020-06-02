class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                    stack.append(s[i])
            if (len(stack) > 0):
                if (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                    if (stack[len(stack)-1] == '(' and s[i] == ')') or \
                    (stack[len(stack)-1] == '{' and s[i] == '}') or \
                    (stack[len(stack)-1] == '[' and s[i] == ']'):
                        del stack[len(stack)-1]
                    else:
                        return False
            else:
                return False
        return len(stack)==0

s = Solution()
st = "([)]"
print(s.isValid(st))