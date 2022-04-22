# Automate your Youtube Subtitles (with telegram bot)

Boost your youtube video? Than its time to use subtitles.
This script makes it a lot easier to create a subtitle in a few seconds from plain text in every language.

Normally if you have a standard text (in a non-English language) you first have to run it through google translate and then save it as a text file, you have to load it at youtube studio and then adjust the timing.
Then YouTube will determine the timing of the subtitles itself and this can take a while, after that then you have to adjust the timing of these subtitles yourself because its never good and its time consuming if you have a longer video. Also when the video is long youtube will spread the subs along the video so its possible to look at the same subs for 1 of 3 minutes and that's something you dont want.

## how does it work?
The script allows you to turn plain text (in any language) to be translated into english and converted into an (.srt subtitle) timed format which you can upload to youtube studio. You can adjust the timing beween sentences and use a custom starttime. So if there is no dot (.) at the end of the sentence it will continue reading as the sentence is not completed. When a sentence is completed the script will wait for a longer time.  

There are 2 options:<br>
- Run it as a telegram bot<br>
- Run it Stand alone and control it via terminal<br>

## Hardware needed?
- Any ubuntu system will do im using an X64 machine with ubuntu 20+<br>
- Raspberry should work also (not tested)

## Libraries
This script will use google translate so install the correct library for it.  
- make sure you are using googletrans==3.1.0a0, install it via `pip install googletrans==3.1.0a0`

# Option 1: Run stand alone
- Login to youtube studio and download the file with your timed subs (caption.sbv). it will look like:
![image](https://user-images.githubusercontent.com/13587295/164727584-9d35d3f9-40e5-4dbb-94f6-91e63231930d.png)
- Open the subs.py and edit some timing (if needed) in the top of the script  

#auto wait   
woord = 0.5 #sleeptime(readtime) per word  

#sleeptime after complete sentence with a dot(.)  
zinsec = 5  

#start time first sub (max 59 sec)  
subs.starttijd = 2   

- copy the caption.sbv youve downloaded from youtube studio in the same folder as this script and then run command:   
`python3 subs.py moviename`

the script will create a folder with your moviename, open it and upload the txt file to youtube.  
as you can see the timing is adjusted accoring to the3 settings which you can made.  
- Before (generated by youtube captions.sbv):   
![image](https://user-images.githubusercontent.com/13587295/164727584-9d35d3f9-40e5-4dbb-94f6-91e63231930d.png)
- After:  
![image](https://user-images.githubusercontent.com/13587295/164727784-3c4bc4e4-6142-4f2a-b7f9-db258809c79d.png)

- for plain text translating & converting to timed subs  
Just copy some text from a website and paste it into a txt file and run:
`python3 subs.py -tr textfile.txt`

# Option 2: Control it via Telegram
- Create a Telegram bot @botfather see: https://t.me/botfather and https://core.telegram.org/bots
- Put your key token in key.txt
- Lookup your bot in telegram and send it a msg, send /suhelp to get the help menu, it wil look like:
![image](https://user-images.githubusercontent.com/13587295/164730132-c8f527dc-4c17-420d-bb16-b3667476fd95.png)  
- Start with
`/sustart`  
and paste some text (in your own language), you can send multiple messages which will be merged together. Start the translating with `/tra projectname` in this example in using `test`  

![image](https://user-images.githubusercontent.com/13587295/164730863-a758c1ea-fc52-45c0-a32a-fc5315338d1e.png)

After that it will send you the results and send you the timed subs in a file which is named after your projectname

![image](https://user-images.githubusercontent.com/13587295/164731471-4b3a7935-55c7-40e7-aeca-7caaa6ed7ee3.png)

Result:  
![image](https://user-images.githubusercontent.com/13587295/164727784-3c4bc4e4-6142-4f2a-b7f9-db258809c79d.png)

I named the projectname test so the files wil be stored in /test/ like /test/test.txt, in the folder you can find some more files which speaks for themselves.
![image](https://user-images.githubusercontent.com/13587295/164732244-732f30a4-cd3f-4f3d-a128-96e5a81f26c8.png)

You can adapt the timings to your need with /tim and the options like `tim 0.5 5 2` which is standard





## Youtube video to come...






