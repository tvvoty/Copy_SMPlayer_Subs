import pyperclip
import re


pattern_for_timestamp = re.compile(r"@ (\d+.\d+)")

subtititle_file = "/home/tvvoty/LinuxAdd/Vlcfilms/9/Barakamon09.ass"
# log_text = pyperclip.paste()

with open("/home/tvvoty/LinuxAdd/GitHub/Copy_SMPlayer_Subs/SMPlayerLogs.log", mode='r', encoding='utf-8') as file:
    log_text = file.read()

time_stamps = pattern_for_timestamp.finditer(log_text)

# print(time_stamps[1])
time_stamps_list = []
for match in time_stamps:
    print(match.group(1))
    time_stamps_list.append(match.group(1))

    # print(match.group(1)[-1])
print(f"The last time stamp is: {time_stamps_list[-1]}")

# pyperclip.copy(subtitles)
