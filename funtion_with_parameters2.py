calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days,custom_message):
    print(f"{num_of_days} days are {20 * calculation_to_units} {name_of_unit}")
    print(custom_message)
days_to_units(20, "Awesome!")
days_to_units(35,"Looks Good!")
days_to_units(50, "Different!")
days_to_units(110, "Ok!")
days_to_units(365,"A Year!")