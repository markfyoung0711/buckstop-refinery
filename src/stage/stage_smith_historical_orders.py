import pandas as pd

from datetime import datetime
from dataclasses import dataclass

from constants import VENDOR_ROOT
from src.stage.stage import Stage
from src.vendor.vendor_smith_historical_orders import VendorSmithHistoricalOrders


@dataclass
class StageSmithHistoricalOrders(Stage):
    start_date: datetime
    end_date: datetime
    vendor: VendorSmithHistoricalOrders

    def load_dates(self):
        data = []
        for date in pd.daterange(self.start_date, self.end_date):
            df = self.stage(date)
            data.append(df)
        # do something with the history to validate it
        # collapse the data into time series
        # collapse keys: Order No, Order Date

    def stage(self, date):
        """has parssing logic for a single date"""
        vendor = self.vendor(vendor_root=VENDOR_ROOT, vendor_date=date)
        return pd.read_excel(vendor.vendor_filename, sheet_name="Historical Orders")
