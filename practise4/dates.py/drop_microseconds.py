from datetime import datetime, timedelta
def drop_microseconds():
    now = datetime.now()
    return now.replace(microsecond=0)