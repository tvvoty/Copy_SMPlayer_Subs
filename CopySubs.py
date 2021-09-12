import pyperclip
import re


timestamp_pattern = re.compile(r"@ (\d+.\d+)")
subtitle_pattern_old = re.compile(
    r"Dialogue: 0,(0):(00):(22).(89),(0):(00):(24).(68),MX Flashback,,0000,0000,0000,,(I feel something well up,)")
subtitle_pattern = re.compile(
    r"Dialogue: 0,(\d+):(\d+):(\d+)\.(\d+),(\d+):(\d+):(\d+).(\d+),[^,,]*,,\d+,\d+,\d+,,(.*)")


subtititle_file = "/home/tvvoty/LinuxAdd/Vlcfilms/9/Barakamon09.ass"  # 508 dialogs in this file
log_file = "/home/tvvoty/LinuxAdd/GitHub/Copy_SMPlayer_Subs/SMPlayerLogs.log"
# log_text = pyperclip.paste()

with open(log_file, mode='r', encoding='utf-8') as file:
    log_text = file.read()

with open(subtititle_file, mode='r', encoding='utf-8') as file:
    subtititle_file_content = file.read()

time_stamps = timestamp_pattern.finditer(log_text)
dialogues = subtitle_pattern.finditer(subtititle_file_content)

time_stamps_list = []
dialogues_list = []
dialogues_count_list = []

for match in time_stamps:
    # print(match.group(1))
    time_stamps_list.append(match.group(1))

for match in dialogues:
    # print(match.group(1))
    dialogues_list.append(match.group(0))


dialogue_count = 0
for x in dialogues_list:
    print(x)
    dialogue_count += 1
print(f"Total amount of dialogues: {dialogue_count}")


start_sub_hour = subtitle_pattern.findall(subtititle_file_content)
# print(start_sub_hour)
start_sub_minute = 0
start_sub_second = 0
start_sub_msecond = 0

finish_sub_hour = 0
finish_sub_minute = 0
finish_sub_second = 0
start_sub_msecond = 0

# print(match.group(1)[-1])
# print(f"The last time stamp is: {time_stamps_list[-1]}")

# pyperclip.copy("subtitles")


# log_text = pyperclip.paste()
