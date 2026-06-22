import unittest

from energy_monitor import (
    calculate_energy_financials
)


class TestEnergy(unittest.TestCase):


    def test_normal_case(self):

        devices = [
            {
                "id": "M01",
                "old_index": 1000,
                "new_index": 5000
            }
        ]

        total, discount, cost = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            total,
            4000
        )

        self.assertEqual(
            discount,
            0
        )

        self.assertEqual(
            cost,
            12000000
        )


    def test_discount_case(self):

        devices = [
            {
                "id": "M01",
                "old_index": 0,
                "new_index": 60000
            }
        ]

        total, discount, cost = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            total,
            60000
        )

        self.assertEqual(
            discount,
            3
        )

        self.assertEqual(
            cost,
            174600000
        )


    def test_boundary_case(self):

        devices = [
            {
                "id": "M01",
                "old_index": 0,
                "new_index": 50000
            }
        ]

        total, discount, cost = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            total,
            50000
        )

        self.assertEqual(
            discount,
            3
        )

        self.assertEqual(
            cost,
            145500000
        )


if __name__ == "__main__":
    unittest.main()