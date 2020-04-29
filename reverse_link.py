#! /usr/bin/python3

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


def reverse_link(root):
    prev, curr = None, root
    while curr is not None:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


def test():
    cases = ['as', 'a', '', 'aa', 'asd', 'asdfghjkllkjhgfdsa', 'aaaaaa', 'asasasas', '{[()]}', '{{',
             [], [1, 2], None, [1, 2, 1]]
    print('%-20s\t%-10s' % ('Case', 'Palindrome'))
    for case in cases:
        root = create_link_str(case)
        res = reverse_link(root)
        rs = []
        while res is not None:
            rs.append(res.val)
            res = res.next

        print('%-20s\t%-20s' % (case, rs))


if __name__ == '__main__':
    test()
