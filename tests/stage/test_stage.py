import pandas as pd
from datetime import datetime

from src.stage.stage import Stage


def test_stage():
    """Test that we get a stage object for
    vendor and date
    """
    test_date = datetime(2024, 2, 26)

    stage = Stage(vendor="test", date=test_date)
    assert stage.vendor == "test"
    result = stage.run()
    assert isinstance(result, pd.DataFrame)
