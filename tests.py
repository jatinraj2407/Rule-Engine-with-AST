import unittest
from rule_engine import RuleEngine

class TestRuleEngine(unittest.TestCase):

    def setUp(self):
        self.engine = RuleEngine()

    def test_create_rule(self):
        rule_str = "(age > 30 and department == 'Sales')"
        ast = self.engine.create_rule("rule1", rule_str)
        self.assertIsNotNone(ast)

    def test_evaluate_rule(self):
        rule_str = "(age > 30 and department == 'Sales')"
        self.engine.create_rule("rule1", rule_str)
        data = {"age": 35, "department": "Sales"}
        result = self.engine.evaluate_rule(self.engine.rules["rule1"], data)
        self.assertTrue(result)

    def test_combine_rules(self):
        rule1 = "(age > 30 and department == 'Sales')"
        rule2 = "(salary > 50000)"
        self.engine.create_rule("rule1", rule1)
        self.engine.create_rule("rule2", rule2)
        combined_ast = self.engine.combine_rules(["rule1", "rule2"])
        self.assertIsNotNone(combined_ast)
        result = self.engine.evaluate_rule(combined_ast, {"age": 35, "department": "Sales", "salary": 60000})
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
