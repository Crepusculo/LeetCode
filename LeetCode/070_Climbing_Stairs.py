# -*- coding: UTF-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

"""
This is my first time to deal with DP :)
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        f(N) = f(N-1) + f(N-2)
        """
        f = [0] * (n+1)
        f[0] = 1
        f[1] = 1
        i = 2
        while i <= n:
            f[i] = f[i-2] + f[i-1]
            i += 1
        return f[n]


def main():
    s = Solution()
    print s.climbStairs(5)

if __name__ == '__main__':
    main()
