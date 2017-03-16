def largest_connected_component(board):
	largest_count = 0
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == 1:
				board[row][column] = 0
				count = dfs(board, row, column, 1)
				largest_count = max(largest_count, count)
	return largest_count			

def dfs(board, row, column, count):
	neighbors = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
	for neighbor in neighbors:
		x = row + neighbor[0]
		y = column + neighbor[1]
		if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
			continue
		if board[x][y] == 1:
			board[row][column] = 0
			count += 1 
			dfs(board, x, y, count)
	return count		

# TEST					
board = [
			[1, 1, 0, 0],
			[0, 1, 1, 0],
			[0, 0, 1, 0],
			[1, 0, 0, 0],
		]
print(largest_connected_component(board))
###
def largest_connected_component(board):
	largest_count = 0
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == 0:
				continue
			else:
				count = 1
				count += dfs(board, row+1, column)
				count += dfs(board, row-1, column)
				count += dfs(board, row, column+1)
				count += dfs(board, row, column-1)
				count += dfs(board, row+1, column+1)
				count += dfs(board, row-1, column-1)
				count += dfs(board, row+1, column-1)
				count += dfs(board, row-1, column+1)
				largest_count = max(largest_count, count)
	return largest_count			

def dfs(board, row, column):
	if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]):
		return 0
	if board[row][column] == 1:
		board[row][column] = 0
		count += 1
		count += dfs(board, row+1, column)
		count += dfs(board, row-1, column)
		count += dfs(board, row, column+1)
		count += dfs(board, row, column-1)
		count += dfs(board, row+1, column+1)
		count += dfs(board, row-1, column-1)
		count += dfs(board, row+1, column-1)
		count += dfs(board, row-1, column+1)
		return 1	
	else:
		return 0	
					
board = [
			[1, 1, 0, 0],
			[0, 1, 1, 0],
			[0, 0, 1, 0],
			[1, 0, 0, 0],
		]
print(largest_connected_component(board))
