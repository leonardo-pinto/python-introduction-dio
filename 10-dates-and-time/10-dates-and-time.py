from datetime import date, time, datetime, timedelta

def date_example():
    current_date = date.today()
    current_date_formatted = current_date.strftime('%d/%m/%Y')
    print(current_date)
    print(current_date_formatted)

def time_example():
    current_time = time(hour=10, minute=40, second=34)
    print(current_time)

def datetime_example():
    current_datetime = datetime.now()
    current_datetime_formatted = current_datetime.strftime('%c')
    print(current_datetime)
    print(current_datetime_formatted)

def date_diff():
    current_date = date.today()
    new_date = current_date - timedelta(days=852)
    print(new_date)

if __name__ == '__main__':
    date_example()
    time_example()
    datetime_example()
    date_diff()
