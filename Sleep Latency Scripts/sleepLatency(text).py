import csv
from datetime import datetime
import pandas as pd


def convert_to_datetime(time_str):
    try:
        return datetime.strptime(time_str, '%m/%d/%Y %I:%M:%S %p')
    except ValueError:
        try:
            return datetime.strptime(time_str, '%m/%d/%Y %I:%M %p')
        except ValueError:
            print("Error: Unable to parse time data:", time_str)
            return None

def calculate_sleep_latency(entries):
    wake_times = []
    light_sleep_time = None

    for entry in entries:
        time = convert_to_datetime(entry[1])
        level = entry[3]

        if level == 'wake':
            if 18 <= time.hour < 24:
                wake_times.append(time)
        elif level == 'light' or level == 'rem':
            if time.hour >= 18:
                light_sleep_time = time
                break

    if wake_times and light_sleep_time:
        wake_times_before_light_sleep = [wake for wake in wake_times if wake < light_sleep_time]

        if len(wake_times_before_light_sleep) > 4:
            first_wake_after_6pm = wake_times_before_light_sleep[0]
            last_wake_before_light_sleep = wake_times_before_light_sleep[-1]
            sleep_latency = (last_wake_before_light_sleep - first_wake_after_6pm).total_seconds() / 60

            print(
                f"First Wake after 6 PM: {first_wake_after_6pm}, Last Wake before 'light' sleep: {last_wake_before_light_sleep}, Sleep Latency: {sleep_latency} minutes")
            if sleep_latency <= 2:
                global count_2_minutes_or_less
                count_2_minutes_or_less += 1
            return sleep_latency, first_wake_after_6pm, last_wake_before_light_sleep

    return None, None, None



# Read data from CSV file
file_name = 'SP23_30SecondSleepStages.csv'
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

grouped_data = {}
for entry in data[1:]:
    participant_id = entry[0]
    date = entry[1].split()[0]  # Extract date portion of time
    key = (participant_id, date)

    if key not in grouped_data:
        grouped_data[key] = []
    grouped_data[key].append(entry)
calculated_count = 0
total_sleep_latency = 0
count_2_minutes_or_less = 0  # Counter for sleep latency points that are 2 minutes or less

# Calculate sleep latency for each participant and date
for key, entries in grouped_data.items():
    participant_id, date = key
    sleep_latency, first_wake, last_wake = calculate_sleep_latency(entries)
    if sleep_latency is not None:
        total_sleep_latency += sleep_latency
    else:
        calculated_count += 1
        print(f"Participant ID: {participant_id}, Date: {date}, Sleep Latency: Unable to calculate")

print("Total sum of sleep latency minutes:", total_sleep_latency)
print("Number of lines where sleep latency could not be calculated:", calculated_count)
print("Number of sleep latency points that are 2 minutes or less:", count_2_minutes_or_less)

df = pd.read_csv(file_name)
# Count unique values in column A
unique_count = df['Id'].nunique()

print("Number of unique values in column A:", unique_count)



def get_consecutive_wakes(participant_id, start_date, end_date, entries):
    consecutive_wakes = []
    current_span = []
    print(f"Entries for participant {participant_id} from {start_date} to {end_date}: {entries}")  # Add this line
    for entry in entries:
        time = convert_to_datetime(entry[1])
        level = entry[3]
        print(f"Processing entry: {entry}")  # Add this line

        if level == 'wake' and 18 <= time.hour < 24:
            current_span.append(time)
        else:
            if current_span:
                consecutive_wakes.append(current_span)
                current_span = []

    if current_span:
        consecutive_wakes.append(current_span)

    return consecutive_wakes



# Filter entries for participant 21101 for the specified date range
participant_id = '21101'
start_date = '3/05/2023'
end_date = '3/06/2023'
entries = grouped_data.get((participant_id, start_date), [])
for date in pd.date_range(start=start_date, end=end_date):
    date_str = date.strftime('%m/%d/%Y')
    entries.extend(grouped_data.get((participant_id, date_str), []))

consecutive_wakes = get_consecutive_wakes(participant_id, start_date, end_date, entries)
print(f"Consecutive wake times for Participant {participant_id} from {start_date} to {end_date}:")
for i, span in enumerate(consecutive_wakes, start=1):
    start_time = span[0].strftime('%m/%d/%Y %I:%M:%S %p')
    end_time = span[-1].strftime('%m/%d/%Y %I:%M:%S %p')
    print(f"Consecutive Wake Span {i}: from {start_time} to {end_time}")
print(consecutive_wakes)

