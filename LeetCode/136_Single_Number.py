# -*- coding: UTF-8 -*-
"""
1: +1s重复元素
2: 删除重复元素
删除有额外性能开销, 但是最后不需要遍历
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mdict = {}
        for i in nums:
            if i in mdict:
                # exist
                mdict[i] += 1
                pass
            else:
                # not exist
                mdict[i] = 1

        for i in mdict:
            if mdict[i] == 1:
                return mdict[i]


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mdict = {}
        for i in nums:
            if i in mdict:
                # exist
                del mdict[i]
                pass
            else:
                # not exist
                mdict[i] = 1

        for i in mdict:
            if mdict[i] == 1:
                return i