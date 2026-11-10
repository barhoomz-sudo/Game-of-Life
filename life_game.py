import random
import time

def main():
    random_board = random_state(20, 20)
    render(random_board)
    print()
    while True:
        random_board = next_board_state(random_board)
        render(random_board)
        time.sleep(0.5)

def dead_state(w, h):
    board = []
    for _ in range(h):
        board.append([0] * w)
        
    return board

def random_state(w, h):
    state = dead_state(w, h)
    
    for outer in state:
        for inner in range(len(outer)):
            random_number = random.random()
            outer[inner] = 0 if random_number >= 0.5 else 1
    return state

def render(board):
    for row in board:
        line = str(row).replace("[", "").replace("]", "").replace(",", "").replace(" ", "").replace("1","🟦").replace("0", "🟥")
        print("|",line,"|",sep="")

def next_board_state(board):
    h = len(board)
    w = len(board[0])

    new_state = dead_state(w, h)
    for row in range(0, h):
        for col in range(0, w):
            current_cell = board[row][col]
            live_neighbors = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:

                    if dr == 0 and dc == 0:
                        continue

                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < h and 0 <= nc < w:
                        live_neighbors += board[nr][nc]

                    if current_cell == 1 and (live_neighbors <= 1 or live_neighbors > 3):
                        new_state[row][col] = 0
                    elif current_cell == 1 and (live_neighbors == 2 or live_neighbors == 3):
                        new_state[row][col] = 1
                    elif current_cell == 0 and live_neighbors == 3:
                        new_state[row][col] = 1
                    else:
                        new_state[row][col] = 0
    return new_state

                    
if __name__ == "__main__":
    main()