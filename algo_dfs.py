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
