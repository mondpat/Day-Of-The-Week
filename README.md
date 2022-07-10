# Day-Of-The-Week
## EN (CZ bellow):
Console program for calculating the day of the week based on the given date.
The calculation is consist of a some functions:
- AreDateSame - Checks if the given two data are the same (day1, day2, month1, moth2), if so, function will return true.
- NumberOfDays - Return the number of day from beginning of the year to the given date (day, month).
- IsYearLeap - If the given year is a leap yer then true is retuned.
- NumberOfDaysPerYears - Count number of days from year 1 to given year, including a leap years.
- GetDayOfTheWeek - The day of the week is determined based on the remainder after dividing the number of days from year 1 to given date by number 7.

## CZ:
Konzolový program pro výpočet dne v týdnu, dle zadaného data.
Projekt sestává z několika funkcí:
- JsouDataStejná - Vrátí true, pokud jsou v parametrech při volání vloženy stejné dny a měsíce.
- PočetDní - Vrátí počet dní od počátku roku až do zadaného dne a měsíce.
- JeRokPřestupný - Zkontroluje zda je rok zadaný jako parametr při volání přestupný. Pokud ano, vrátí true.
- PočetDníZaRoky - Vypočítá počet dní od roku 1 do zadaného roku (přestupné roky se počítají souběžně s nepřestupnými).
- UrčiDenVTýdnu - Určí den v týdnu podle zybtku po vydělením počtu dní od roku 1 do určeného data číslem 7.
