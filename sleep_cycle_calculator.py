from datetime import datetime, timedelta

# bed_time: Float, the time of sleep in hours
# Currently returns a list of sleep cycles and the total sleep time.
# Constraint that needs to be added, 24 hour clock
def sleep_cycle_calculator(bed_time):
  time_to_fall_asleep = timedelta(minutes=15)  # Average time for someone to fall asleep
  sleep_cycle_time = timedelta(minutes=90)     # Typical sleep cycle time
  
  
  # The time the person falls asleep
  sleep_start_time = bed_time + time_to_fall_asleep
  
  # Optimum Cycles are 5 or 6. 3, 4 or 10.5 are okay if not often
  sleep_cycle_range = 10
  
  wake_times = {}
  
  for i in range(sleep_cycle_range):
    cycle = i + 1
    wake_time = sleep_start_time + (cycle * sleep_cycle_time)
    
    wake_times[cycle] = wake_time
  
  return wake_times


my_bed_time = datetime.strptime("21:00", "%H:%M")
my_wake_time_options = sleep_cycle_calculator(my_bed_time)

for sleep_cycle, wake_time in my_wake_time_options.items():
  print(f'Number of Sleep Cycles: {sleep_cycle}. Wake Up time: {wake_time.strftime("%I:%M %p")}')
  

# In order to add these sleep times a helper function is needed to accomodate for the 24 hour clock
# Returns the sum of two times on a 24 hour clock
