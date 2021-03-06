#!/usr/bin/python

"""
Brute force sudoku solver.  Found Online.
Baseline of sudoku challenge
"""

import sys

# 060900100308200000009006052400000005027080340500000008950700200000002607002004030
# 012345678901234567890123456789012345678901234567890123456789012345678901234567890
# 0         1         2         3         4         5         6         7         8
# s        s        s        s        s        s        s        s        s
#                            bbb      bbb      bb*
#                                              rr*rrrrrr
#   c        c        c        c        c        *        c        c        c
#   2        11       20       29       38       47       56       65       74


def same_row(i, j):
	return (i // 9 == j // 9)
def same_col(i, j):
	return (i - j) % 9 == 0
def same_block(i, j):
	return (i // 27 == j // 27 and i % 9 // 3 == j % 9 // 3)


def r(a):
	global tickle
	tickle += 1
	i = a.find('0')
	if i == -1:
		print("number of recursive calls: " + str(tickle))
		sys.exit(a)
	excluded_numbers = set()
	for j in range(81):
		if same_row(i, j) or same_col(i, j) or same_block(i, j):
			excluded_numbers.add(a[j])
	for m in '123456789':
		if m not in excluded_numbers:
			r(a[:i] + m + a[i + 1:])
		print("returning None. i is: " + str(i) + " j is: " + str(j) + " Excluded Numbers is: " + repr(sorted(list(excluded_numbers))))
	#print(a)

if __name__ == '__main__':
	tickle = 0
	r('060900100308200000009006052400000005027080340500000008950700200000002607002004030')
