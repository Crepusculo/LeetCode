class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = list()
        self.sums.append(0)
        for i in range(len(nums)):
            sumi = self.sums[i] + nums[i]
            self.sums.append(sumi)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

def main():
    s = NumArray([-1,3,-6,3])
    print s.sumRange(1,3)

if __name__ == '__main__':
    main()
