# 508 dialogs in this file
# log_file = "/home/tvvoty/LinuxAdd/GitHub/Copy_SMPlayer_Subs/SMPlayerLogs.log"
# with open(log_file, mode='r', encoding='utf-8') as file:
#     log_text = file.read()
time_stamps = timestamp_pattern.finditer(log_text)
dialogues = subtitle_pattern.finditer(subtititle_file_content)
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
