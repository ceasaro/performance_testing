from datetime import datetime, timezone

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def str_to_datetime(datetime_str: str) -> datetime:
    _datetime = datetime.strptime(datetime_str, DATE_TIME_FORMAT)
    return _datetime.replace(tzinfo=timezone.utc)


def datetime_to_str(_datetime: datetime) -> str:
    return _datetime.strftime(DATE_TIME_FORMAT)


def timestamp_to_datetime(timestamp: float) -> datetime:
    """convert epoch timestamp in seconds to datetime object with UTC timezone

    Args:
        timestamp (float): epoch timestamp in seconds

    Returns:
        datetime: datetime object represent the input epoch. object timezone is set to UTC
    """
    _datetime = datetime.utcfromtimestamp(timestamp)
    return _datetime.replace(tzinfo=timezone.utc)


def elapsed_time(func, *args, **kwargs):
    start = datetime.now()
    resp = func(*args, **kwargs)
    return datetime.now() - start, resp
