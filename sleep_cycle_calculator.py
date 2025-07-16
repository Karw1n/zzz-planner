from datetime import datetime, timedelta

def end_of_sleep_cycle_wake_times(bed_time):
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

# From 
def optimum_wake_up_time(wake_times):
  return (wake_times[5], wake_times[6])

# my_bed_time = datetime.strptime("22:45", "%H:%M")
# my_wake_time_options = end_of_sleep_cycle_wake_times(my_bed_time)

# for sleep_cycle, wake_time in my_wake_time_options.items():
#   print(f'Number of Sleep Cycles: {sleep_cycle}. Wake Up time: {wake_time.strftime("%H:%M")}')
  
# # Maybe create a time formatter so it's all in one universal metric
# print(optimum_wake_up_time(my_wake_time_options))