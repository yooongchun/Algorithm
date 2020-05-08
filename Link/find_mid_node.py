#! /usr/bin/python3
from Link.common import str_link, cases_link_with_head

"""
Description：查找链表的中间节点
Source: Leetcode 876
Solution：
    1. 遍历链表，使用双指针，一快指针一次移动两个位置，慢指针一次移动一个位置。
        这样，当第快指针到达尾部时慢即在中间位置
    2. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def find_mid_node(root):
    slow, fast = root, root
    while fast:
        slow = slow.next
        fast = fast.next.next if fast.next else fast.next
    return slow


def test():
    print('%-20s\t%-20s' % ('Case', 'Mid after'))
    for case in cases_link_with_head:
        mid = find_mid_node(case)
        print('%-20s\t%-20s' % (str_link(case), str_link(mid)))


if __name__ == '__main__':
    test()
