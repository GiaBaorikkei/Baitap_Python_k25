import unittest

from main import calc_actual_withdrawal


class TestFantasyLeague(unittest.TestCase):
    """
    Unit Test cho hàm calc_actual_withdrawal().
    """

    def test_withdraw_100_tokens(self):
        """
        Test Case 1:
        Rút 100 token -> nhận 90 token.
        """

        expected = 90.0

        self.assertEqual(
            calc_actual_withdrawal(100),
            expected
        )

    def test_negative_withdraw(self):
        """
        Test Case 2:
        Rút số âm phải phát sinh ValueError.
        """

        with self.assertRaises(ValueError):
            calc_actual_withdrawal(-100)


if __name__ == "__main__":
    unittest.main()