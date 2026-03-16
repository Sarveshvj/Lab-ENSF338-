import sys

class Node:
    def __init__(self, value):
        self.value = value    
        self.left = None
        self.right = None

OPERATORS = {'+', '-', '*', '/'}

def parse(tokens, index):
    token = tokens[index]

    if token == '(':
        index += 1

        left_node, index = parse(tokens, index)

        op = tokens[index]
        index += 1

        right_node, index = parse(tokens, index)

        index += 1

        node = Node(op)
        node.left = left_node
        node.right = right_node
        return node, index

    else:
        return Node(int(token)), index + 1

def evaluate(node):
    if node.left is None and node.right is None:
        return node.value

    left_val  = evaluate(node.left)
    right_val = evaluate(node.right)

    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val
