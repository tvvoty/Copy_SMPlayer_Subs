import pyperclip
import re


def sub_time_to_ms(hours, minutes, seconds, miliseconds):
    return int(miliseconds + "0") + (int(seconds) * 1000) + (int(minutes) * 60000) + (int(hours) * 3600000)


def timestamp_to_ms(seconds, miliseconds):
    return int(miliseconds[0:3]) + (int(seconds) * 1000)


def binary_search(sub_list, timestamp):
    subtitle = []
    timestamp_ms = timestamp_to_ms(timestamp[-1][0], timestamp[-1][1])
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        sub_line_start = sub_time_to_ms(
            sub_list[mid][0], sub_list[mid][1], sub_list[mid][2], sub_list[mid][3])
        sub_line_end = sub_time_to_ms(
            sub_list[mid][4], sub_list[mid][5], sub_list[mid][6], sub_list[mid][7])
        # If a legit subtitle is found we go up and down to search if there are more around.
        if sub_line_start < timestamp_ms < sub_line_end:
            subtitle.append(sub_line)
            # Going down the list
            row = mid
            while sub_line_start < timestamp_ms:
                row += 1
                sub_line_start = sub_time_to_ms(
                    sub_list[row][0], sub_list[row][1], sub_list[row][2], sub_list[row][3])
                sub_line_end = sub_time_to_ms(
                    sub_list[row][4], sub_list[row][5], sub_list[row][6], sub_list[row][7])
                if sub_line_start < timestamp_ms < sub_line_end:
                    subtitle.append(sub_line)
            # Going up the list
            going_up(sub_line_end, timestamp_ms, mid)
            return subtitle
        if timestamp_ms > sub_line_end:
            low = mid + 1
        else:
            high = mid - 1
    return None


def going_up(sub_line_end, timestamp_ms, row):
    while sub_line_end > timestamp_ms:
        row -= 1
        sub_line_start = sub_time_to_ms(
            sub_list[row][0], sub_list[row][1], sub_list[row][2], sub_list[row][3])
        sub_line_end = sub_time_to_ms(
            sub_list[row][4], sub_list[row][5], sub_list[row][6], sub_list[row][7])
        if sub_line_start < timestamp_ms < sub_line_end:
            subtitle.append(sub_line)
    for i in range(5):
        row -= 1
        sub_line_start = sub_time_to_ms(
            sub_list[row][0], sub_list[row][1], sub_list[row][2], sub_list[row][3])
        sub_line_end = sub_time_to_ms(
            sub_list[row][4], sub_list[row][5], sub_list[row][6], sub_list[row][7])
        if sub_line_end > timestamp_ms:
            going_up(sub_line_start, timestamp_ms, row)
        return None


# Patterns section
timestamp_pattern = re.compile(r"@ (\d+).(\d+)")
subtitle_pattern = re.compile(
    r"Dialogue: 0,(\d+):(\d+):(\d+)\.(\d+),(\d+):(\d+):(\d+).(\d+),[^,,]*,,\d+,\d+,\d+,,(.*)")


# File section
# Put the path to your .ass subtitle file in to the "subtitle_file" variabe below".
subtititle_file = "/home/tvvoty/LinuxAdd/Vlcfilms/9/Barakamon09j.ass"
with open(subtititle_file, mode='r', encoding='utf-8') as file:
    subtititle_file_content = file.read()

log_text = pyperclip.paste()


# Matching patterns

time_stamps_findall = timestamp_pattern.findall(log_text)
print(time_stamps_findall)


print(
    f"timestamp seconds: {time_stamps_findall[-1][0]}\ntimestamp ms: {time_stamps_findall[-1][1]}")

time_stamp_in_ms = convert_sub_timestamp_to_miliseconds(
    time_stamps_findall[-1][0], time_stamps_findall[-1][1])
print(f"Time stamp in ms is: {time_stamp_in_ms}")
subtitle = []
for sub_line in subtitle_pattern.findall(subtititle_file_content):
    sub_line_start = convert_sub_time_to_miliseconds(
        sub_line[0], sub_line[1], sub_line[2], sub_line[3])
    # print(f"sub_line_start = {sub_line_start}")
    sub_line_end = convert_sub_time_to_miliseconds(
        sub_line[4], sub_line[5], sub_line[6], sub_line[7])
    # print(f"sub_line_end = {sub_line_end}")
    if sub_line_start < time_stamp_in_ms < sub_line_end:
        subtitle.append(sub_line)

print(f"The matching subtitle is: {subtitle}")

# print(start_sub_hour)

# print(match.group(1)[-1])
# print(f"The last time stamp is: {time_stamps_list[-1]}")

line_to_print = ''
for line in subtitle:
    line_to_print += line[8]

pyperclip.copy(line_to_print)

# log_text = pyperclip.paste()
