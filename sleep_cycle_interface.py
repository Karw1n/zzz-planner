from datetime import datetime, timedelta
from sleep_cycle_calculator import end_of_sleep_cycle_wake_times, optimum_wake_up_time

# user_input = input('Enter time (HH:MM, 24-hour format): ')


# bed_time = datetime.strptime(user_input, '%H:%M')

# wake_times = end_of_sleep_cycle_wake_times(bed_time)
# optimum_wake_times = optimum_wake_up_time(wake_times)

# print(f'If you sleep at {bed_time.strftime('%I:%M %p')}\nYou should wake up at:')
# for time in optimum_wake_times:
#   print(time.strftime('%I:%M %p'))

def sleep_cycle_interface():
  # User selects 12/24 hour clock for input and output
  time_format = get_time_format()
  
  if time_format == 24:
    while True:
      user_input = input('Enter time in 24-hour format (HH:MM): ')
      try:
        bed_time = datetime.strptime(user_input, '%H:%M')
        break # Input is valid, exit loop
      except ValueError:
        print('Invalid time format. Please enter in HH:MM.')
  else: # 12 hour clock
    while True:
      user_input = input('Enter time in 12-hour format (HH:MM AM/PM): ').strip()
      
      try:
        bed_time = datetime.strptime(user_input, '%I:%M %p')
        break # Valid input
      except ValueError:
        print("Invalid time format. Please enter in HH:MM AM/PM.")

  print(bed_time)
  
def get_time_format():
  while True:
    time_format = int(input('Enter time (12 or 24): ').strip())
    
    if time_format in [12, 24]:
      return time_format
    
    else:
      print('Invalid input. Please type \'12\' or \'24\'')
  