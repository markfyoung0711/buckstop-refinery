import pandas as pd
from src.bonum_logging import log
from dataclasses import dataclass
from datetime import datetime
from src.vendor.vendor import Vendor
import sqlalchemy as sa


@dataclass
class Override:
    """Behavior:
        1. Load the overrides into cache for a particular date range
        2. Use the payload to match field and value to "old_value" from overrides
        3. Match the dates of the override.
        4. Apply new_value to matches
        5. Return overridden data.

        db_connection: connection to the database storing the overrides
        vendor: the name of the vendor
        valid_from: the start date/time (inclusive) of the time series
        valid_to: the end date/time (exclusive) of the time series
        archival_date: the date/time that the record is archived, if not null, then
    it is archived

        key_field_name: the field name of the key
        key_field_value: the value of the key field

        value_field_name: name of the field that needs an override
        value_current_value: the current value of the value field
        value_new_value: the value to use to replace the current value

        description: the reason for the override

        cache: a cache of the overrides for the vendor

    """

    db_connection: sa.engine.base.Engine
    vendor: Vendor
    valid_from: datetime
    valid_to: datetime
    archive_date: datetime

    key_field_name: str
    key_field_value: str

    value_field_name: str
    value_current_value: str
    value_new_value: str

    description: str

    def load(self, point_in_time):
        """Load overrides from DB and cache in memory"""
        # TODO: load the override contents into a dataframe for the date
        # in question.
        # return only those items where archive_date is null or archive_date > point in time
        self.cache = pd.DataFrame()
        return

    def match(self, payload):
        """Returns dataframe of matches
        1. Generate the payload index where there are matches.
        2. Join cache with the payload
        3. Match on field first.
        4. Match on valid_from, valid_to, and value
        """
        df_matched = self.payload.merge(
            self.cache["valid_from", "valid_to", "archive_date", "field", "value"],
            how="left",
            left_on=["field"],
            right_on=["field"],
            suffixes=("_pl", ""),
        )

        # did not match on field

        idx_matched = (
            (df_matched["field"].notnull())
            & (df_matched["valid_from_pl"] >= df_matched["valid_from"])
            & (df_matched["valid_to_pl"] <= df_matched["valid_to"])
            & (df_matched["value_pl"] == df_matched["value"])
        )

        if (num_matched := idx_matched.sum()) > 0:
            log.info(f"Override matches {num_matched}")

        return idx_matched, df_matched

    def apply(self, point_in_time, payload):
        """
        If the point_in_time matches a valid_from-valid_to range for a vendor,
        then look at the payload to decode the fieldname and value for
        the date.

        If there is an override match
        and the vendor file matches a vendor in
        """
        if (idx_matched := self.match(payload)).sum() > 0:
            return payload.loc[idx_matched]

        return payload
