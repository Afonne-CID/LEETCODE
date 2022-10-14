class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_vals, window = {}, {}
        l, res = 0, [-1, -1]
        res_len = float("infinity")

        for v in t:
            t_vals[v] = 1 + t_vals.get(v, 0)

        need, have = len(t_vals), 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_vals and window[c] == t_vals[c]:
                have += 1

            while have == need:
                if ((r - l) + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l) + 1

                b = s[l]
                window[b] -= 1
                if b in t_vals and window[b] < t_vals[b]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float('infinity') else ''            
