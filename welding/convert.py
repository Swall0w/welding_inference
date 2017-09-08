from datetime import datetime


def parse_time(timestamp):
    a = datetime.strptime(timestamp, '%H:%M:%S.%f')
    return a


def _datetime_to_second(time):
    second = (time.hour * 3600 + time.minute * 60. + time.second +
              float(str(time.microsecond)[:2]) * .01)
    return second


def convert_time_to_index(time, fps):
    index = _datetime_to_second(time) * fps
    return int(index)
