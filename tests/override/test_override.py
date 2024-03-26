from datetime import datetime
from tempfile import TemporaryDirectory

import sqlalchemy as sa

from src.override.override import Override
from src.vendor.vendor import Vendor


def test_override():
    engine = sa.create_engine("sqlite+pysqlite:///:memory:", echo=True)
    test_date = datetime.now()
    tmpdir = TemporaryDirectory()
    test_valid_from = datetime(2024, 1, 1)
    test_valid_to = datetime(2262, 4, 11)
    test_vendor = Vendor(
        vendor_root=tmpdir,
        vendor_name="test",
        vendor_date=test_date,
        vendor_filename="test.csv",
    )
    obj = Override(
        db_connection=engine,
        vendor=test_vendor,
        valid_from=test_valid_from,
        valid_to=test_valid_to,
        archive_date=None,
        key_field_name="vin",
        key_field_value="ABC123Z0F33",
        value_field_name="color",
        value_current_value="red",
        value_new_value="black",
        description="wrong color for vin",
    )
    print(obj)
    assert isinstance(obj, Override)
