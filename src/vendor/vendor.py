import os

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Vendor:
    vendor_root: str
    vendor_name: str
    vendor_date: datetime
    vendor_filename: str

    # def __init__(name: str, date: datetime, filename: str):
    def __init__(self, vendor_root, vendor_name, vendor_date, vendor_filename):
        self.vendor_root = vendor_root
        self.vendor_name = vendor_name
        self.vendor_date = vendor_date
        self.vendor_filename = vendor_filename
        self.path = (
            f"{vendor_root}/{vendor_name}/{vendor_date:%Y/%m/%d}/{vendor_filename}"
        )
