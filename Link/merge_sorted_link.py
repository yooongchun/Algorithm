#! /usr/bin/python3
from Link.common import Node, cases_link_sorted, cases_link_sorted2, str_link

"""
Description：合并两个有序链表
Source: Leetcode 21
Solution：
    1. 设链表为root1和root2，引入一个头结点prev，同时遍历两个链表，
        每次对比值r1和r2，若r1较小，将r1接到prev之后，然后移动r1-->r1.next，否则将r2接到prev之后
    2. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def merge_sorted_link(root1, root2):
    prev = Node(-1)
    head = prev
    while root1 and root2:
        if root1.val <= root2.val:
            prev.next, prev, root1 = root1, root1, root1.next
        else:
            prev.next, prev, root2 = root2, root2, root2.next
    prev.next = root1 if root1 else root2
    return head.next


def test():
    print('%-20s\t%-20s\t%-40s' % ('Case1', 'Case2', 'Merged'))
    for case1, case2 in zip(cases_link_sorted, cases_link_sorted2):
        sc1, sc2 = str_link(case1), str_link(case2)
        root = merge_sorted_link(case1, case2)
        print('%-20s\t%-20s\t%-40s' % (sc1, sc2, str_link(root)))


if __name__ == '__main__':
    test()
