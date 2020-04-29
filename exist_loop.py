#! /usr/bin/python3

"""
Description：判断链表是否有环
Solution：
    1. 使用双指针slow和fast遍历链表，其中slow一次移动一位，fast一次移动两位
    2. 当fast==slow则说明有环，否则fast到达None，无环
"""

__author__ = 'yooongchun'


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_link_str(s, pos):
    if s is None or len(s) < 1:
        return None
    root = Node(s[0])
    p = root
    for c in s[1:]:
        node = Node(c)
        p.next = node
        p = p.next
    loop = root
    n = 0
    while n < pos:
        loop = loop.next
        n += 1
    p.next = loop
    return root


def exist_loop(root):
    if root is None or root.next is None:
        return False
    slow, fast = root, root.next
    while fast is not None and fast.next is not None and fast != slow:
        slow = slow.next
        fast = fast.next.next
    return True if fast == slow else False


def test():
    cases = [[3, 2, 0, -4], 'a', 'as', 'aa', 'asd', 'asdfghjkllkjhgfdsa', 'aaaaaa', 'asasasas', '{[()]}', '{{',
             [], [1, 2], None, [1, 2, 1]]
    print('%-20s\t%-10s' % ('Case', 'Palindrome'))
    for case in cases:
        root = create_link_str(case, 1)
        res = exist_loop(root)
        print(res)
        break


if __name__ == '__main__':
    test()
