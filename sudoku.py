board = [
[8,7,6,9,0,0,0,0,0],
[0,1,0,0,0,6,0,0,0],
[0,4,0,3,0,5,8,0,0],
[4,0,0,0,0,0,2,1,0],
[0,9,0,5,0,0,0,0,0],
[0,5,0,0,4,0,3,0,6],
[0,2,9,0,0,0,0,0,8],
[0,0,4,6,9,0,1,7,3],
[0,0,0,0,0,1,0,0,4]
]

def print_board (bo):
	for i in range (len(bo)):
		if i % 3 == 0 and i != 0:
			print('---------------------')
		for j in range (len(bo[0])):
			if j % 3 == 0 and j != 0:
				print("|",end = " ")
			if j == len(bo[0]) - 1:
				print(bo[i][j])
			else:
				print(bo[i][j], end = " ")


def find_emty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == 0:
				return i, j   #return position
	return None


def valid (bo,num,pos):
	for i in range(len(bo)):
		# check row
		if num == bo[pos[0]][i] and pos[0] != i:
			return False
		#check colum
		if num == bo[i][pos[1]] and pos[1] != 1:
			return False
	#check box
	box_x = pos[0] // 3
	box_y = pos[1] // 3
	for i in range (box_x * 3, box_x * 3 + 3):
		for j in range (box_y * 3, box_y * 3 + 3):
			if num == bo[i][j] and (i,j) != pos:
				return False
	return True

def solve(bo):
	emty = find_emty(bo)
	if not emty:
		return True
	else:
		row, col = emty
		print(emty)

	for i in range (1,10):
		if valid(bo, i, (row,col)):
			bo[row][col] = i
			print(row, col)
			print('--------------------------')
			print_board(bo)

			if solve(bo):
				return True

			bo[row][col] = 0

	return False

print_board(board)
print('--------------------------')
solve(board)
print_board(board)




