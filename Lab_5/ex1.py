import sys

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


def evaluate(expression):
    stack = Stack()

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:

        if token == ')':
            args = []

            while stack.peek() != '(':
                args.append(stack.pop())

            stack.pop()

            e2 = args[0]
            e1 = args[1]
            operator = args[2]

            if operator == '+':
                result = e1 + e2
            elif operator == '-':
                result = e1 - e2
            elif operator == '*':
                result = e1 * e2
            elif operator == '/':
                result = e1 // e2

            stack.push(result)

        elif token == '(':
            stack.push(token)

        else:
            try:
                stack.push(int(token))
            except ValueError:
                stack.push(token)

    return stack.pop()


if __name__ == '__main__':
    expression = sys.argv[1]
    print(evaluate(expression))