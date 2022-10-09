from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n, new_list = 0, []
        for num in nums:
            for each in new_list:
                if (num + each) == target:
                    if each == num:
                        return ([nums.index(each), nums.index(num, n, len(nums))])
                    return ([nums.index(each), nums.index(num)])
            n += 1
            new_list.append(num)