from helper import *
import os
print(os.name)
user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and conversion unit (example days:hours, days:hour) :\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"Days": days_and_unit[0], "Units": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)
    
 # Changes made from the Github
