def days_to_unit(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"there are {number_of_days * 24} hours in {number_of_days} days."
    elif conversion_unit == "minutes":
        return f"there are {number_of_days * 24*60} minutes in {number_of_days} days."
    else:
        print("Unit is unsupported")


def validate_and_execute(days_and_unit_dictionary):
    try:
        number_of_days = int(days_and_unit_dictionary["Days"])

        # We want to do conversion for the positive number
        if number_of_days > 0:
            calculated_value = days_to_unit(number_of_days, days_and_unit_dictionary["Units"])
            print(calculated_value)
        elif number_of_days == 0:
            print("You enter Zero, please enter a valid positive number")
        else:
            print("You enter negative value, no conversion for you")
    except ValueError:
        print("your input is not a valid number. Don't ruin my code")