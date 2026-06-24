hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
weekday = input("Day of the week: ")

if weekday == "Sunday":
    hourly_wage *= 2

daily_wage = hourly_wage * hours_worked
print(f"Daily wages: {daily_wage} euros")