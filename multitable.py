#! /usr/bin/python
# python script to generate random multiplication tables 
"""
Multiplication table generator
"""


import random

#This function randomizes and returns a list of twelve values from 1-12.
def arrayoftwelve():
    """makes a list of 12 random numbers"""
    referencetwelve = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    newtwelve = []
    while len(referencetwelve) > 0:
        derpnumber = random.randrange(13)
        if derpnumber not in newtwelve and derpnumber in referencetwelve:
            newtwelve.append(derpnumber)
            referencetwelve.remove(derpnumber)
    return newtwelve

#this function takes in two lists and outputs a proper 2d list 
def twodtwelves(fir, sec):
    """arranges a 2d list based on 2 1d lists"""	
    finalgrid = [[] for _ in range(14)]
    finalgrid[0] = ['X', sec[0], sec[1], sec[2], sec[3], sec[4], \
		    sec[5], sec[6], sec[7], sec[8], sec[9], sec[10], sec[11], 'X']
    finalgrid[1] = [fir[0], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[0]]
    finalgrid[2] = [fir[1], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[1]]
    finalgrid[3] = [fir[2], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[2]]
    finalgrid[4] = [fir[3], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[3]]
    finalgrid[5] = [fir[4], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[4]]
    finalgrid[6] = [fir[5], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[5]]
    finalgrid[7] = [fir[6], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[6]]
    finalgrid[8] = [fir[7], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[7]]
    finalgrid[9] = [fir[8], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[8]]
    finalgrid[10] = [fir[9], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[9]]
    finalgrid[11] = [fir[10], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[10]]
    finalgrid[12] = [fir[11], '', '', '', '', '', \
		    '', '', '', '', '', '', '', fir[11]]
    finalgrid[13] = ['X', sec[0], sec[1], sec[2], sec[3], sec[4], \
		    sec[5], sec[6], sec[7], sec[8], sec[9], sec[10], sec[11], 'X']
    return finalgrid

def maxitemlength(inputlist):
    """ Max item length """	
    maxlen = 0
    rows = len(inputlist)
    cols = len(inputlist[0])
    for row in xrange(rows):
        for col in xrange(cols):
            maxlen = max(maxlen, len(str(inputlist[row][col])))
    return maxlen

def printgrid(inputgrid):
    """ Printing the grid """
    if (inputgrid == []):
    # So we don't crash accessing a[0]
        print []
        return
    rows = len(inputgrid)
    cols = len(inputgrid[0])
    fieldwidth = maxitemlength(inputgrid)
    print "  ",
    for row in xrange(rows):
        if (row > 0): 
            print "\n  ",
        for col in xrange(cols):
            if (col > 0): 
                print " ",
            format1 = "%" + str(fieldwidth) + "s"
            print format1 % str(inputgrid[row][col]),

def main():
    """The Heavy Lifting"""
    columns = arrayoftwelve()
    rows = arrayoftwelve()
    grid = twodtwelves(columns, rows) 
    printgrid(grid)

if __name__ ==  "__main__":
    main()
