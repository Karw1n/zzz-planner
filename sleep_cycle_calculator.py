from datetime import datetime, timedelta
import json

OPTIMUM_CYCLE           = 5 # 5 Cycles is recommended
OPTIMUM_RECOVERY_CYCLE  = 6 # 6 Cycles is recommended for full recovery.
AVG_TIME_TO_SLEEP_MIN   = 15 # Average time for someone to sleep
SLEEP_CYCLE_TIME_MIN    = 90 # Typical sleep cycle time
JSON_FILE_LOCATOIN      = 'data/sleep_cycle_desc.json'


def get_optimum_wake_up_time(sleep_time: datetime):
  time_to_fall_asleep = get_time_to_fall_asleep()
  total_sleep_time = get_sleep_cycle_time() * OPTIMUM_CYCLE
  return sleep_time + time_to_fall_asleep + total_sleep_time

def get_optimum_sleep_time(wake_time: datetime):
  time_to_fall_asleep = get_time_to_fall_asleep()
  total_sleep_time = get_sleep_duration(OPTIMUM_CYCLE)
  return wake_time - total_sleep_time - time_to_fall_asleep


def get_time_to_fall_asleep():
  return timedelta(minutes=AVG_TIME_TO_SLEEP_MIN)

def get_sleep_cycle_time():
  return timedelta(minutes=SLEEP_CYCLE_TIME_MIN)

def get_sleep_duration(num_cycle):
  return get_sleep_cycle_time() * num_cycle

def build_cycle_description_lookup(file_path):
  with open(file_path) as file:
    data = json.load(file)
    return {item['number_of_cycles']: item['description'] for item in data}

def get_cycle_description(cycle_lookup, sleep_cycle_number):
  return cycle_lookup.get(sleep_cycle_number, 'Cycle number not found.')


# Test value:
# Testing if the optimum sleep time answer is equal to optimum wake time answer
# Optimum wake up from sleep time == Optimum sleep time from wake up
standard_sleep_time = datetime.strptime('22:00', '%H:%M')
optimum_wake = get_optimum_wake_up_time(standard_sleep_time)
print(get_optimum_sleep_time(optimum_wake) == standard_sleep_time)
# Test Passed

# Vice Versa
standard_wake_time = datetime.strptime('6:00', '%H:%M')
optimum_sleep_time = get_optimum_sleep_time(standard_wake_time)
print(get_optimum_wake_up_time(optimum_sleep_time) == standard_wake_time)
# Test Passed