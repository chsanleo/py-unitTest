import unittest


class NumberTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


"""
Without using a subtest, execution would stop after the
first failure, and the error would be less easy to diagnose
because the value of i wouldn't be displayed
"""
if __name__ == '__main__':
    unittest.main()
