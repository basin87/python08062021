import time
import datetime


def countdown(func):
    def wrapper(*args, **kwargs):
        count = 3
        while count > 0:
            time.sleep(1)
            print(count)
            count -= 1
        result = func(*args, **kwargs)
    return wrapper


@countdown
def what_time_is_it():
    tasktime = datetime.datetime.now()
    current_time = tasktime.strftime("%I:%M:%S %p")
    print(current_time)
    return current_time


what_time_is_it()