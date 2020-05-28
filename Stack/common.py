#! /usr/bin/python3
# *-coding:utf-8-*

"""
Description：栈通用函数
"""


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, x):
        self.stack.append(x)

    def pop(self, pos=0):
        n = len(self.stack) - 1 - pos
        if n < 0:
            return
        val = self.stack[n]
        del self.stack[n]
        return val

    def top(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == '__main__':
    stack = Stack()
    stack.push('==')
    print(stack.stack)
    val = stack.pop()
    print(val)
    print(stack.stack)
    print(stack.top())
