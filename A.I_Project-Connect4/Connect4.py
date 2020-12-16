

# This evaluation is based on the location
evaluation_array = [[3, 4,  5,  7,  5, 4, 3],
                    [4, 6,  8, 10,  8, 6, 4],
                    [5, 8, 11, 13, 11, 8, 5],
                    [5, 8, 11, 13, 11, 8, 5],
                    [4, 6,  8, 10,  8, 6, 4],
                    [3, 4,  5,  7,  5, 4, 3]]


YELLOW  = '\033[1;33;40m'
RED    = '\033[1;31;40m'
WHITE   = '\033[1;37;40m'


alpha = -10000
beta = 10000
depth = 6

def evaluation_function(state):
    f = 0
    for row in range(6):
        for column in range(7):
            if state[row][column] == 'R' :
                f += evaluation_array[row][column]
            elif state[row][column] == 'Y':
                f -= evaluation_array[row][column]
    #  print(f)
    #  print('_______________________________')
    return f


def create_state(state, player):
    state_list = []
    for column in range(7):
        if not full_column(state, column):
            state_list.append(put(state, column, player))
    return state_list


def win(state, player):
    player_win = False
    for row in range(6):
        for column in range(7):
            if state[row][column] == player:
                player_win = is_four(state, row, column, player)
            if player_win:
                return True
    return False


# check if the player has four points together
def is_four(state, row, column, player):
    if row >= 3:
        if state[row - 3][column] == player and state[row - 2][column] == player and state[row - 1][column] == player:
            return True
        if column >= 3:
            if state[row - 3][column - 3] == player and state[row - 2][column - 2] == player and state[row - 1][column - 1] == player:
                return True
        if 6 - column >= 3:
            if state[row - 3][column + 3] == player and state[row - 2][column + 2] == player and state[row - 1][column + 1] == player:
                return True
    if 5 - row >= 3:
        if state[row + 3][column] == player and state[row + 2][column] == player and state[row + 1][column] == player:
            return True
        if column >= 3:
            if state[row + 3][column - 3] == player and state[row + 2][column - 2] == player and state[row + 1][column - 1] == player:
                return True
        if 6 - column >= 3:
            if state[row + 3][column + 3] == player and state[row + 2][column + 2] == player and state[row + 1][column + 1] == player:
                return True
    if column >= 3:
        if state[row][column - 3] == player and state[row][column - 2] == player and state[row][column - 1] == player:
            return True
    if 6 - column >= 3:
        if state[row][column + 3] == player and state[row][column + 2] == player and state[row][column + 1] == player:
            return True
    return False


def put(state, column, player):
    state_copy = copy(state)
    for row in reversed(range(6)):
        if state_copy[row][column] == '.':
            state_copy[row][column] = player
            break
    return state_copy


def copy(state):
    s = [[], [], [], [], [], []]
    for i in range(6):
        for j in range(7):
            s[i].append(state[i][j])
    return s


# This method show if the board is full
def full_board(state):
    for column in range(7):
        if not full_column(state, column):
            return False
    return True



def full_column(state, column):
    if state[0][column] == 'Y' or state[0][column] == 'R':
        return True
    else:
        return False


def maximum(x, y):
    if x > y:
        return x
    else:
        return y


def minimum(x, y):
    if x < y:
        return x
    else:
        return y


def print_board(state):
    for i in range(6):
        for j in range(7):
            if state[i][j] == 'Y':
                print(WHITE + '|' + ' ' + YELLOW + state[i][j] + ' ', end= '')
            elif state[i][j] == 'R':
                print(WHITE +'|'+ ' '+ RED  + state[i][j] + ' ', end='')
            elif state[i][j] == '.':
                print(WHITE +'|   ', end = '') 
        
        print('|')
            
    print(WHITE +'_______________________________')

def print_board2(state):
    print(state[0])
    print(state[1])
    print(state[2])
    print(state[3])
    print(state[4])
    print(state[5])

def alpha_beta_search(state, alpha, beta, depth, turn):
    #  print(f'{alpha} <= {beta}')
    #  print_board(state)
    if turn == 'R':
        depth -= 1
        value = -10000
        list_value = []
        list = create_state(state, 'R')
        for s in list:
            min_v = min_value(s, alpha, beta, depth)
            value = maximum(value, min_v)
            list_value.append(min_v)
            if value >= beta:
                break
            alpha = maximum(alpha, value)
        for i in range(len(list)):
            if value == list_value[i]:
                #  print_board(list[i])
                return list[i]
    else:
        depth -= 1
        value = 10000
        list_value = []
        list = create_state(state, 'Y')
        for s in list:
            min_v = max_value(s, alpha, beta, depth)
            value = minimum(value, min_v)
            list_value.append(min_v)
            if value <= alpha:
                break
            alpha = minimum(alpha, value)
        for i in range(len(list)):
            if value == list_value[i]:
                #  print_board(list[i])
                return list[i]
        



def max_value(state, alpha, beta, depth):
    #  print(f'{alpha} <= {beta}')
    #  print_board(state)
    if win(state, 'Y'):
        return -10000
    elif full_board(state):
        return 0
    elif depth == 0:
        return evaluation_function(state)

    depth -= 1
    value = -10000
    list = create_state(state, 'R')
    for s in list:
        value = maximum(value, min_value(s, alpha, beta, depth))
        if value >= beta:
            return value
        alpha = maximum(alpha, value)
    return value


def min_value(state, alpha, beta, depth):
    #  print(f'{alpha} <= {beta}')
    #  print_board(state)
    if win(state, 'R'):
        return 10000
    elif full_board(state):
        return 0
    elif depth == 0:
        return evaluation_function(state)

    depth -= 1
    value = 10000
    list = create_state(state, 'Y')
    for s in list:
        value = minimum(value, max_value(s, alpha, beta, depth))
        if value <= alpha:
            return value
        beta = minimum(beta, value)
    return value


#  max = B, min = Y
current_state = []

for line in open("test1.txt"):
    line=line.strip()
    current_state.append([str(c) for c in line])

# current_state = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
#                  [' ', ' ', ' ', 'Y', ' ', ' ', 'Y'],
#                  [' ', ' ', 'R', 'Y', 'R', 'Y', 'R']]

# print(current_state)
turn  = 'R'

while(True):

    if win(current_state, 'Y'):
        print(YELLOW +'** Yellow won **')
        break
    elif win(current_state, 'R'):
        print(RED +'** RED won **')
        break
    elif full_board(current_state):
        print('The board is full')
        break

    temp1 = alpha_beta_search(current_state, alpha, beta, depth, turn)
    print('best move to '+turn+' player:')
    print_board(temp1)

    if turn == 'R':
        turn = 'Y'
    else:
        turn = 'R'

    current_state = temp1