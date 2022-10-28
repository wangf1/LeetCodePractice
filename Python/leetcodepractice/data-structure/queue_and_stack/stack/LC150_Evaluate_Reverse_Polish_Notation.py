# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}

        token_to_operation = {
            '+': lambda x, y: x + y,  #
            '-': lambda x, y: x - y,  #
            '*': lambda x, y: x * y,  #
            '/': lambda x, y: int(x / y)  #
        }

        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                val = token_to_operation[t](left, right)
                stack.append(val)
        return stack.pop()

    # Do not use set and map, performance is better
    def evalRPN_performance_is_better(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif t == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif t == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif t == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(t))
        return stack.pop()
