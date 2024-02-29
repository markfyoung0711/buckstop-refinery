from dataclasses import dataclass
from datetime import datetime

# TODO: implement as AirByte sources so as to support all connectors supported by Airbyte
"""
Airbyte Actor (Source) input: serialized json message to configure
                      output: serialized json message to log (AirbyteMessage)
    spec() -> ConnectorSpecification
    check(Config) -> AirbyteConnectionStatus
"""


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

    def get_path(self):
        return f"{self.vendor_root}/{self.vendor_name}/{self.vendor_date:%Y/%m/%d}/{self.vendor_filename}"
