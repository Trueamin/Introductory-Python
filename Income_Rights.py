def Income_rights():
    week_day = input('Please specify which days you work: ')
    if week_day == 'Friday':
        print('That`s Wrong! Friday is for rest.')

    weekly_hour = int(input('Please give me number of working hours per day: '))
    if weekly_hour < 8:
        print('You are so lazy!')

    per_hour = float(input('Please tell me the price you work per hour: '))
    if per_hour <= 40:
        print('This price is not worth it!')

    print('Days you work: ', week_day)
    print('The hours you work each day: ', weekly_hour)
    print('The price you work per hour: ', per_hour)

    Total_revenue = weekly_hour * per_hour

    return Total_revenue

revenue = Income_rights()
print('Total revenue: ', revenue)






