import unittest

from main import calculate_actual_pay


class TestCalculateActualPay(unittest.TestCase):
    """
    Unit Test cho hàm calculate_actual_pay().
    """

    def test_active_player_salary(self):
        """
        Test Case 1:
        Tuyển thủ Active nhận 100% lương.
        """

        player = {
            "player_id": "P01",
            "name": "Faker",
            "role": "Mid Lane",
            "salary": 5000.0,
            "status": "Active"
        }

        expected = 5000.0

        self.assertEqual(calculate_actual_pay(player), expected)

    def test_benched_player_salary(self):
        """
        Test Case 2:
        Tuyển thủ Benched nhận 50% lương.
        """

        player = {
            "player_id": "P02",
            "name": "Ruler",
            "role": "ADC",
            "salary": 6000.0,
            "status": "Benched"
        }

        expected = 3000.0

        self.assertEqual(calculate_actual_pay(player), expected)


if __name__ == "__main__":
    unittest.main()