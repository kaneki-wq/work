from datetime import datetime, timedelta
def print_dates():
    today = datetime.now()

    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    print("Yesterday:", yesterday.date())
    print("Today:", today.date())
    print("Tomorrow:", tomorrow.date())