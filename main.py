import random

def main():
    print(random_state(7, 3))


def dead_state(w, h):
    board = []
    for i in range(h):
        board.append([0] * w)
        
    return board

def random_state(w, h):
    state = dead_state(w, h)
    
    for outer in state:
        for inner in range(len(outer)):
            random_number = random.random()
            outer[inner] = 0 if random_number >= 0.5 else 1
    return state
    

if __name__ == "__main__":
    main()