#! /usr/bin/python3
# *- coding: utf-8 -*

from collections import namedtuple

"""
Description：实现四则运算优先级
Source: Leetcode 20
Solution：
    1. 使用两个栈来存储，数字依次入栈1，符号依次入栈2
    2. 每次符号入栈判断符合优先级是否更大，更大则取出数进行计算
    2. 遍历直到计算完毕
    3. 时间复杂度：O(n)，空间复杂度：O(1)
"""

__author__ = 'yooongchun'


def comp_priority(s1, s2):
    Pri = namedtuple('Priority', ['ADD', 'SUB', 'DIV', 'MUL'])
    pri = Pri(0, 0, 1, 1)
    sym_map = {'+': pri.ADD, '-': pri.SUB, '*': pri.MUL, '/': pri.DIV}
    return sym_map[s1] >= sym_map[s2]


def cal_arithmetic(s: str) -> str:
    sym, nums = [], []
    for v in s:
        if v in (str(v) for v in range(10)):
            nums.append(v)
        else:
            while len(sym) > 0 and comp_priority(sym[-1], v):
                res = eval(nums[-1] + sym[-1] + nums[-2])
                del sym[-1], nums[-1]
                nums[-1] = str(res)
            sym.append(v)
    return nums[-1]


def test():
    cases = ['2*8-5+6/2*3+9', '1+2', '2-2', '1', '3*5/7', '3+1-9+12', '3+8*7/4*9+12-7']
    print('{:>15s}\t{:>5s}'.format('Case', 'Res'))
    for case in cases:
        res = cal_arithmetic(case)
        print('{:>15s}\t{:>5,.4f}'.format(case, float(res)))


if __name__ == '__main__':
    test()
