#! /usr/bin/python
# python script to generate random multiplication tables 

import random

#This function randomizes and returns a list of twelve values from 1-12.
def ArrayOfTwelve():
	ReferenceTwelve=[1,2,3,4,5,6,7,8,9,10,11,12]
	NewTwelve=[]
	count = 0
	while len(ReferenceTwelve) > 0:
		DerpNumber=random.randrange(13)
		if DerpNumber not in NewTwelve and DerpNumber in ReferenceTwelve:
			NewTwelve.append(DerpNumber)
			ReferenceTwelve.remove(DerpNumber)
		count += 1
	return NewTwelve

#this function takes in two lists and outputs a 2d list with the right shape/scope
def TwoDTwelves(first, second):

	FinalGrid = [[] for _ in range(14)]
	FinalGrid[0]=['Corner',second[0],second[1],second[2],second[3],second[4],second[5],second[6],second[7],second[8],second[9],second[10],second[11],'Corner']
	FinalGrid[1]=[first[0],'','','','','','','','','','','','',first[0]]
	FinalGrid[2]=[first[1],'','','','','','','','','','','','',first[1]]
	FinalGrid[3]=[first[2],'','','','','','','','','','','','',first[2]]
	FinalGrid[4]=[first[3],'','','','','','','','','','','','',first[3]]
	FinalGrid[5]=[first[4],'','','','','','','','','','','','',first[4]]
	FinalGrid[6]=[first[5],'','','','','','','','','','','','',first[5]]
	FinalGrid[7]=[first[6],'','','','','','','','','','','','',first[6]]
	FinalGrid[8]=[first[7],'','','','','','','','','','','','',first[7]]
	FinalGrid[9]=[first[8],'','','','','','','','','','','','',first[8]]
	FinalGrid[10]=[first[9],'','','','','','','','','','','','',first[9]]
	FinalGrid[11]=[first[10],'','','','','','','','','','','','',first[10]]
	FinalGrid[12]=[first[11],'','','','','','','','','','','','',first[11]]
	FinalGrid[13]=['Corner',second[0],second[1],second[2],second[3],second[4],second[5],second[6],second[7],second[8],second[9],second[10],second[11],'Corner']

	return FinalGrid

def maxItemLength(a):
	maxLen = 0
	rows = len(a)
	cols = len(a[0])
	for row in xrange(rows):
		for col in xrange(cols):
			maxLen = max(maxLen, len(str(a[row][col])))
	return maxLen

def PrintGrid(InputGrid):
	if (InputGrid == []):
		# So we don't crash accessing a[0]
		print []
		return
	rows = len(InputGrid)
	cols = len(InputGrid[0])
	fieldWidth = maxItemLength(InputGrid)
	print "  ",
	for row in xrange(rows):
		if (row > 0): 
			print "\n  ",
	        #print "[ ",
	        for col in xrange(cols):
	        	if (col > 0): print " ",
			# The next 2 lines print a[row][col] with the given fieldWidth
			format = "%" + str(fieldWidth) + "s"
			print format % str(InputGrid[row][col]),
		#print "]",
	#print "]"
			
	
	
	#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in InputGrid]))

def main():
	Columns=ArrayOfTwelve()
	Rows=ArrayOfTwelve()
	Grid=TwoDTwelves(Columns, Rows) 
	PrintGrid(Grid)



if __name__ == "__main__":
	main()
