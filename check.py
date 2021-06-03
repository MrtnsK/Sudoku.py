import numpy as np
import re

def check_valid(grid):
	for i in range(0,8):
		for j in range(0,8):
			if grid[i][j] != 0 and check_square(grid[i][j], i, j, grid) is False\
				and check_vert(grid[i][j], i, j, grid) is False:
				return False
	return True


def check_vert(nb, pos_x, pos_y, grid):
	for elem in grid[pos_x]:
		if elem == nb:
			return False
	i = 0
	while i < 9:
		if grid[i][pos_y] == nb:
			return False
		i += 1
	return True

def check_square(nb, pos_x, pos_y, grid):
	x = 0
	y = 0
	while x < 3:
		while y < 3:
			tmp_x = (pos_x - (pos_x % 3) + x)
			tmp_y = (pos_y - (pos_y % 3) + y)
			if  np.logical_and(tmp_x != pos_x, tmp_y != pos_y) and grid[tmp_x][tmp_y] == nb:
				return False
			y +=1
		y = 0
		x += 1
	return True

def fill_grid(grid, inpt):
	inpt = re.sub(r'[ \t\n]','',inpt)
	if len(inpt) != 81 or inpt.isdigit() is False:
		return -1
	x = 0
	for i in range(0,9):
		for j in range(0,9):
			grid[i][j] = int(inpt[x])
			x += 1
	return 0

def layout(grid):
	tmp = ""
	for i in range(0,9):
		for j in range(0,9):
			tmp += str(int(grid[i][j])) + (' ' if j != 8 else '\n')
	return tmp
