import calendar

def get_weekday(date: str) -> int:
    year, month, day = map(int, date.split('-'))
    weekday = calendar.weekday(year, month, day)

    if weekday == 6:
        return 0
    else:
        return weekday + 1