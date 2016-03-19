# DFS // do it later


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.answer = []
        self.remove(s)

    def remove(self, s):
        stack = []
        count = [0,]
        for letter in s:
            if letter == "(":
                stack.append(letter)
                count.append(count[-1]+1)
            if letter == ")":
                count.append(count[-1]-1)
                if stack:
                    stack.pop()
                else:
                    pass
            if count[-1] < -1:
                # '))'
                if s not in self.answer:
                    self.answer.append("")
            elif count[-1] == -1:
                for letter in s:
                    if letter == "(":
                        self.remove(s[0:s.index(letter)]+s[s.index(letter)+1:len(s)])



        if stack:
            # if recursive sub str
            for letter in s:
                if letter == "(":
                    self.remove(s[0:s.index(letter)]+s[s.index(letter)+1:len(s)])
        # any if match
        else:
            if s not in self.answer:
                self.answer.append(s)


def main():
    s = Solution()
    s.removeInvalidParentheses("())()()")
    print s.answer
    # s.removeInvalidParentheses(")(")
    # s.removeInvalidParentheses("())(((((")
    # s.removeInvalidParentheses(")))))asfa)))((((aasda(((((((bvxcbasad(((()(")


if __name__ == '__main__':
    main()
