# Automate your Youtube Subtitles (with telegram bot)

Boost your youtube video? Than its time to use subtitles.
This script makes it a lot easier to create a subtitle in a few seconds from plain text in every language.

Normally if you have a standard text (in a non-English language) you first have to run it through google translate and then save it as a text file, you have to load it at youtube studio and then adjust the timing.
Then YouTube will determine the timing of the subtitles itself and this can take a while, after that then you have to adjust the timing of these subtitles yourself because its never good and its time consuming if you have a longer video. Also when the video is long youtube will spread the subs along the video so its possible to look at the same subs for 1 of 3 minutes and that's something you dont want.

## how does it work?
The script allows you to turn plain text (in any language) to be translated into english and converted into an (.srt subtitle) timed format which you can upload to youtube studio. You can adjust the timing beween sentences and use a custom starttime.  

There are 2 options:<br>
- Run it as a telegram bot<br>
- Run it Stand alone and control it via terminal<br>

## Hardware needed?
- Any ubuntu system will do im using an X64 machine with ubuntu 20+<br>
- Raspberry should work also (not tested)

## Libraries
- make sure you are using googletrans==3.1.0a0, install it via `pip install googletrans==3.1.0a0`

# Option 1: Run stand alone
- Login to youtube studio and download the file with your timed subs (caption.sbv). it will look like:
![image](https://user-images.githubusercontent.com/13587295/164724031-f131aa77-35a6-49d3-ab02-cb1042fd9fee.png)

- copy the caption.sbv in the same folder as this script then command:

python3 subs.py moviename

the script will create a folder with your moviename, open it adn upload the txt file to youtube


for translating & converting to timed subs use:
python3 subs.py -tr textfile.txt



## Youtube video to come...






