import unittest
from main import calculate_total_revenue


class TestTicketing(unittest.TestCase):
    """Unit Test cho hàm calculate_total_revenue()."""

    def test_calculate_total_revenue_with_booked_and_cancelled(self):
        """Test Case 1: Chỉ tính doanh thu của các vé Booked."""

        ticket_list = [
            {
                "ticket_id": "T01",
                "buyer_name": "Nguyen Van A",
                "price": 500.0,
                "status": "Booked",
                "seat": ("A", 1)
            },
            {
                "ticket_id": "T02",
                "buyer_name": "Tran Thi B",
                "price": 300.0,
                "status": "Cancelled",
                "seat": ("B", 5)
            },
            {
                "ticket_id": "T03",
                "buyer_name": "Le Van C",
                "price": 500.0,
                "status": "Booked",
                "seat": ("A", 2)
            }
        ]

        expected = 1000.0
        actual = calculate_total_revenue(ticket_list)

        self.assertEqual(actual, expected)

    def test_calculate_total_revenue_empty_list(self):
        """Test Case 2: Danh sách rỗng trả về 0.0."""

        ticket_list = []

        expected = 0.0
        actual = calculate_total_revenue(ticket_list)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()