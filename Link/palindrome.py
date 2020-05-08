#! /usr/bin/python3
from Link.common import cases_link, str_link
"""
Description：判断链表是否为回文链表
Source: Leetcode 234
Solution：
    1. 使用双指针slow和fast遍历链表，其中slow一次移动一位，fast一次移动两位，遍历完找到链表中点slow
    2. 反转链表的后半部分
    3. 从中间向两边遍历链表，对比值是否相同，若不同，则不是回文。
    4. 3遍历结束，则为回文
    5. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def is_palindrome(head):
    slow, fast, prev = head, head, None
    while fast is not None:
        slow = slow.next
        fast = fast.next.next if fast.next is not None else fast.next
    while slow is not None:
        slow.next, slow, prev = prev, slow.next, slow
    while head and prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True


def test():
    print('%-20s\t%-10s' % ('Case', 'Palindrome'))
    for case in cases_link:
        s = str_link(case)
        res = is_palindrome(case)
        print('%-20s\t%-10s' % (s, res))


if __name__ == '__main__':
    test()
