import json
from ast import Node, parse_rule

class RuleEngine:
    def __init__(self):
        self.rules = {}

    def create_rule(self, rule_name, rule_str):
        """Create a rule and return its AST representation"""
        ast = parse_rule(rule_str)
        self.rules[rule_name] = ast
        return ast

    def combine_rules(self, rule_names):
        """Combines multiple rules into a single AST"""
        combined = None
        for rule_name in rule_names:
            if rule_name in self.rules:
                if combined is None:
                    combined = self.rules[rule_name]
                else:
                    combined = Node('operator', combined, self.rules[rule_name], 'And')
        return combined

    def evaluate_rule(self, ast_node, data):
        """Evaluate a rule's AST against the given user data"""
        if ast_node.type == 'operator':
            if ast_node.value == 'And':
                return self.evaluate_rule(ast_node.left, data) and self.evaluate_rule(ast_node.right, data)
            elif ast_node.value == 'Or':
                return self.evaluate_rule(ast_node.left, data) or self.evaluate_rule(ast_node.right, data)
        elif ast_node.type == 'operand':
            left = ast_node.left.value
            right = ast_node.right.value
            if ast_node.value == 'Gt':
                return data.get(left, 0) > right
            elif ast_node.value == 'Lt':
                return data.get(left, 0) < right
            elif ast_node.value == 'Eq':
                return data.get(left) == right

    def modify_rule(self, rule_name, new_rule_str):
        """Modify an existing rule by updating its AST"""
        if rule_name in self.rules:
            new_ast = parse_rule(new_rule_str)
            self.rules[rule_name] = new_ast
        return self.rules.get(rule_name)

# Sample API to interact with the rule engine
from flask import Flask, request, jsonify

app = Flask(__name__)
engine = RuleEngine()

@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.get_json()
    rule_name = data.get('rule_name')
    rule_str = data.get('rule')
    ast = engine.create_rule(rule_name, rule_str)
    return jsonify({"rule_name": rule_name, "ast": str(ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    data = request.get_json()
    rule_name = data.get('rule_name')
    user_data = data.get('data')
    ast = engine.rules.get(rule_name)
    if ast:
        result = engine.evaluate_rule(ast, user_data)
        return jsonify({"result": result})
    return jsonify({"error": "Rule not found"}), 404
