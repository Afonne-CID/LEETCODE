class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        if x < 0:
            res = -res
        return res if (res <= 2**31 - 1 and res >= -2**31) else 0