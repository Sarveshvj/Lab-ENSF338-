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
            # Pop until '('
            e2 = stack.pop()
            e1 = stack.pop()
            operator = stack.pop()
            stack.pop()  # remove '('

            if operator == '+':
                result = e1 + e2
            elif operator == '-':
                result = e1 - e2
            elif operator == '*':
                result = e1 * e2
            elif operator == '/':
                result = e1 // e2
            else:
                raise ValueError("Unknown operator")

            stack.push(result)

        elif token == '(':
            stack.push(token)

        else:
            # number or operator
            try:
                stack.push(int(token))
            except ValueError:
                stack.push(token)

    return stack.pop()


if __name__ == '__main__':
    expression = sys.argv[1]
    print(evaluate(expression))
