# DFS // do it later


class Solution(object):
    def match(self, s):
        num = 0
        stack = list()
        for each in s:
            if each == '(':
                stack.append(each)
            elif each == ')':
                if stack:
                    stack.pop()
                else:
                    num += 1
                    self.sta = self.status[1]
        num += len(stack)
        if num > 0 and not self.sta:
            self.sta = self.status[2]
        # print num, s, stack
        return num

    def dfs(self, s, num):
        newnum = num
        tar = self.sta
        if num == 0:
            self.result.append(s)
            return
        for letter in range(len(s)):
            if s[letter] == tar:
                # if s[letter] != '(' and s[letter] != ')':
                #     # print "continue!"
                #     continue
                if letter - 1 > 0:
                    if s[letter - 1] == s[letter]:
                        # print "continue!"
                        continue
                sub = s[0:letter] + s[letter + 1:len(s)]
                newnum = self.match(sub)
                # print sub
                if sub in self.result:
                    continue
                if newnum < num:
                    self.dfs(sub, newnum)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.sta = 0
        self.status = ("m", ")", "(")
        ctl = 0
        ctr = 0
        for each in s:
            if each == ')':
                ctl += 1
            else:
                break
        for each in s[::-1]:
            if each == '(':
                ctr += 1
            else:
                break
        s = s[ctl:len(s) - ctr]
        # print s
        self.result = []
        num = self.match(s)
        self.dfs(s, num)
        return self.result


def main():
    s = Solution()
    # s.removeInvalidParentheses("()(()()")
    # print s.result
    # s.removeInvalidParentheses(")(")
    # print s.result
    # s.removeInvalidParentheses("())(((((")
    # print s.result
    s.removeInvalidParentheses(")(((()(y((u()(z()()")
    print s.result


if __name__ == '__main__':
    main()
