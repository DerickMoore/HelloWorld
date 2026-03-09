import unittest
from io import StringIO
import sys
from helloworld import is_prime, dm_hello


class TestIsPrime(unittest.TestCase):
    """Test cases for the is_prime function"""

    def test_negative_numbers(self):
        """Negative numbers should not be prime"""
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-1))

    def test_zero_and_one(self):
        """Zero and one are not prime"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_small_primes(self):
        """Test small prime numbers"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_small_non_primes(self):
        """Test small non-prime numbers"""
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

    def test_larger_primes(self):
        """Test larger prime numbers"""
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(97))

    def test_larger_non_primes(self):
        """Test larger non-prime numbers"""
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(121))  # 11 * 11
        self.assertFalse(is_prime(144))  # 12 * 12

    def test_edge_case_two(self):
        """Two is the only even prime"""
        self.assertTrue(is_prime(2))
        
    def test_even_numbers(self):
        """Even numbers > 2 are not prime"""
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(50))
        self.assertFalse(is_prime(100))


class TestDmHello(unittest.TestCase):
    """Test cases for the dm_hello function"""

    def test_dm_hello_output(self):
        """Test that dm_hello prints the correct string"""
        captured_output = StringIO()
        sys.stdout = captured_output
        dm_hello("Hello, world!")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, world!\n")

    def test_dm_hello_with_different_strings(self):
        """Test dm_hello with different input strings"""
        captured_output = StringIO()
        sys.stdout = captured_output
        dm_hello("Test message")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Test message\n")

    def test_dm_hello_with_empty_string(self):
        """Test dm_hello with empty string"""
        captured_output = StringIO()
        sys.stdout = captured_output
        dm_hello("")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n")

    def test_dm_hello_with_special_characters(self):
        """Test dm_hello with special characters"""
        captured_output = StringIO()
        sys.stdout = captured_output
        dm_hello("Hello, world! 123 @#$")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, world! 123 @#$\n")


if __name__ == '__main__':
    unittest.main()
