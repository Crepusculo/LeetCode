from random import randint


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mdict = {}
        for i in nums:
            if i in mdict:
                # exist
                return i
                pass
            else:
                # not exist
                mdict[i] = 1


def main():
    s = Solution()
    while True:
        print "Aloha!"
        nums = [randint(1, 10) for i in range(20)]
        print nums
        print s.findDuplicate(nums)
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
