from datetime import datetime, timedelta
def date_difference_seconds(date1, date2):
    diff = date2 - date1
    return diff.total_seconds()