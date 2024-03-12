from datetime import datetime
from tempfile import TemporaryDirectory

from src.vendor.vendor import Vendor

RAW_CONTENTS = """Contents
"""


def test_vendor():
    """Test that we can create a Vendor and use it"""
    test_vendor_name = "test"
    test_date = datetime(2024, 2, 26)
    test_filename = f"buster_brown_{test_date:%Y%m%d}.csv"

    # TODO: fixture
    with TemporaryDirectory() as test_vendor_root:
        test_dir = f"{test_vendor_root}/{test_vendor_name}/{test_date:%Y/%m/%d}"
        print("Created temporary directory ", test_dir)
        vendor = Vendor(
            vendor_root=test_vendor_root,
            vendor_name=test_vendor_name,
            vendor_date=test_date,
            vendor_filename=test_filename,
        )
        assert vendor.vendor_name == test_vendor_name
        assert vendor.path == f"{test_dir}/{test_filename}"
