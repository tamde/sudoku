# description of the game is in the README

top = '  A B C    D E F    G H I'
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# print(top)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# solution
# replace the last 9 on the bottom right with a 0 and start the game.
# type "ii9" to quickly test the functionality of determining a winner.
# board = [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

class Sudoku:
    def print_board(self, bo):
        """prints the gameboard"""
        print(top)
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
            print(col[i], end=" ")
            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")


    def user_input(self):
        """takes user input and updates the gameboard"""
        coord_dict = {'a': 0,  'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
        inp = input().lower()
        a = 0
        b = 0
        if inp == 'done':
            if self.verify(board):
                return
            return 
            # if self.verify(board) == True:
            #     return True
            # return self.verify(board)
        try:
            if inp[0] and inp[1] in coord_dict:
                a = coord_dict.get(inp[0])
                b = coord_dict.get(inp[1])
            board[a][b] = int(inp[2])
        except:
            print('invalid input, try again')

    def verify(self, bo):
        """verify if the player's solution is correct"""
        # row verification
        for i in range(9):
            temp = []
            for j in range(9):
                if bo[i][j] not in temp and bo[i][j] in range(1,10):
                    temp.append(bo[i][j])
                else:
                    # print('you FAIL!')
                    return False

        # col verification
        for i in range(9):
            temp = []
            for j in range(9):
                if bo[j][i] not in temp and bo[j][i] in range(1,10):
                    temp.append(bo[j][i])
                else:
                    # print('you FAIL!')
                    return False
        
        # 3x3 verification
        # verifies each 3x3 vertically
        for k in range(0, 9, 3):# need to skip every 3
            box_x = k // 3
            for p in range(0, 9, 3):
                box_y = p // 3
                temp = []
                for i in range(box_x*3, box_x*3 + 3):
                    for j in range(box_y*3, box_y*3 + 3):
                        if bo[i][j] not in temp:
                            temp.append(bo[i][j])
                        else:
                            # print('you FAIL!')
                            return False
        # print('you win!')
        return True
            
if __name__ == '__main__':
    c = Sudoku()
    c.print_board(board)
    while c.verify(board) != True:
        c.user_input()
        c.print_board(board)
    print('you win!')

