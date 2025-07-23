from datetime import datetime, timedelta
import json

OPTIMUM_CYCLE           = 5 # 5 Cycles is recommended
OPTIMUM_RECOVERY_CYCLE  = 6 # 6 Cycles is recommended for full recovery.
AVG_TIME_TO_SLEEP_MIN   = 15 # Average time for someone to sleep
SLEEP_CYCLE_TIME_MIN    = 90 # Typical sleep cycle time
JSON_FILE_LOCATOIN      = 'data/sleep_cycle_desc.json'


def get_optimum_wake_up_time(sleep_time: datetime):
  time_to_fall_asleep = get_time_to_fall_asleep()
  total_sleep_time = get_sleep_cycle_time * OPTIMUM_CYCLE
  return sleep_time + time_to_fall_asleep + total_sleep_time

def get_time_to_fall_asleep():
  return timedelta(minutes=AVG_TIME_TO_SLEEP_MIN)

def get_sleep_cycle_time():
  return timedelta(minutes=SLEEP_CYCLE_TIME_MIN)

def get_cycle_description(sleep_cycle_number):
  with open(JSON_FILE_LOCATOIN) as file:
    data = json.load(file)
    
    for item in data:
      if item['number_of_cycles'] == sleep_cycle_number:
        return item['description']
      
  return "Cycle number not found"

