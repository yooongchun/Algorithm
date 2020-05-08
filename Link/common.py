#! /usr/bin/python3

"""
Description：链表公用函数
"""

__author__ = 'yooongchun'


class Node:
    """链表结点"""
    def __init__(self, x: int):
        self.val = x
        self.next = None


def create_link(s: list, with_head: bool = False, loop_pos: int = -1, sort: bool = False):
    """创建链表
    Args:
        :param s:字符串或列表
        :param with_head: 是否带有头结点
        :param loop_pos: 环的位置，若为-1则无环
        :param sort: 排序
        :return: 第一个结点

    """
    if s is None or len(s) < 1:
        return Node(-1) if with_head else None
    if sort:
        s = sorted(s)
    if with_head:
        head = Node(-1)
    else:
        head = Node(s[0])
    p = head
    s = s if with_head else s[1:]
    for c in s:
        node = Node(c)
        p.next, p = node, node
    if loop_pos >= 0:
        n = 0
        q = head
        while n < loop_pos:
            q = q.next
            n += 1
        p.next = q
    return head


def str_link(root):
    """将链表序列化为字符串"""
    str_ = ''
    node_list = []
    while root and root not in node_list:
        str_ += str(root.val) + ' '
        node_list.append(root)
        root = root.next
    return str_


cases_list = [[21, 34], [12, 56], [1], [1, 2], [1, 2, 1], [1, 1], [1, 1, 2, 2], [1, 2, 3, 4, 5, 6, 7, 8],
              'sd', 'as', 'as', 'we', 'asdsa', 'aaa', 'aa', 'asdfghjkl', 'asdfghjklkjhgfdsa', 'qawseddeswaq']

cases_link = [create_link(case) for case in cases_list]
cases_link_with_head = [create_link(case, with_head=True) for case in cases_list]
cases_link_loop = [create_link(case, loop_pos=0) for case in cases_list]
cases_link_sorted = [create_link(case, sort=True) for case in cases_list]
cases_link_sorted2 = [create_link(case, sort=True) for case in cases_list]

if __name__ == '__main__':
    print([str_link(case) for case in cases_link])
    print([str_link(case) for case in cases_link_with_head])
    print([str_link(case) for case in cases_link_loop])
    print([str_link(case) for case in cases_link_sorted])


