from datetime import datetime
from tempfile import TemporaryDirectory

from src.vendor.vendor_smith_historical_orders import VendorSmithHistoricalOrders

RAW = """
Order Number, Customer Number, Order Date, Sales Amount, Cost, Product Number
100001, 120, 2024-02-21, 10001.00, 120000.00, BUCLAB-101
"""

# fixture to write a temporary file


def test_vendor_smith_historical_orders():
    """Test shows that vendor SmithHistoricalOrders can be used to locate a file and return its location"""
    test_vendor_name = "smith_historical_orders"
    test_date = datetime(2024, 2, 27)
    with TemporaryDirectory() as test_vendor_root:

        vendor = VendorSmithHistoricalOrders(
            vendor_root=test_vendor_root, vendor_date=test_date
        )
        test_file1 = vendor.get_path()
        test_file = f"{test_vendor_root}/{test_vendor_name}/{test_date:%Y/%m/%d}/{vendor.vendor_filename}"
        assert test_file == test_file1
