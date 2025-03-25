from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        delta = given_date - today_date
        return delta.days
    except ValueError:
        return "Будь ласка введіть дату в форматі 'рік-місяць-день'"

    
print(get_days_from_today('2021-10-9'))
print(get_days_from_today('2025-03-16'))
print(get_days_from_today('Неправильна дата'))