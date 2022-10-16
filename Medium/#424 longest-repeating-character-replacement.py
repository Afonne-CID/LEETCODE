class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_f, res = 0, 0
        s_hash = {}

        while r < len(s):
            v = s[r]
            s_hash[v] = 1 + s_hash.get(v, 0)
            max_f = max(max_f, s_hash[v])
            if (r - l+1) - max_f > k:
                s_hash[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res