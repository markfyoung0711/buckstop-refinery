import pandas as pd

from dataclasses import dataclass


@dataclass
class Stage:
    vendor: str
    date: float

    pass

    def run(self):
        return pd.DataFrame()
