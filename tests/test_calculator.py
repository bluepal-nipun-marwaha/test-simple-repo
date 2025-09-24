#!/usr/bin/env python3
"""
Tests for the Calculator class.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
        
        result = self.calc.subtract(1, 1)
        self.assertEqual(result, 0)
    
    def test_multiply(self):
        """Test multiplication operation."""
        result = self.calc.multiply(2, 3)
        self.assertEqual(result, 6)
        
        result = self.calc.multiply(-2, 3)
        self.assertEqual(result, -6)
    
    def test_divide(self):
        """Test division operation."""
        result = self.calc.divide(6, 2)
        self.assertEqual(result, 3)
        
        result = self.calc.divide(5, 2)
        self.assertEqual(result, 2.5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_history(self):
        """Test calculation history."""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("1 + 2 = 3", history)
        self.assertIn("5 - 3 = 2", history)
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(1, 2)
        self.calc.clear_history()
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 0)


if __name__ == '__main__':
    unittest.main()
