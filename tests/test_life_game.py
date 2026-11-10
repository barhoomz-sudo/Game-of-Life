from life_game import next_board_state

def test_all_dead():
    assert next_board_state([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]) == [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

def test_dead_with_3_neughbors():
    assert next_board_state([
        [0,0,1],
        [0,1,1],
        [0,0,0]
        ]) == [
        [0,1,1],
        [0,1,1],
        [0,0,0]
        ]

def test_1x1_cell():
    assert next_board_state([[1]]) == [[0]]

def test_single_row():
    assert next_board_state([[1,1,1]]) == [[0,1,0]]

def test_single_width():
    assert next_board_state([[1],[1],[1]]) == [[0],[1],[0]]

def test_overpopulation_dies():
    assert next_board_state([
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ]) == [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]

def test_corners_and_edges():
    assert next_board_state([
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]) == [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]

def test_corner_birth():
    assert next_board_state([
        [0,1],
        [1,1]
    ]) == [
        [1,1],
        [1,1]
    ]