#! /usr/bin/python
# python script to generate random multiplication tables 

import random

#This function randomizes and returns a list of twelve values from 1-12.
def ArrayOfTwelve():
    ReferenceTwelve=[1,2,3,4,5,6,7,8,9,10,11,12]
    NewTwelve=[]
    while len(ReferenceTwelve) > 0:
        DerpNumber=random.randrange(13)
        if DerpNumber not in NewTwelve and DerpNumber in ReferenceTwelve:
            NewTwelve.append(DerpNumber)
            ReferenceTwelve.remove(DerpNumber)
    return NewTwelve

#this function takes in two lists and outputs a proper 2d list 
def TwoDTwelves(f, s):
    FinalGrid = [[] for _ in range(14)]
    FinalGrid[0]=['X',s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],'X']
    FinalGrid[1]=[f[0],'','','','','','','','','','','','',f[0]]
    FinalGrid[2]=[f[1],'','','','','','','','','','','','',f[1]]
    FinalGrid[3]=[f[2],'','','','','','','','','','','','',f[2]]
    FinalGrid[4]=[f[3],'','','','','','','','','','','','',f[3]]
    FinalGrid[5]=[f[4],'','','','','','','','','','','','',f[4]]
    FinalGrid[6]=[f[5],'','','','','','','','','','','','',f[5]]
    FinalGrid[7]=[f[6],'','','','','','','','','','','','',f[6]]
    FinalGrid[8]=[f[7],'','','','','','','','','','','','',f[7]]
    FinalGrid[9]=[f[8],'','','','','','','','','','','','',f[8]]
    FinalGrid[10]=[f[9],'','','','','','','','','','','','',f[9]]
    FinalGrid[11]=[f[10],'','','','','','','','','','','','',f[10]]
    FinalGrid[12]=[f[11],'','','','','','','','','','','','',f[11]]
    FinalGrid[13]=['X',s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10],s[11],'X']
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
    for col in xrange(cols):
        if (col > 0): print " ",
        format = "%" + str(fieldWidth) + "s"
        print format % str(InputGrid[row][col]),

def main():
  Columns=ArrayOfTwelve()
  Rows=ArrayOfTwelve()
  Grid=TwoDTwelves(Columns, Rows) 
  PrintGrid(Grid)

if __name__ == "__main__":
	main()
