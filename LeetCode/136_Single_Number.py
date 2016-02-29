# -*- coding: UTF-8 -*-

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
