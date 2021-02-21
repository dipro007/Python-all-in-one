
# year, week, days
def find(number_of_days):
    # Assume that years is
    # of 365 days
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
               DAYS_IN_WEEK)
    days = (number_of_days % 365) % DAYS_IN_WEEK

    print("years = ", year,
          "\nweeks = ", week,
          "\ndays = ", days)


