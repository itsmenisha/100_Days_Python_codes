print("Welcome to leap year checker!!")


def is_leap(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def month_of_year(a, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return (month_days[month-1])


year = int(input("enter the year:"))
b = int(input("enter the month:"))
result = is_leap(year)
days = month_of_year(result, b)
print(result)
print(f"The days in this month are:{days}")
