# Copy_SMPlayer_Subs
A python script that attempts to help copying subtitles from SMPlayer into clipboard.

# Usage

Right now the script only works with .ass files.

1). You will need Python 3 installed on your system. After you've done that you will also need to install pyperclip python module for python (you should be able to do it by typing "pip install pyperclip" into the command line, if it doesn't work - look for solution online.)

.

2). Download CopySub.py file or all files in the repository (clicking on Code > Download zip, for example) and
paste the full path to the .ass subtitle file you want to copy subs from into the "subtitle_file" variable that's located on the 21 line in that file.

On Linux it will look something like this:
subtititle_file = "/path/to/file.ass"

And on Windows it should probably look something like that:
subtititle_file = "\\path\\to\\file.ass" , though I'm not sure.

Open SMPlayer and load the video.

.

3). Click View > SMPlayer Log, a log window will be open.
I'd recommend putting it on a different virtual desktop, to which you can switch with a keyboard shortcut, if you have those available on your system.

.

4). When you see a line that you want to copy, either press back and then forward or even better - Frame back step(it's just one button and you can map it in the settings to a handy key).
This action is required in order to get the timestamp in the log.

Go to the log window and press the "Copy" key.
You can do it just by Right-Clicking on it or, if the button is in focus (either you
pressed it before or you selected it with Tab button), you can just press Space (at least that's
how it works on my system), that's how I do it.

.

5). Run the CopySub.py file. You can usually do it by typing "python3 path/to/file.py" or "python path/to/file.py" into the command line or sometimes you can just double click on the file. The subtitles should be
copied into your clipboard after this.

.

It's highly recommended automate the thing - at least the last step, but even better - all of it.
On Linux with KDE you should be able to automate the last step by:

First, modifying included .sh file - delete everything except the first two lines and paste the path to the location of CopySub.py file on your system, so it's gonna look like:

#!/bin/bash

python3 /path/to/CopySubs.py

Then go to Settings > Workspace > Shortcuts > Custom Shortcuts, then do Edit > New > Global Shortcut > Command/URL, choose a shortcut and then pass the path to the .sh file in the action tab.
You should probably be able to do it on other Linux distributions, Unix systems and Windows too, but I don't know how you'd do it. You can probably try using AutoKey or AHK for that.

If you want to modify everything else - you can look at what I did in the bash script and try to do something similar with bash, or anything else available to you on your platform. In my case - it uses xdotool to manipulate keyboard presses, you can check out examples how to use it on their github page, but here's an overview how what I wrote for myself works:

#!/bin/bash - just says to execute the script with bash

xdotool key BackSpace; - press the frame back button

sleep 0.2; - wait for a while to mitigate buttons jamming

xdotool key "alt+d"; - press a shortcut to switch to a virtual desktop with the log window

sleep 0.1;

xdotool key space; - if you previously copied text from the log window the copy button will be in focus and you can copy again just by pressing space

sleep 0.1;

xdotool key "alt+e"; - switch to a virtual desktop with yomichan to translate stuff

python3 /home/tvvoty/LinuxAdd/GitHub/Copy_SMPlayer_Subs/CopySubs.py - run the script itself
