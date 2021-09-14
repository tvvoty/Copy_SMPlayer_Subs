import pyperclip
import re


def convert_sub_time_to_miliseconds(hours, minutes, seconds, miliseconds):
    return int(miliseconds + "0") + (int(seconds) * 1000) + (int(minutes) * 60000) + (int(hours) * 3600000)


def convert_sub_timestamp_to_miliseconds(seconds, miliseconds):
    return int(miliseconds[0:3]) + (int(seconds) * 1000)


# Patterns section
timestamp_pattern = re.compile(r"@ (\d+).(\d+)")
subtitle_pattern = re.compile(
    r"Dialogue: 0,(\d+):(\d+):(\d+)\.(\d+),(\d+):(\d+):(\d+).(\d+),[^,,]*,,\d+,\d+,\d+,,(.*)")


# File section
subtititle_file = "/home/tvvoty/LinuxAdd/Vlcfilms/9/Barakamon09.ass"
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
