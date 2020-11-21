#!/usr/bin/env python3

#Cisco exams auto evaluation

class color:
     BOLD = '\033[1m'
     END = '\033[0m'

be = input("Hany szazalek lett a " + color.BOLD + "FEJEZETVIZSGA?   " + color.END)

x = float(be)

if x >= 92.5:
    jegy = 5
elif x >= 85.0:
    jegy = 4
elif x >= 77.5:
    jegy = 3
elif x >= 70.0:
    jegy = 2
else:
    jegy = 1
    
print(jegy)
