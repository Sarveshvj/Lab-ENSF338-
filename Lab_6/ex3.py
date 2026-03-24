import sys

class Node:
    def __init__(self, value):
        self.value = value    
        self.left = None
        self.right = None

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
        
    
if __name__ == "__main__":
    expression = sys.argv[1]
    expression = expression.replace("(", " ( ").replace(")", " ) ")

    tokens = expression.split()

    if len(tokens) == 1:
        print(int(tokens[0]))
        sys.exit(0)

    if tokens[0] != "(":
        tokens = ["("] + tokens + [")"]
        
    root, _ = parse(tokens, 0)
    result = evaluate(root)

    if isinstance(result, float) and result.is_integer():
        print(int(result))
    else:
        print(result)
