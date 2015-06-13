#!/usr/bin/python
import sys
import os
#part 1- read in a sudoku puzzle
#formatted in 9 lines with a + as a blank

dir = os.path.dirname(__file__)
sudokopuzzlepath = os.path.join(dir, 'sudokopuzzle1.txt')

Matrix = [[0 for x in range(9)] for x in range(9)]

blanks =[]


with open(sudokopuzzlepath) as f:
	row_counter=0
	blank_counter=0
	for line in f:
		column_counter=0
		for character in line:
			if character == '$':
				blank_counter+=1
				#add list to a blank
				blanks.append((row_counter,column_counter))
			if column_counter < 9:
				Matrix[row_counter][column_counter]=character
			column_counter+=1
		row_counter+=1

print 'these are blanks', blanks

print 'Matrix[0][2]', Matrix[0][2]
#print Matrix
print blank_counter,' blanks'
i=0
while i < 9:
	print Matrix[i]
	i+=1

#write a method to check for valid row
def validrow():
	return true
#takes in matrix [][]
#contains no repeats

#write a method to check for valid column
def validcolumn():
	return true
#takes in matrix [][]


#write a method to check for valid cube
def validcube():
	return true
#takes in matrix [][]
#0-2,0-2
#0-2,3-5
#0-2,6-8

#take in 
def rowlist(row,column):
#calc the row for that blank entry
#find the values for the rows
	i=0
	while i < 9:
		if Matrix[row][i] != '$':
			test=int((Matrix[row][i]))
			if test in numbers:
				numbers.remove(test)
		i+=1
#	return true
	
def columnlist(row,column):
	i=0
	while i < 9:
		if Matrix[i][column] != '$':
			test= int(Matrix[i][column])
			if test in numbers:
				numbers.remove(test)
		i+=1
#	return true
	
def cubelist(row,column):
#section 1
	if int(row) <= 2:
#if in the top 3 rows
		if int(column) <=2:
#			print 'section 1'
#if in the top left section, row 0-2, col 0-2
			i=0
			j=0
			while i <=2:
				while j<=2:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1
#if in the top middle section, row 0-2, col 3-5
		if int(column)>2 and int(column)<=5:
#			print 'section 2'
			i=0
			j=3
			while i <=2:
				while j<6:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1		
#in the top right section, row 0-2, col, 6-8
		if int(column)>5:
#			print 'section 3'
			i=0
			j=6
			while i <3:
				while j<9:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1
#middle left section, rows 3-5, col 0-2
	if int(row) > 2 and int(row)<=5:
		if int(column) <=2:
#			print 'section 4'
			i=3
			j=0
			while i <6:
				while j<3:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1
				#middle, middle, 3,4,5 for both
		if int(column)>2 and int(column)<=5:
#			print 'section 5'
			i=3
			j=3
			while i <6:
				while j<6:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1	
#middle right, row 3-5, col 6-8				
		if int(column)>5:
#			print 'section 6'
			i=2
			j=6
			while i <6:
				while j<9:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1
#section3, bottom left
	if int(row) > 5:
		if int(column) <=2:
#			print 'section 7'
			i=6
			j=0
			while i <9:
				while j<3:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1
				#bottom middle, row 6-8, col 3-5
		if int(column)>2 and int(column)<=5:
#			print 'section 8'
			i=6
			j=3
			while i <9:
				while j<6:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1		
				#bottom right
		if int(column)>5:
#			print 'section 9'
			i=6
			j=6
			while i <9:
				while j<9:
					if Matrix[i][j] != '$':
						test= int(Matrix[i][j])
						if test in numbers:
							numbers.remove(test)
					j+=1
				i+=1

def match(row,col,value):
	print 'match'
	#this is kind of difficult
	temp_val=(row,col)
	blanks.remove(temp)
	Matrix[row][col]=value
	#delete from list of blanks
	#replace section in matrix with new value

def rowcheck(row,value):
	print 'thing'
	
def colcheck(col,value):
	print 'thing'
def cubecheck(row,col,value):
	print 'thing'
	
#how do i figure out the section of the cube
	
#part 2- solve it
#look at first row, are there any blanks, if yes:
#loop from 1 to 9, if more than 1 fits
#call is valid on a single cell
#if valid on more than 1 entry, fails

blank_num=0
#while there are blanks
while len(blanks)>0:
	blank_num=0
	while blank_num<len(blanks):
		numbers=list(xrange(1,10))
	#i need to access the row of the matrix
		temp=blanks[blank_num]
		rowlist((temp[0]),(temp[1]))
		columnlist((temp[0]),(temp[1]))
		cubelist((temp[0]),(temp[1]))
#		print 'numbers modified',numbers
		#shortcut-only one number fits

		if len(numbers)==1:
			print 'yay'
			match((temp[0]),(temp[1]),(numbers[0]))
			#function when we have a match
###rest of algorithm- this is where I stopped for the night
		while len(numbers)>1:
			i=0
			while i < len(numbers):
				temp_numb=numbers[i]
				j=0
				while j < 9:
					if temp_numb ==Matrix[(temp[0])][j]:
						test=int(Matrix[(temp[0])][j])
						numbers.remove(test)
			while i < len(numbers):
				temp_numb=numbers[i]
				j=0
				while j < 9:
					if temp_numb ==Matrix[j][(temp[1])]:
						test=int(Matrix[j][(temp[1])])
						numbers.remove(test)
				#row,column
				#does numbers[i] exist in row
				
				#does numbers[i] exist in column
				
				#does numbers[i] exist in cube
							
			#iterate over these numbers
			#does number fit in other spaces in row
			#does number fit in other spaces in column
			#does number fit in other spaces in cube
			#if number only fits in those
			#check if there are legal spaces for the other numbers
		print 'length of blanks',len(blanks)
		blank_num+=1
		
	i=0
	while i < 9:
		print Matrix[i]
		i+=1
	
#	look at blank 1
i=0
while i < 9:
	print Matrix[i]
	i+=1
		
print 'length of blanks',len(blanks)

#we know that a number fills in if either of these criteria fails


#part 3- print out solved puzzle
raw_input("Press Enter to continue...")
