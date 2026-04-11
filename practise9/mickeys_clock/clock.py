import datetime

def get_time_angles():
    now = datetime.datetime.now()
    # 360 градусов / 60 секунд = 6 градусов на ед. времени
    # В Pygame вращение идет против часовой, поэтому берем минус
    second_angle = -(now.second * 6)-18
    minute_angle = -(now.minute * 6)
    return minute_angle, second_angle