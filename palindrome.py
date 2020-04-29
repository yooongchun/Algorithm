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
    cases = ['', 'a', 'as', 'aa', 'asd', 'asdfghjkllkjhgfdsa', 'aaaaaa', 'asasasas', '{[()]}', '{{',
             [], [1, 2], None, [1, 2, 1]]
    print('%-20s\t%-10s' % ('Case', 'Palindrome'))
    for case in cases:
        root = create_link_str(case)
        res = is_palindrome(root)
        print('%-20s\t%-10s' % (case, res))


if __name__ == '__main__':
    test()
