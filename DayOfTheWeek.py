def AreDatesTheSame(day, month, DayInMonth, AMonth):
    if(day == DayInMonth and month == AMonth):
        return True
    return False

def NumberOfDays(day, month, year):
    count = 0
    DayInMonth = 1
    AMonth = 1
    if(day == 1 and month == 1):
        return 1
    while(DayInMonth != day or month != AMonth):
        DayInMonth = 1
        count += 1
        if(AMonth in (1, 3, 5, 7, 8, 10, 12)):
            while(DayInMonth < 31 and not AreDatesTheSame(day, month, DayInMonth, AMonth)):
                count += 1
                DayInMonth += 1
        if(AMonth in (4, 6, 9, 11)):
            while(DayInMonth < 30 and not AreDatesTheSame(day, month, DayInMonth, AMonth)):
                count += 1
                DayInMonth += 1
        if(AMonth == 2):
            if(IsYearLeap(year)):
                while(DayInMonth < 29 and not AreDatesTheSame(day, month, DayInMonth, AMonth)):
                    count += 1
                    DayInMonth += 1
            else:
                while(DayInMonth < 28 and not AreDatesTheSame(day, month, DayInMonth, AMonth)):
                    count += 1
                    DayInMonth += 1
        if(AMonth != month):
            AMonth += 1
        elif(AMonth == month and DayInMonth == day):
            return count

def IsYearLeap(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
        else:
            return True

def NumberOfDaysPerYears(year):
    count = 0
    years = 1
    while(years != year):
        if(IsYearLeap(years)):
            count += 366
        else:
            count += 365
        years += 1
    return count

def GetDayOfTheWeek(day, month, year):
    count = NumberOfDays(day, month, year) + NumberOfDaysPerYears(year)
    count = count % 7

    match count:
        case 0: print("sunday")
        case 6: print("saturday")
        case 5: print("friday")
        case 4: print("thursday")
        case 3: print("wednesday")
        case 2: print("tuesday")
        case 1: print("monday")

print("Welcome to program for calculating a day of the week for a specific date, please enter a date you want to get the day for")

print("day: ", end='')
day = int(input())
while(day not in range (1,32)):
    print("the day have to be in range from 1 to 31")
    day = int(input())

print("month: ", end='')
month = int(input())
while(month not in range (1,13)):
    print("the month have to be in range from 1 to 12")
    month = int(input())

print("year: ", end='')
year = int(input())
while(year < 1):
    print("the year have to be a positive integer")
    year = int(input())

GetDayOfTheWeek(day, month, year)