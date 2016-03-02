# -*- coding: UTF-8 -*-
from random import randint


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num > 0:
                d[num] = num + 1
        i = 1
        while True:
            if i in d:
                i += 1
                continue
            else:
                return i


def main():
    s = Solution()
    while True:
        print "Aloha!"
        nums = [randint(-3, 10) for i in range(30)]
        print nums
        print s.firstMissingPositive(nums)

        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
            else:
                pass
        except (KeyboardInterrupt,EOFError):
            break


if __name__ == '__main__':
    main()
