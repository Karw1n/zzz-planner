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

def optimum_wake_up_time(bed_time):
  wake_times = end_of_sleep_cycle_wake_times(bed_time)
  return (wake_times[5], wake_times[6])

