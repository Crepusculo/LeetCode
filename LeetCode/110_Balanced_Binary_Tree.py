# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def def_child(self, l, r):
        self.left = l
        self.right = r


class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        elif self.is_balanced(root) < 0:
            return False
        else:
            return True

    def is_balanced(self, root):
        # con 1. if not root
        if not root:
            return 0
        l_dep = self.is_balanced(root.left)
        r_dep = self.is_balanced(root.right)
        # con 2. if unbalanced left or unbalanced right
        if abs(l_dep - r_dep) > 1 or l_dep == -1 or r_dep == -1:
            return -1

        return max(l_dep, r_dep)+1


def main():
    a = TreeNode("a")
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')
    g = TreeNode('g')
    a.def_child(b, c)
    b.def_child(d, e)
    d.def_child(f, g)
    sc = Solution()
    print 'a', sc.isBalanced(a)
    print 'b', sc.isBalanced(b)
    print 'c', sc.isBalanced(c)
    print 'd', sc.isBalanced(d)
    print 'e', sc.isBalanced(e)

if __name__ == '__main__':
    main()
