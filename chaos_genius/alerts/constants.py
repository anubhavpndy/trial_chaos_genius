"""Constants used in alerts."""

import datetime

ALERT_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

ALERT_DATE_FORMAT = "%b %d %Y"

ALERT_READABLE_DATE_FORMAT = "%b %d"

ALERT_READABLE_DATETIME_FORMAT = "%b %d, %I %p"

ALERT_READABLE_DATA_TIMESTAMP_FORMAT = "%b %d %Y %H:%M:%S"

ALERT_READABLE_DATA_TIME_ONLY_FORMAT = "%I %p"
"""Format for time (without date) of anomaly."""

ANOMALY_TABLE_COLUMN_NAMES_MAPPER = {
    "series_type": "Dimension",
    "data_datetime": "Time of Occurrence",
    "y": "Value",
    "severity": "Severity Score",
    "change_message": "Change",
    "expected_value": "Expected Value",
    "previous_value": "Previous Value",
}
ANOMALY_TABLE_COLUMN_NAMES_ORDERED = [
    "series_type",
    "data_datetime",
    "y",
    "previous_value",
    "change_message",
    "severity",
    "expected_value",
]

FREQUENCY_DICT = {
    "weekly": datetime.timedelta(days=7, hours=0, minutes=0),
    "daily": datetime.timedelta(days=1, hours=0, minutes=0),
    "hourly": datetime.timedelta(days=0, hours=1, minutes=0),
    "every_15_minute": datetime.timedelta(days=0, hours=0, minutes=15),
    "every_minute": datetime.timedelta(days=0, hours=0, minutes=1),
}

OVERALL_KPI_SERIES_TYPE_REPR = "Overall KPI"

ALERT_RELEVANT_SUBDIMS_TOP_N = 3
"""Number of subdims to consider as relevant for an overall anomaly."""
ALERT_OVERALL_TOP_N = 5
"""Number of overall anomalies to show in an individual alert."""
ALERT_SUBDIM_TOP_N = 3
"""Number of subdim anomalies to show in an individual alert."""
ALERT_REPORT_OVERALL_TOP_N = 10
"""Number of top overall anomalies to show in an alert report."""
ALERT_REPORT_SUBDIM_TOP_N = 10
"""Number of top subdim anomalies to show in an alert report."""
