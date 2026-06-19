import unittest

from wallet import (
    Wallet,
    InvalidAmountError,
    InsufficientBalanceError
)


class TestWallet(unittest.TestCase):
    """Unit tests for Wallet."""

    def setUp(self):
        self.wallet = Wallet()

    def test_deposit_success(self):
        """Deposit should increase balance."""

        self.wallet.deposit(500000)

        self.assertEqual(
            self.wallet.balance,
            500000
        )

    def test_transfer_insufficient_balance(self):
        """Transfer should raise error."""

        with self.assertRaises(
            InsufficientBalanceError
        ):
            self.wallet.transfer(
                "0987654321",
                100000
            )

    def test_invalid_amount(self):
        """Negative amount."""

        with self.assertRaises(
            InvalidAmountError
        ):
            self.wallet.deposit(-1000)


if __name__ == "__main__":
    unittest.main()