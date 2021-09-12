import pyperclip
import re

subtitle_count_pattern = re.compile(r"Dialogue")
subtititle_file = "/home/tvvoty/LinuxAdd/Vlcfilms/9/Barakamon09.ass"

with open(subtititle_file, mode='r', encoding='utf-8') as file:
    subtititle_file_content = file.read()
c = 0
dialogues_count = subtitle_count_pattern.finditer(subtititle_file_content)
for match in dialogues_count:
    c += 1
    print(match)
print(c)
dialogues_count_list = []

for match in dialogues_count_list:
    print(match.group(1))
    dialogues_count_list.append(match.group(0))

dialogue_count = 0
for x in dialogues_count_list:
    print(x)
    dialogue_count += 1
print(dialogue_count)
