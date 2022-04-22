
""""
credits:
rob226@gmail.com

install:
pip install googletrans==3.1.0a0


use:
copy the caption.sbv in the same folder as this script then command:

python3 subs.py moviename

the script will create a folder with your moviename, open it adn upload the txt file to youtube


for translating & converting to timed subs use:
python3 subs.py -tr textfile.txt

"""""



import os
import datetime
import sys
import random
from googletrans import Translator
from convert import *
translator = Translator()
#wachten tussen de zinnen (met komma)
sec1 = 3

#automatisch wachten aan de hand van aantal woorden
autodelay = 1
woord = 0.5 #wachttijd per woord per lijn

#wachten tussen de zinnen na een punt(.)
zinsec = 5

#starttijd 0 voor standaard (automatisch) begin met subs vanaf aantal sec (max 59 sec)
starttijd = 2


val2 = 0
file1 = ""
starttijd1 = ""
laatstetot = ""
tot2 =""

    
tempsec1 = sec1



def help1():
    print("\ncredits:\n\
rob226@gmail.com\n\
\n\
use:\n\
copy the caption.sbv in the same folder as this script then command:\n\
\nConverting only from youtube subs to custom timed subs:\n\
python3 subs.py moviename\n\
the script will create a folder with your moviename, open it and upload the txt file to youtube\n\
\n\
Translating textfile(from any language) to english & converting to timed subs use:\n\
python3 subs.py -tr textfile.txt")


def randomnu():
	randnu7 = str(random.randint(1, 100)) + str(random.randint(1, 100))  + str(random.randint(1, 100))
	return randnu7

def tijd(x,sec1,c):
    eind = x.split(",")
    tijd = eind[c]
    sec = tijd.split(":")[2]
    sec = int(sec.split(".")[0])
    if c == 0:
        if starttijd != 0:
            #tijd = tijd.replace(":" + str(sec),":" + str(starttijd1))
            tijd = "0:00:"+ starttijd1 +".000"
        res = tijd
    else:
        res = tijd.replace(":" + str(sec),":" + str(sec + sec1))
    return res

def cor(tijd1,sec1,eerste,sp):
    #print(tijd)
    if sp == 1:
        tijd1 = tijd1.split(",")[0]
    sec = tijd1.split(".")[0]
    sec = time_to_sec(sec)  
    sec2 = sec + sec1
    res = str(sectotime(sec2)) +".000"
    return res

def sectotime(b) :
    conversion = datetime.timedelta(seconds=b)
    return conversion

def time_to_sec(t):
   h, m, s = map(int, t.split(':'))
   return h * 3600 + m * 60 + s

def submain(dir1,x):
  global starttijd1
  if starttijd < 10 and starttijd > 0:
      starttijd1 = "0" + str(starttijd)
  else:
      starttijd1 = str(starttijd)
  #override
  if x == 0:
      fname3 = "captions.sbv"
      try:
        os.popen('cp ' + fname3 + " " + dir1 + "/" + fname3)
      except:
        print("cannot copy captions.sbv")
  else:
      fname3 = "captions.txt"
      
  with open(fname3, 'r') as f:
    global tot,start,sec1,laatstetot,val2
    eerstelijn = f.readline()
    start = tijd(eerstelijn,sec1,0)
    eind = cor(start,sec1,1,0)
    tot = start + "," + eind + '\n'
    #print(start + "," + eind +'\n')
    for line in f:
        if ":" in line and "," in line and "." in line:
            line = line.strip()
            #als we moeten wachten na een punt(.)
            if sec1 == zinsec:
                start = cor(eind,sec1,1,0)
            else:    
                start = eind
            #reset wachttijd    
            sec1 = tempsec1    
            eind = cor(start,sec1,0,0)
            #print(start + "," + eind)
            tot2 =  start + "," + eind +'\n'
            laatstetot = tot2
        else:    
            line = line.strip()
            #een try:
            #voor filteren van lege lijnen
            try:
                if autodelay == 1 :
                    number_of_words = len(line.split())
                    wt = round(number_of_words * woord)
                    if wt == 0:
                        wt = 1    
                    eind = cor(tot2,wt,0,1)
                    tot3 = start + "," + eind +'\n'
                    tot = tot + tot3   
                elif tot2 != "":
                    tot = tot + tot2
                tot2 = ""
            
                if line[-1] == ".":
                    sec1 = zinsec
                else:
                    sec1 = tempsec1
            except:
                pass
                
            tot = tot + line + '\n'
  with open(dir1 + '/captions.txt', 'w') as f:
        f.write(tot)   
  val2 = laatstetot.split(",")[0]
  val2 = val2.split(".")[0]
  print("Video cannot be longer than: " + val2)
  
  try:
      os.remove("captions.txt")
  except:
      pass      
  print("Process completed")



    
def translate(file1,x):
        global file9
        file9 = "translated_" + randomnu() + ".txt"
        f = open(file1, encoding = "ISO-8859-1")
        if f.mode == 'r':
            contents = f.read()
            #print(contents)
            
        #translate from NL to ENG
        #result = translator.translate(contents, src='nl', dest='en')
        #auto detect language
        result = translator.translate(contents,  dest='en')
        print("\nTranslated to english complete")
        with open(file9, 'w') as f:
            f.write(result.text)
        coverttosub(file9)
        if x != None:
            dir1 = x
            x = file1
        else:  
            dir1 = str(input("\nTiming subs aanpassen?\nvul een project/video naam in\n(leeg is exit): "))
            x = "telegram.txt"
            
        if dir1 != "":
              try:
                os.makedirs(dir1)
              except:
                pass
              try:
                os.popen('mv ' + x + " " + dir1 + "/original.txt")
              except:
                print("Cannot Move to original.txt")                
              submain(dir1,1)
        else:
          print("Exit")
#start
try:
   dir1= sys.argv[1]
except :
	 dir1 = "output"

if dir1 == "-help":
    help1()
    sys.exit()
    
    
if dir1 == "-tr":
    try:
      translate(sys.argv[2],None)
      sys.exit()  
    except:
      sys.exit()      
else:       
    try:
      os.makedirs(dir1)
      print(submain(dir1,0))  
    except:
      pass     

 
    
    