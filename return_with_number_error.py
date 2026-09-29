calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

user_input = input("Hey user, enter a number of days and i will convert it to hours!")
calculated_value = days_to_units(user_input)
print(calculated_value)