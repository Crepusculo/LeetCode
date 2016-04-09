"""
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
where # represents a null node.

Given a string of comma separated values,
verify whether it is a correct preorder traversal serialization of a binary tree.

Find an algorithm without reconstructing the tree.
Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid,
for example it could never contain two consecutive commas such as "1,,3".
"""

test = True


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = list()

        for each in preorder.split(","):
            stack.append(each)
            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != ['#']:
                stack = stack[:-3] + ['#']
        return len(stack) == 1 and stack[0] == '#'


def main():
    if test:
        s = Solution()
        s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
        s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,2")
        s.isValidSerialization("1,,")

if __name__ == '__main__':
    main()
