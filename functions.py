to_seconds = 24 * 60 * 60
unit = "seconds"

def days_to_units(No_of_days):
    print (f"{No_of_days} days are {No_of_days * to_seconds} {unit}")
    print("all good")


#scope global variables and local variables check
def scope_check():
    print(unit)
    #print(No_of_days) #not working because it is not defined
    



days_to_units(23)
days_to_units(76)
