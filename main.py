import random

def main():
    random_board = random_state(5, 5)
    render(random_board)


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
        print(line)

if __name__ == "__main__":
    main()