class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left       # Reference to the left child Node
        self.right = right     # Reference to the right child Node
        self.value = value     # Holds value for operand nodes (e.g., age, salary, etc.)

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"


def parse_rule(rule_str):
    """Parses a rule string into an Abstract Syntax Tree (AST)"""
    import ast
    parsed_expr = ast.parse(rule_str, mode='eval')
    return build_ast(parsed_expr.body)


def build_ast(node):
    """Recursively build AST from parsed expressions."""
    if isinstance(node, ast.BinOp):
        left = build_ast(node.left)
        right = build_ast(node.right)
        operator = node.op.__class__.__name__
        return Node('operator', left, right, operator)
    elif isinstance(node, ast.Compare):
        left = build_ast(node.left)
        right = build_ast(node.comparators[0])
        operator = node.ops[0].__class__.__name__
        return Node('operand', left, right, operator)
    elif isinstance(node, ast.Name):
        return Node('operand', value=node.id)
    elif isinstance(node, ast.Constant):
        return Node('operand', value=node.value)
