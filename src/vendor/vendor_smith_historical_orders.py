from src.vendor.vendor import Vendor

from dataclasses import dataclass
from datetime import datetime


@dataclass
class VendorSmithHistoricalOrders(Vendor):
    """Specialization for Smith Historical Orders"""

    vendor_root: str
    vendor_date: datetime

    def __init__(self, vendor_root, vendor_date):
        # TODO: configuration code to set vendor_name and vendor_filename
        super().__init__(
            vendor_root=vendor_root,
            vendor_name="smith_historical_orders",
            vendor_date=vendor_date,
            vendor_filename="3. FY24 Order Analysis.xlsx",
        )
