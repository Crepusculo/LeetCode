"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Subscribe to see which companies asked this question
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        result = None
        if l1.val < l2.val:
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
        else:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)

        return result
