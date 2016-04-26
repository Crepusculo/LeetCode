class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = list()
        tail = list()
        for i in range(rowIndex/2 + 1):
            result.append(self.c(i, rowIndex))
        if rowIndex % 2:
            tail = result[::-1]
        else:
            tail = result[-2::-1]

        result += tail
        return result

    def c(self, k, n):
        if n == 0:
            return 1
        numerator = 1
        denominator = 1

        cur = n-k+1
        while cur <= n:
            denominator *= n
            print "n", n
            n -= 1
        while 0 < k:
            numerator *= k
            print "k", k
            k -= 1

        return denominator / numerator


def main():
    s = Solution()
    print s.getRow(4)

if __name__ == '__main__':
    main()