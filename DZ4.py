from datetime import datetime

users = [
    {"name": "John Doe", "birthday": "1985.03.25"},
    {"name": "Jane Smith", "birthday": "1990.03.26"}
]


today = datetime.today().date()
current_month = today.month

def get_upcoming_birthdays(users):
    upcoming_birthday = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = birthday.replace(year=today.year)
        if birthday>today:
            birthday_next_year = birthday.replace(year=today.year+1)
        days_left = (birthday - today).days
        if 0 <= days_left <= 7:
            formatted_date = birthday.strftime("%Y-%m-%d")
            upcoming_birthday.append (f'''{user['name']} - {formatted_date}''')
    return upcoming_birthday


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
