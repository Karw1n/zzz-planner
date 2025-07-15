
# bed_time: Float, the time of sleep in hours
def sleep_cycle_calculator(bed_time):
  time_to_fall_asleep = 15  # Average time for someone to fall asleep
  sleep_cycle_time_min = 90     # Typcial sleep cycle time
  sleep_cycle_time_hr = round((sleep_cycle_time_min / 60), 2)
  
  # The time the person falls asleep
  sleep_start_time = bed_time + time_to_fall_asleep
  
  # Optimum Cycles are 5 or 6. 3, 4 or 10.5 are okay if not often
  sleep_cycle_range = 10
  
  wake_times = {}
  
  for i in range(sleep_cycle_range):
    cycle = i + 1
    wake_time = (cycle * sleep_cycle_time_hr)
    print(wake_time, cycle, sleep_cycle_time_hr)
    wake_times[cycle] = wake_time
  
  return wake_times


my_bed_time = 9
my_wake_time_options = sleep_cycle_calculator(my_bed_time)

for sleep_cycle, wake_time in my_wake_time_options.items():
  print(f'Sleep Cycle: {sleep_cycle}. Wake Up time: {wake_time}')
  

  