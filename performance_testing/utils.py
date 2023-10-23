from datetime import datetime, timezone


def str_to_datetime(datetime_str: str) -> datetime:
    return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


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
    func(*args, **kwargs)
    return datetime.now() - start
