#! /usr/bin/python3

"""
Description：删除链表的倒数第n个节点
Source: Leetcode 19
Solution：
    1. 遍历链表，使用双指针，指针间隔为n+1个节点，这样，当第一个指针到达尾部时另一指针即在倒数n前一个位置
    2. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_link_str(s):
    if s is None or len(s) < 1:
        return None
    root = Node(s[0])
    p = root
    for c in s[1:]:
        node = Node(c)
        p.next = node
        p = p.next
    return root


def delete_reverse_nth_ele_in_link(root, n_th):
    head = Node(-1)
    head.next = root
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
    return head.next


def str_link(root):
    str_ = ''
    while root:
        str_ += str(root.val) + ' '
        root = root.next
    return str_


def test():
    cases = ['as', 'a', '', 'aa', 'asd', 'asdfghjkllkjhgfdsa', 'aaaaaa', 'asasasas', '{[()]}', '{{',
             [1], [1, 2], None, [1, 2, 1], [1, 2, 4, 8, 21, 43, 2]]

    print('%-20s\t%-20s' % ('Case', 'Deleted'))
    for case in cases:
        root = create_link_str(case)
        head = delete_reverse_nth_ele_in_link(root, 1)
        print('%-20s\t%-20s' % (case, str_link(head)))


if __name__ == '__main__':
    test()
