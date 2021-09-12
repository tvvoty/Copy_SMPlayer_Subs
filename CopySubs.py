import pyperclip
import re


pattern_for_timestamp = re.compile(r"@ \d+.\d+")

subtititle_file = ""
log_text = pyperclip.paste()


pyperclip.copy(subtitles)
