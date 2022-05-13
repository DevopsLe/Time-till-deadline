from datetime import datetime

user_input = input("Enter your goal with the Deadline separated by the colon (Format - Goal:DD.MM.YYYY) \n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.today()

# how many days till the deadline
time_till = deadline_date - today
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Dear user! Time remaining for your goal {goal} is {hours_till} hours")
