import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """تشغيل قبل كل اختبار - بتهيأ كائن من الكلاس."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """اختبار دالة الجمع"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_subtraction(self):
        """اختبار دالة الطرح"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiplication(self):
        """اختبار دالة الضرب"""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_division(self):
        """اختبار دالة القسمة"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertIsNone(self.calc.divide(5, 0))  # اختبار القسمة على صفر
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
