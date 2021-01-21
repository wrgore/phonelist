#!/bin/python3

#import list of "dirty" data and creates empty list for converted data
source = input("Enter your data source file name: \n")
rawdata = open(source, "r")

cleandata = []

#convert data to cleaner format for final wordlist
for x in rawdata:
	cleandata.append(x.strip())
	
#open file which will recieve the output
f = open("output.txt", "a")

#iterates through both lists and formats data
i = 0000

for n in cleandata:		
	for i in range (0000, 10000):
		print(str(n)+'{0:04}'.format(i), file=f),
		
#close the file after wrting is complete and inform user of completion
f.close
print("Your data has been printed to output.txt. Please change the name if you do not intend to use this script to append additional data to the file.")
