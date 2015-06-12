#part 1- read in a sudoku puzzle
#formatted in 9 lines with a + as a blank
import sys
import os
dir = os.path.dirname(__file__)
sudokopuzzlepath = os.path.join(dir, 'sudokopuzzle1.txt')

Matrix = [[0 for x in range(9)] for x in range(9)]

with open(sudokopuzzlepath) as f:
	row_counter=0
	for line in f:
		column_counter=0
#		print "row", row_counter
		for character in line:
#			print "column", column_counter
			if column_counter < 9:
				Matrix[row_counter][column_counter]=character
			column_counter+=1
		row_counter+=1

#print Matrix
i=0
while i < 9:
	print Matrix[i]
	i+=1

#write a method to check for valid row
#takes in matrix [][]
#contains no repeats

#write a method to check for valid column
#takes in matrix [][]


#write a method to check for valid cube
#takes in matrix [][]


	
#part 2- solve it
#look at first row, figure out if we can fill 

#we know that a number fills in if either of these criteria fails


#part 3- print out solved puzzle
raw_input("Press Enter to continue...")