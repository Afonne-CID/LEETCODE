class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, start = 0, 0
        s_hash = {}

        for i, v in enumerate(s):
            if v in s_hash and start <= s_hash[v]:
                start = s_hash[v] + 1
            else:
                longest = max(longest, (i - start) + 1)
            s_hash[v] = i
        return longest