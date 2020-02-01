from time import perf_counter_ns as tick


def get_current_time():
    return tick()


def get_elapse_time(old_time):
    return get_current_time() - old_time


