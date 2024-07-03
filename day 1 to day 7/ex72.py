import unittest
from hello2 import isprime
class TestPrimeFunction(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(isprime(5))

if __name__ == '__main__':
    unittest.main()