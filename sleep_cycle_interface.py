from datetime import datetime, timedelta
from sleep_cycle_calculator import end_of_sleep_cycle_wake_times, optimum_wake_up_time

user_input = input('Enter time (HH:MM, 24-hour format): ')


bed_time = datetime.strptime(user_input, '%H:%M')

wake_times = end_of_sleep_cycle_wake_times(bed_time)
optimum_wake_times = optimum_wake_up_time(wake_times)

print(f'If you sleep at {bed_time.strftime('%I:%M %p')}\nYou should wake up at:')
for time in optimum_wake_times:
  print(time.strftime('%I:%M %p'))
