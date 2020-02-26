import time


def log(*args, **kwargs):
    formats = "%Y/%m/%d %H:%M:%S"
    value = time.localtime(int(time.time()))
    dt = time.strftime(formats, value)
    print(dt, *args, **kwargs)
