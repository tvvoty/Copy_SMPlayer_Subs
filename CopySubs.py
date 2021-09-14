import pyperclip
import re


def convert_sub_time_to_miliseconds(hours, minutes, seconds, miliseconds):
    # ms_from_hours = hours * 3600000
    # ms_from_minutes = minutes * 60000
    # ms_from_seconds = seconds * 1000

    # return miliseconds + ms_from_hours + ms_from_minutes + ms_from_seconds
    return int(miliseconds + "0") + (int(seconds) * 1000) + (int(minutes) * 60000) + (int(hours) * 3600000)


def convert_sub_timestamp_to_miliseconds(seconds, miliseconds):
    return int(miliseconds[0:3]) + (int(seconds) * 1000)


# Patterns section
timestamp_pattern = re.compile(r"@ (\d+).(\d+)")
subtitle_pattern_old = re.compile(
    r"Dialogue: 0,(0):(00):(22).(89),(0):(00):(24).(68),MX Flashback,,0000,0000,0000,,(I feel something well up,)")
subtitle_pattern = re.compile(
    r"Dialogue: 0,(\d+):(\d+):(\d+)\.(\d+),(\d+):(\d+):(\d+).(\d+),[^,,]*,,\d+,\d+,\d+,,(.*)")


# File section
subtititle_file = "/home/tvvoty/LinuxAdd/Vlcfilms/9/Barakamon09.ass"  # 508 dialogs in this file
# log_file = "/home/tvvoty/LinuxAdd/GitHub/Copy_SMPlayer_Subs/SMPlayerLogs.log"
log_text = pyperclip.paste()

# with open(log_file, mode='r', encoding='utf-8') as file:
#     log_text = file.read()

with open(subtititle_file, mode='r', encoding='utf-8') as file:
    subtititle_file_content = file.read()


# Matching patterns
time_stamps = timestamp_pattern.finditer(log_text)
dialogues = subtitle_pattern.finditer(subtititle_file_content)
time_stamps_findall = timestamp_pattern.findall(log_text)

time_stamps_list = []
dialogues_list = []

for match in time_stamps:
    # print(match.group(1))
    time_stamps_list.append(match.group(1))

for match in dialogues:
    # print(match.group(1))
    dialogues_list.append(match.group(0))


dialogue_count = 0
for x in dialogues_list:
    # print(x)
    dialogue_count += 1
# print(f"Total amount of dialogues: {dialogue_count}")


start_sub_hour = subtitle_pattern.findall(subtititle_file_content)

# print(
#     f"The captured time stamp seconds is: {time_stamps_findall[-1][0]} \n The captured time stamp ms is: {time_stamps_findall[-1][1]}")

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

pyperclip.copy(subtitle[0][8])

# log_text = pyperclip.paste()
