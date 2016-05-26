# -*- coding: UTF-8 -*-
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it wou
ld be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        if target <= nums[start]:
            return 0
        end = len(nums)
        cur = 0
        while end - start > 0:
            cur = (start + end) / 2
            if start == cur:
                return start + 1
            if target > nums[cur]:
                start = cur
            elif target < nums[cur]:
                end = cur
            else:
                return cur

        return cur


def main():
    s = Solution()
    print s.searchInsert([11], 12)  # 4 6

if __name__ == '__main__':
    main()
