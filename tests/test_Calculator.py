import unittest

from calculator.Calculator import Calculator


class TestUtils(unittest.TestCase):
    def test_parser(self):
        print()

        calculator = Calculator()

        self.assertIsNotNone(calculator.parser('1+1==2;'))
        self.assertIsNone(calculator.parser('1^1=2;'))
        self.assertIsNotNone(calculator.parser('1/1==2-1;'))
        self.assertIsNotNone(calculator.parser('1-1==0/2;'))
