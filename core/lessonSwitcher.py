from datetime import datetime, time

lessons_time = [
    [time(8, 30), time(10, 0)],
    [time(10, 20), time(11, 50)],
    [time(12, 10), time(13, 40)],
    [time(14, 30), time(16, 0)],
    [time(16, 10), time(17, 40)]
]


def select_current(lesson_number, check_time=None):
    # If check time is not given, default to current time
    check_time = check_time or datetime.now().time()
    begin_time = lessons_time[lesson_number][0]
    end_time = lessons_time[lesson_number][1]
    return check_time >= begin_time and check_time <= end_time
