class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''
        for i in range(len(s)):
            if len(res) == 0:
                if s[i] == ' ':
                    continue
                if s[i] == '-' or s[i] == '+':
                    res += s[i]
                    continue
            if (not 48 <= ord(s[i]) <= 57):
                break
            res += s[i]
        if (not len(res)) or (len(res) == 1 and (res == '-' or res == '+')):
            res = 0
        return max(-2**31, min(int(res), 2**31-1))