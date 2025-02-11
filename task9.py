# Finding the median of given arrays after merge

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        half_len = (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums1[i] < nums2[j - 1]:
                # i is too small, increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: left_max = nums2[j - 1]
                elif j == 0: left_max = nums1[i - 1]
                else: left_max = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return left_max

                if i == m: right_min = nums2[j]
                elif j == n: right_min = nums1[i]
                else: right_min = min(nums1[i], nums2[j])

                return (left_max + right_min) / 2.0