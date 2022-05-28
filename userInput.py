to_seconds = 24 * 60 * 60
unit = "seconds"

def days_to_units(No_of_days):
    return (f"{No_of_days} days are {No_of_days * to_seconds} {unit}")
  


user_input = int(input("hey user, enter a number of days and i will convert to hours \n"))

calc_value = days_to_units(user_input)

print(calc_value)