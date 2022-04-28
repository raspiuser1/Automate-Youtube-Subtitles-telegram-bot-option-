import os
import sys
import time
import random

#starttijd
start = "0:00:05.000,0:00:00.000\n"
#tussentijd
tussen = "0:00:00.000,0:00:00.000\n"


result2 = ""
file4 = ""

def randomnu():
	randnu7 = str(random.randint(1, 100)) + str(random.randint(1, 100))  + str(random.randint(1, 100))
	return randnu7

#maximaal 50 karakters per lijn
def coverttosub(txt):
	global file4
	file4 = "converted" + randomnu() + ".txt"
	
	with open(txt,  encoding = "UTF-8") as f:
		lines = f.readlines()
		max_width = 50 
		result = ""
		col = 0
		result = start
		for line in lines:	
			for word in line.split():
				end_col = col + len(word)
				if col != 0:
					end_col += 1
				if end_col > max_width: 
					result += '\n'
					col = 0    
				if col != 0:
					result += ' ' 
					col += 1
				result += word 
				col += len(word)
			#print (result)
	
	with open(file4, 'w') as f:
			f.write(result)
	alinea()


def insertchar(string, index,char):
    zin = string[:index] + char + string[index:]
    return zin

def alinea():	
	with open(file4,  encoding = "UTF-8") as f:
		result2 = f.readlines()
		result3 = ""
		tel = 0
		for line in result2:
			if ". " in line and tel == 2:
					pos = line.find('. ') + 1
					if len(line[pos:]) > 20:
						line = insertchar(line, pos, "\n\n" + tussen)
					result3 +=  line 
			else:	
					result3 += line
			if tel == 2:
				result3 += '\n' + tussen
				tel = 0
			tel = tel + 1		
	with open(f'captions.txt', 'w') as f:
			f.write(result3)
	print("Converting Subs Finished")
#alinea()	
