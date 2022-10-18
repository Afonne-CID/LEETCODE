from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = nums1, nums2
        if len(nums2) < len(nums1):
            l1, l2 = nums2, nums1
            
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2
        start, end = 0, len(l1) - 1
        
        while True:
            p1 = (start + end) // 2
            p2 = half - p1 - 2
            
            l1_l = l1[p1] if p1 >= 0 else float('-infinity')
            l1_r = l1[p1+1] if (p1 + 1) < len(l1) else float('infinity')
            
            l2_l = l2[p2] if p2 >= 0 else float('-infinity')
            l2_r = l2[p2+1] if (p2 + 1) < len(l2) else float('infinity')
            
            if l1_l <= l2_r and l2_l <= l1_r:
                if total % 2:
                    return max(l1_l, l2_l)
                    # return min(l1_r, l2_r)
                return (max(l1_l, l2_l) + min(l1_r, l2_r)) / 2
            elif l1_l > l2_r:
                end = p1 - 1
            else:
                start = p1 + 1