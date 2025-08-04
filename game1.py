import numpy as np
import random
import asyncio

from moving import block_lr, set_global_var

class block_stack:
    def __init__(self):
        self.block_1 = np.array([[1, 1, 1], [0, 1, 0], [1, 1, 1]], dtype='uint8')
        self.block_2 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype='uint8')
        self.board = np.zeros((9, 9), dtype='uint8')
    
    def get_block(self):
        block = [self.block_1, self.block_2]
        return block[random.randint(0, 1)]
    

def get_1step_fall(rb_row, rb_col, lt_row, lt_col, block, input_board):
    # input_board equals to previous board
    board = input_board.copy()
    # print(f'Here Coodinate rb: ({rb_col}, {rb_row})')
    for i in range(lt_col, rb_col + 1):
        for j in range(lt_row,  rb_row + 1):
            if block[j - lt_row][i - lt_col] and board[j][i]:
                return True, input_board    # i_b useless
            
    for i in range(lt_col, rb_col + 1):
        for j in range(lt_row,  rb_row + 1):
            if block[j - lt_row][i - lt_col]:
                board[j][i] = 1
    return False, board


def get_coord(rb_row, rb_col):
    return rb_row - 2, rb_col - 2


async def stay():
    await asyncio.sleep(2)


async def main():
    game = block_stack()
    # For the game running
    while True:
        block = game.get_block()
        # init coodinate
        rb_row, rb_col = 2, random.randint(2, 8)

        # For one block running <-- Now
        while True:
            lt_row, lt_col = get_coord(rb_row, rb_col)
            collision, save_board = get_1step_fall(rb_row, rb_col, lt_row, lt_col, block, game.board)

            task_move = asyncio.create_task(block_lr())
            task_stay = asyncio.create_task(stay())


            # condition
            if collision:
                print(f'Collision: Coordinate rb: ({rb_col}, {rb_row})')
                game.board = last_vaild_board
                print(last_vaild_board)
                break

            # each time update the last_vaild
            last_vaild_board = save_board.copy()
            print(last_vaild_board)
            print('\n-------------------------------------------------------------------------\n')

            await task_stay
            await task_move
            set_global_var(False)

            rb_row += 1

            if rb_row == 9:
                game.board = save_board
                break

        print('\n')
        print('Final board:')
        print(game.board)
        break
        

asyncio.run(main())