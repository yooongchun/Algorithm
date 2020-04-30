#! /usr/bin/python3

"""
Description：合并两个有序链表
Source: Leetcode 21
Solution：
    1. 设链表为root1和root2，同时遍历两个链表，每次对比值r1和r2，若r1较小，移动r1-->r1.next，
       否则将r2插入r1之前，直到r1到达None。然后将r2剩余部分接到r1之后。
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
    s = sorted(s)
    root = Node(s[0])
    p = root
    for c in s[1:]:
        node = Node(c)
        p.next = node
        p = p.next
    return root


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
    cases1 = ['as', 'a', '', 'aa', 'asd', 'asdfghjkllkjhgfdsa', 'aaaaaa', 'asasasas', '{[()]}', '{{',
             [], [1, 2], None, [1, 2, 1]]
    cases2 = ['asadfds', '', [], 'aasdeda', 'asd', 'asdfghjkllkjhgfdsa', 'aaaaaa', 'asasasas', '{[()]}', '{{',
              [], [1, 2, 6], None, [2, 4, 8, 9]]

    print('%-20s\t%-20s\t%-40s' % ('Case1', 'Case2', 'Merged'))
    for case1, case2 in zip(cases1, cases2):
        root1 = create_link_str(case1)
        root2 = create_link_str(case2)
        root = merge_sorted_link(root1, root2)
        merged_str = []
        while root:
            merged_str.append(root.val)
            root = root.next
        print('%-20s\t%-20s\t%-40s' % (case1, case2, merged_str))


if __name__ == '__main__':
    test()
