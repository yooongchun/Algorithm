#! /usr/bin/python3
from Link.common import str_link, cases_link_with_head

"""
Description：删除链表的倒数第n个节点
Source: Leetcode 19
Solution：
    1. 遍历链表，使用双指针，指针间隔为n+1个节点，这样，当第一个指针到达尾部时另一指针即在倒数n前一个位置
    2. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def delete_reverse_nth_ele_in_link(head, n_th):
    prev, curr = None, head
    n = 1
    while curr and curr.next:
        curr = curr.next
        if n == n_th:
            prev = head
        elif n > n_th:
            prev = prev.next
        n += 1
    if prev and prev.next:
        prev.next = prev.next.next
    return head


def test():
    print('%-20s\t%-20s' % ('Case', 'Deleted'))
    for case in cases_link_with_head:
        o_case_str = str_link(case.next)
        head = delete_reverse_nth_ele_in_link(case, 1)
        print('%-20s\t%-20s' % (o_case_str, str_link(head.next)))


if __name__ == '__main__':
    test()
