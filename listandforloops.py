
to_seconds = 24 * 60 * 60
unit = "seconds"

def days_to_units(No_of_days):
        return (f"{No_of_days} days are {No_of_days * to_seconds} {unit}")

def validate_and_execute():
   try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calc_value =  days_to_units(user_input_number)
            print(calc_value)
        elif user_input_number == 0:
            print("you entered a 0,please enter a valid number")
        else:
            print("you enter negative number. no conversion")
   except ValueError:
       print("your input is not a valid number, dont ruin my program")



user_input = ""
while user_input != "exit":
  user_input = input("hey user, enter a number of days and i will convert to hours \n")
  for num_of_days in set(user_input.split(",")):
    validate_and_execute()