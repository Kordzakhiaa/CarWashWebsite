from datetime import datetime, timedelta


def date(days):
    return datetime.now() - timedelta(days=days)
