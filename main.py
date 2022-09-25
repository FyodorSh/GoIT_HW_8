# Завдання
# Вам треба реалізувати корисну функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.
#
# У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. Така структура
# представляє модель списку користувачів з їх іменами і днями народження. name — це рядок з ім'ям користувача,
# а birthday — це datetime об'єкт, в якому записаний день народження.
#
# Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить у консоль (за
# допомогою print) список користувачів, яких потрібно привітати по днях.
#
# Умови приймання
# get_birthdays_per_week виводить іменинників у форматі:
# Monday: Bill, Jill
# Friday: Kim, Jan
#
# Користувачів, у яких день народження був на вихідних, потрібно привітати у понеділок.
# Для відладки зручно створити тестовий список users та заповнити його самостійно.
# Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
# Тиждень починається з понеділка.

from datetime import date, timedelta
from collections import defaultdict


def birthday_this_year(date_for_change):
    return date(year=date.today().year, month=date_for_change.month, day=date_for_change.day)


def birthday_week_day(birthday):
    this_year_date = birthday_this_year(birthday)
    return next_working_day(this_year_date).strftime("%A")


def next_working_day(date_for_check):
    if date_for_check.weekday() < 5:
        return date_for_check
    elif date_for_check.weekday() == 5:
        return date_for_check + timedelta(days=2)
    else:
        return date_for_check + timedelta(days=1)


def get_birthdays_per_week(users):

    date_today = date.today()
    date_plus_7days = date_today + timedelta(days=7)

    users_for_print = [elem for elem in users if date_today <= birthday_this_year(elem["birthday"]) <= date_plus_7days]

    week_birthdays = defaultdict(list)
    for elem in users_for_print:
        week_birthdays[birthday_week_day(elem["birthday"])].append(elem["name"])

    for weekday, names in week_birthdays.items():
        print(f'{weekday}: {", ".join(names)}')


if __name__ == "__main__":
    users = [
        {
            "name": "Bill", "birthday": date(year=1984, month=9, day=15)
        },
        {
            "name": "Jill", "birthday": date(year=1984, month=9, day=25)
        },
        {
            "name": "Kim", "birthday": date(year=1984, month=9, day=27)
        },
        {
            "name": "John", "birthday": date(year=1984, month=9, day=27)
        },
        {
            "name": "Jack", "birthday": date(year=1984, month=9, day=30)
        },
        {
            "name": "Alex", "birthday": date(year=1984, month=10, day=1)
        },
        {
            "name": "Jan", "birthday": date(year=1984, month=9, day=28)
        }
    ]

    get_birthdays_per_week(users)
