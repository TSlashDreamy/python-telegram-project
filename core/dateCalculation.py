import math
from datetime import date, datetime
from core import daySwitcher

global even_week, today, days, weeks, time, day


def calculate_even_week():
    global even_week, today, days, weeks, time, day

    days_a_week = 7
    day = datetime.today().weekday()
    today = date.today()
    start_year = date(date.today().year, 1, 1)
    days = today - start_year
    weeks = days.days / days_a_week
    weeks = math.floor(weeks)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")

    print("\n========================")
    print("🧮 Обрахування дати: ")
    print("🕑 Час:", time)
    print("📆 День тижня:", daySwitcher.switch_day(day))
    print("🗓️ Сьогоднішня дата:", today.strftime("%d/%m/%Y"))
    print("📆 Всього днів пройшло:", days.days)
    print("📆 Всього тижнів пройшло:", weeks)

    if weeks % 2 == 0:
        print("🟰 Парний тиждень")
        even_week = True
    else:
        print("➖ Не парний тиждень")
        even_week = False
