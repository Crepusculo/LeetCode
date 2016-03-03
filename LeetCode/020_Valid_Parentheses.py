class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for letter in s:
            # letter = copy.deepcopy(copys)
            if letter == "(" or letter == '{' or letter == "[":
                stack.append(letter)
            elif letter == ')':
                if len(stack):
                    if stack.pop() == '(':
                        continue
                return False
            elif letter == '}':
                if len(stack):
                    if stack.pop() == '{':
                        continue
                return False
            elif letter == ']':
                if len(stack):
                    if stack.pop() == '[':
                        continue
                return False
            else:
                return False
        if not len(stack):
            return True
        else:
            return False


def main():
    s = Solution()
    while True:
        print "Aloha!"
        print s.isValid("(()()()")
        print s.isValid("()()[]")
        print s.isValid("{}()()()")
        print s.isValid("(())()()")
        print s.isValid("(({[]})()")
        print s.isValid("(")
        print s.isValid("[")
        print s.isValid("}")

        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
            else:
                pass
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()