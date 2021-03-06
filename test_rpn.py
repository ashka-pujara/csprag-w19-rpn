import unittest
import rpn


class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate('4 2 -')
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate('3 4 *')
        self.assertEqual(12, result)
    def test_divide(self):
        result = rpn.calculate('9 3 /')
        self.assertEqual(3, result)
    def test_power(self):
        result = rpn.calculate('3 2 ^')
        self.assertEqual(9, result)

#TestBasics tb;
#tb.test_add() ==> TestBasics.test_add(tb)
