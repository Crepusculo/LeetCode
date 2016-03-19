class Solution(object):
    def isPowerOfThree(self, n):
        """
        Given an integer, write a function to determine if it is a power of three.
        Follow up:      Could you do it without using any loop / recursion?
        :type n: int
        :rtype: bool
        """
        max_3power_int = 1162261467
        if n <= 0 or n > max_3power_int:
            return False
        return max_3power_int % n == 0
