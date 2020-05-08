#! /usr/bin/python3
from Link.common import str_link, cases_link_loop

"""
Description：判断链表是否有环
Source: Leetcode 141
Solution：
    1. 使用双指针slow和fast遍历链表，其中slow一次移动一位，fast一次移动两位
    2. 当fast==slow则说明有环，否则fast到达None，无环
    3. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def exist_loop(head):
    if head is None or head.next is None:
        return False
    slow, fast = head, head.next
    while fast is not None and fast.next is not None and fast != slow:
        slow = slow.next
        fast = fast.next.next
    return True if fast == slow else False


def test():
    print('%-20s\t%-5s\t%-10s' % ('Case', 'Loop pos', 'Exist loop'))
    for case in cases_link_loop:
        res = exist_loop(case)
        print('%20s\t%5d\t%10s' % (str_link(case), 0, res))


if __name__ == '__main__':
    test()
