#! /usr/bin/python3
from Link.common import str_link, cases_link

"""
Description：反转链表
Source: Leetcode 206
Solution：
    1. 遍历链表，每次将指针反转
    2. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def reverse_link(root):
    prev, curr = None, root
    while curr is not None:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


def test():
    print('%-20s\t%-10s' % ('Case', 'Reversed'))
    for case in cases_link:
        case_str = str_link(case)
        res = reverse_link(case)
        print('%-20s\t%-20s' % (case_str, str_link(res)))


if __name__ == '__main__':
    test()
