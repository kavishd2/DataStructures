import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

# Returns evaluation given operator and operands
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        return None

    def peek(self):
        if (not self.is_empty()):
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

# Represents expression so that it can be evaluated
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Keeps adding to the stack till finding a right parentheses to make the parent node
    def create_tree(self, expr):
        stack = Stack()
        tokens = expr.split()
        for token in tokens:
            if token == '(':
                continue
            elif token == ')':
                right = stack.pop()
                operator = stack.pop()
                left = stack.pop()
                operator.left = left
                operator.right = right
                stack.push(operator)
            else:
                stack.push(Node(token))
        self.root = stack.pop()

    # Result of evaluating the expression with this node as the root
    def evaluate(self, current): # Recursively calls method depending on whether current is an operator or not
        if current.data not in operators:
            return current.data
        return float(operation(current.data, self.evaluate(current.left), self.evaluate(current.right)))

    # The preorder notation of the expression with this node as the root
    def pre_order(self, current): # Adds operator before operands
        if current.data not in operators:
            return current.data
        return current.data + " " + self.pre_order(current.left) + " " + self.pre_order(current.right)

    # The post order notation of the expression with this node as the root
    def post_order(self, current): # Adds operator after operands
        if current.data not in operators:
            return current.data
        return self.post_order(current.left) + " " + self.post_order(current.right) + " " + current.data

# Execution
debug = False
if debug:
    in_data = open('expression.in')
else:
    in_data = sys.stdin

# read infix expression
line = in_data.readline()
expr = line.strip()

tree = Tree()
tree.create_tree(expr)

# evaluate the expression and print the result
print(expr, "=", str(tree.evaluate(tree.root)))

# get the prefix version of the expression and print
print("Prefix Expression:", tree.pre_order(tree.root).strip())

# get the postfix version of the expression and print
print("Postfix Expression:", tree.post_order(tree.root).strip())
