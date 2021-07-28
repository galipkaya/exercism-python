from datetime import date

# range end inclusive
def meetup_date(year, month, day_of_week, range_start, range_end, day_order=1):
    current_day_order = 0
    last_date = None
    for day in range(range_start, range_end+1):
        result_date = date(year, month, day)
        if result_date.strftime("%A") == day_of_week:
            current_day_order += 1
            last_date = result_date
        if current_day_order == day_order:
            return result_date

    if day_order == 6:
        return last_date

    raise MeetupDayException("Not Found")


max_months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def get_max_months(month, year):
    if month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    return max_months.get(month)


def meetup(year, month, week, day_of_week):
    if week == "teenth":
        # 13th, 14th, 15th, 16th, 17th, 18th, 19th
        return meetup_date(year, month, day_of_week, 13, 19)
    elif week == "1st":
        return meetup_date(year, month, day_of_week, 1, 7)
    elif week == "2nd":
        return meetup_date(year, month, day_of_week, 1, 14, 2)
    elif week == "3rd":
        return meetup_date(year, month, day_of_week, 1, 21, 3)
    elif week == "4th":
        return meetup_date(year, month, day_of_week, 1, get_max_months(month, year), 4)
    elif week == "5th":
        return meetup_date(year, month, day_of_week, 1, get_max_months(month, year), 5)
    elif week == "last":
        return meetup_date(year, month, day_of_week, 1, get_max_months(month, year), 6)


class MeetupDayException(Exception):
    pass
