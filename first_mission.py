from datetime import datetime

today = datetime.today().date()
print(today)

date_string = "2023-01-01"
print(date_string)

def get_days_from_today(date_string):
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Правильний формат 'РРРР-ММ-ДД'.")
    days_difference = (today - date).days
    return days_difference

days_difference = get_days_from_today(date_string)
print(days_difference)