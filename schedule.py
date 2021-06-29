import datetime

def run_schedule(date, times):
    minutes, hours, weekdays, monthdays, months = [], [], [], [], []  # Переопределяем время
    # нужны только эти значении, так как остальные значение спокойно находятся по каленьдарю
    # также если в переменных minutes, hours первое значение 0, то прибавляем 15 минуты и 1 час к переменной date
    # в остальных значениях таких как weekdays, monthdays и months не может содержать значение 0
    matrix_minutes = datetime.timedelta(minutes=15)
    matrix_hours = datetime.timedelta(hours=1)
    for_minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']

    if times[-1] == ';':                                        # Если последний символ ";"
        times = times[0:-1]                                      # Перезаписываем без последнего символа

    # записываем значению каждой строке свои значении времени
    times = times.split(';')
    minutes += times[0].split(',')
    hours += times[1].split(',')
    weekdays += times[2].split(',')
    monthdays += times[3].split(',')
    months += times[4].split(',')

    run_date_minute = date.minute
    run_date_hour = date.hour
    run_date_month = date.month
    run_date_day = date.day
    run_date_year = date.year

    if '0' in minutes:
        date += matrix_minutes
    elif '0' in hours:
        date += matrix_hours

    # преобразуем все значение в массиве в целое число
    minutes = [int(min) for min in minutes]
    hours = [int(hour) for hour in hours]
    weekdays = [int(weekday) for weekday in weekdays]
    monthdays = [int(monthday) for monthday in monthdays]
    months = [int(month) for month in months]
    new_date = 0

    if len(minutes) == 1:
        run_date_minute = minutes[0]
    else:
        while run_date_minute not in minutes:
            run_date_minute += 1
            if run_date_minute == 60:
                run_date_minute = 0
    if len(hours) == 1:
        run_date_hour = hours[0]
    else:
        while run_date_hour not in hours:
            run_date_hour += 1
            if run_date_hour == 24:
                run_date_hour = 0
    if len(months) == 1:
        run_date_month = months[0]
    else:
        while run_date_month not in months:
            run_date_month += 1
            if run_date_month == 13:
                run_date_month = 1
    if len(monthdays) == 1:
        run_date_day = monthdays[0]
    else:
        while run_date_day not in monthdays:
            run_date_day += 1
            if run_date_day == 31:
                run_date_day = 1

    if run_date_day == 29 and run_date_month == 2:
        run_date_year = 2020
        while (datetime.datetime(run_date_year, run_date_month, run_date_day).isoweekday() + 1) % 7 not in weekdays:
            run_date_year += 4
    else:
        while (datetime.datetime(run_date_year, run_date_month, run_date_day).isoweekday() + 1) % 7 not in weekdays:
            run_date_year += 1



    if run_date_month <= 10:
        run_date_month = '0' + str(run_date_month)

    if run_date_day <= 10:
        run_date_day = '0' + str(run_date_day)

    if run_date_hour <= 10:
        run_date_hour = '0' + str(run_date_hour)

    if run_date_minute <= 10:
        run_date_minute = '0' + str(run_date_minute)


    print('{}.{}.{} {}:{}'.format(run_date_day, run_date_month, run_date_year, run_date_hour, run_date_minute))


#matrix_time = "0,45;12;1,2,6;3,6,14,18,21,24,28;1,2,3,4,5,6,7,8,9,10,11,12;"

# matrix_date = (datetime.datetime(2010, 7, 9, 23, 36))


#matrix_time = input("Перечислите все выбранные ячейки")
#matrix_date = input("Введите дату точку отчета")

matrix_time = "45;12;1;29;2;"
matrix_date = datetime.datetime.now();
# print(matrix_date)

run_schedule(matrix_date, matrix_time.lstrip())
