 #code by it4min
#t.me/LinuxH
#t.me/it4min
import os
os.system("clear")
baner = '''                                                   
   ______            __             __ 
  / ____/___  ____  / /_____ ______/ /_
 / /   / __ \/ __ \/ __/ __ `/ ___/ __/             
/ /___/ /_/ / / / / /_/ /_/ / /__/ /_ 
\____/\____/_/ /_/\__/\__,_/\___/\__/  

   t.me/LinuxH
   Programmer: @it4min                                             
'''
print(baner)
code = input(">>> Please enter the number code: ")
cra = '0123456789'
f = open("Numbers.vcf", 'a')
str = '''
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:@it4min
'''
for q1 in cra:
	for q2 in cra:
		for q3 in cra:
			for q4 in cra:
				for q5 in cra:
					for q6 in cra:
						for q7 in cra:
							phone = code+q1+q1+q3+q4+q5+q6+q7
							print (phone)
							f.write('TEL;TYPE:VOICE,CELL;VALUE=text:'+phone+str)
f.close()
							
							
							
							         
