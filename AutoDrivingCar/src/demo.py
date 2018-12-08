from datetime import datetime, timedelta
from Object.Enum import CONST

def date_time(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")


d = date_time("2018-12-06 14:12:40.280939") - timedelta(day="2018-12-05 14:12:40.280938")
print(d)

