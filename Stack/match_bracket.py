#! /usr/bin/python3
# *- coding: utf-8 -*

from Stack.common import Stack
"""
Description：判断括号是否匹配
Source: Leetcode 20
Solution：
    1. 使用一个栈来存储，元素依次入栈，一旦匹配则一对括号出栈，反之一直入栈。
    2. 当元素遍历完毕，如果栈为空，则括号匹配。反之不匹配
    3. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def compare(b1, b2):
    if b1 in [')', ']', '}']:
        return False
    if (b1 == '(' and b2 == ')') or (b1 == '[' and b2 == ']') or (b1 == '{' and b2 == '}'):
        return True


def is_bracket_matched(brackets):
    stack = Stack()
    for bra in brackets:
        if compare(stack.top(), bra):
            stack.pop()
        else:
            stack.push(bra)
    return stack.is_empty()


def test():
    cases = ['', '{', '{}', '([{}', '}', '}]', '{[()]}', '(){}[]', '{[]}()()']
    print('%-10s\t%-5s' % ('Case', 'Matched'))
    for case in cases:
        res = is_bracket_matched(case)
        print('%-10s\t%-5s' % (case, res))


if __name__ == '__main__':
    test()
