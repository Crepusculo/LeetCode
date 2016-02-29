
from random import randint, choice


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            for i in range(len(nums)):
                if (i is not 0) and (i is not len(nums)-1):
                    # mid
                    if (nums[i] > nums[i-1]) and (nums[i] > nums[i+1]):
                        # is peak
                        # print nums[i-1], nums[i], nums[i+1]
                        return i
                    else:
                        # is not peak
                        pass
                elif i is 0:
                    # head
                    if nums[0] > nums[1]:
                        return i
                elif i is len(nums)-1:
                    # tail
                    if nums[i] > nums[i-1]:
                        return i
                    pass
        elif len(nums) == 1:
            return 0


def main():
    s = Solution()
    while True:
        print "Aloha!"
        nums = [randint(1, 2) for i in range(2)]
        print nums
        print s.findPeakElement(nums)
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



