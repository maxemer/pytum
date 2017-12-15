"""
PyTum Game in Console and Functions
from EPR-Job No.5
"""
from random import randint
from os import name as os_name, system
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

class Field():
    """class: field"""
    def __init__(self, col = 0, row = 0, state = 'em', turn = 0):
        """constructor"""
        self.col = col
        self.row = row
        self.state = state
        self.turn =  turn
    def get_col(self):
        """returns column as integer"""
        return self.col
    def get_row(self):
        """returns row as integer"""
        return self.row
    def get_state(self):
        """returns state as string (em := empty, bl := blocked,
        p1 := player1/black, p2 := player2/white)"""
        return self.state
    def get_turn(self):
        """returns turn as integer"""
        return self.turn
    def set_state(self, new_state, turn):
        """set a new state of the field"""
        self.state = new_state
        self.turn = turn

def generate_area(cols, rows):
    """generate a new area for the game
    given by columns and rows as integer"""
    area = []
    col = 1
    row = 1
    while row <= rows:
        while col <= cols:
            area.append(Field(col, row))
            col += 1
        row += 1
        col = 1
    return area

def console_clear():
    """clears the console output based on the os.name"""
    if os_name == 'nt':
        system('cls')
    elif os_name == 'Darwin':
        system('clear')
    else:
        print('\n' * 99)
    print('\n')

def console_output(area):
    """console output of the area of fields"""
    cur_row = 1
    cout = '⌈ 1 2 3 4 5 6 7 ⌉\n' + str(cur_row) + ' '
    # run through all fields in the area
    for field in area:
        if cur_row != field.get_row():
            cout += str(cur_row) + '\n' + str(field.get_row()) + ' '
            cur_row = field.get_row()
        if 'p1' == field.get_state():
            cout += 'B '
        elif 'p2' == field.get_state():
            cout += 'W '
        elif 'bl' == field.get_state():
            cout += 'X '
        else:
            cout += '  '
    cout += str(cur_row) + '\n⌊ 1 2 3 4 5 6 7 ⌋'
    print(cout)
    
def main():
    """Main-Program for the Game"""

    def block_fields(rand = -1):
        """blocks a random count of fields
        (between 5 and 13 and returns it)
        of random positions in the area"""
        if rand == -1:
            while True:
                rand = randint(5, 13)
                # when value is odd, break generating
                if rand % 2:
                    break
                # when value is eval, continue generating
                else:
                    continue
        c = 0
        while c < rand:
            # when random field is empty, increases counter
            if change_state(randint(1, cols), randint(1, rows), 'bl'):
                c += 1
        return rand

    def change_state(col, row, new_state, turn = 0):
        """change state by column and row"""
        ok = False
        # run through all fields in the area
        for field in area:
            # when found specific field
            if field.get_col() == col and field.get_row() == row:
                # when field is empty, set new state and break the loop
                if field.get_state() == 'em':
                    ok = True
                    field.set_state(new_state, turn)
                    break
        return ok

    def calculate_points(player):
        """returns the total points of a player"""
        def stones_to_points(s):
            """returns points by the number of given stones"""
            points = 0
            if s >= 7:
                points += 119
            elif s == 6:
                points += 56
            elif s == 5:
                points += 25
            elif s == 4:
                points += 10
            elif s == 3:
                points += 3
            return points

        # start values
        col = 1
        row = 1
        points = 0
        results = []

        # run through all fields in the area
        for field in area:
            # when field is occupied by player, append it to 'results'
            if field.get_state() == player:
                results.append(field)

        # run through all columns
        while col <= cols:
            row_list = []
            stones = 1
            # run through all results
            for res in results:
                # when current field matches field from 'results',
                # append row to 'row_list'
                if res.get_col() == col:
                    row_list.append(res.get_row())
            c = 0
            # run through 'row_list
            while c < len(row_list):
                if c > 0:
                    # when row is next to the another row,
                    # increase 'stones'
                    if (row_list[c] - row_list[c - 1]) == 1:
                        stones += 1
                c += 1
            # assign points by stones
            points += stones_to_points(stones)
            col += 1

        # run through all rows
        while row <= rows:
            col_list = []
            stones = 1
            # run through all results
            for res in results:
                # when current field matches field from 'results',
                # append column to 'col_list'
                if res.get_row() == row:
                    col_list.append(res.get_col())
            c = 0
            # run through col_list'
            while c < len(col_list):
                if c > 0:
                    # when column is next to the another column,
                    # increase 'stones'
                    if (col_list[c] - col_list[c - 1]) == 1:
                        stones += 1
                c += 1
            # assign points by stones
            points += stones_to_points(stones)
            row += 1

        return points

    def help():
        """prints a help text / manual"""
        with open('readme.txt', 'r') as helpfile:
            data = helpfile.read()
            print(data)

    def undo(step, turn):
        """undoes the states of the area given by turns"""
        # until all seps are gone
        while step > 0:
            # run through all fields in the area
            for field in area:
                # when field found, reset/decrease values
                if field.get_turn() == turn:
                    field.set_state('em', 0)
                    step -= 1
                    turn -= 1

    # start values
    game = True
    cols = 7
    rows = 7
    fields_to_block = -1

    # game loop
    while game:
        # start values
        area = generate_area(cols, rows)
        cur_player = 'p1'
        empty_fields = cols * rows
        turn = 1
        round = True

        help()
        cin = input('--> ').lower()

        # decrease 'empty_fields'-var by blocked fields
        empty_fields -= block_fields(fields_to_block)

        # round loop
        while round:
            print('\n')
            console_output(area)
            print('\n')
            #print('points player 1:', calculate_points('p1'))
            #print('points player 2:', calculate_points('p2'))
            #print(empty_fields)
            #print('Turn:', turn)

            # test-print the objects
            """for field in area:
                print('r:', field.get_row(), ',c:', field.get_col(), \
                ',s:', field.get_state(), ',t:', field.get_turn())"""

            # when game-area is not full
            if empty_fields > 0:
                # when current player is p1
                if cur_player == 'p1':
                    print('turn for black')
                # when current player is p2
                else:
                    print('turn for white')

                cin = input('--> ').lower()
                console_clear()

                # when input is not empty
                if len(cin) > 0:
                    # when input is digit
                    if cin.isdigit():
                        # when input length is not valid, print error and continue
                        if len(cin) > 2 or len(cin) < 2:
                            print('please enter from 1 to 2 characters!')
                            continue
                        # when input length is valid
                        else:
                            # when inputs are not valid to the game columns and rows,
                            # print error and continue
                            if int(cin[0]) > rows or int(cin[1]) > cols \
                            or int(cin[0]) < 1 or int(cin[1]) < 1:
                                print('your inputs are out of range!')
                                continue
                            # when inputs are valid
                            else:
                                # when field is not empty, print error and continue
                                if not change_state(int(cin[1]), int(cin[0]), cur_player, turn):
                                    print('please choose an empty field!')
                                    continue
                                # when field is empty, decreases 'empty_fields'-var
                                else:
                                    empty_fields -= 1
                                    turn += 1
                    # when input is not full digit
                    else:
                        # when input length is higher than 1, start 'undo'
                        if len(cin) > 1:
                            # when input contains an 'r' and digits after that
                            if cin.find('r') == 0 \
                            and cin.replace('r', '').isdigit():
                                block_inp = int(cin.replace('r', ''))
                                # when value is in interval 5, 13
                                if block_inp in [5, 7, 9, 11, 13]:
                                    fields_to_block = block_inp
                                    empty_fields = 0
                                else:
                                    print('choose an odd value between 5 and 13!')
                            # when input contains an 'u' and digits after that
                            elif cin.find('u') == 0 \
                            and cin.replace('u', '').isdigit():
                                steps = int(cin.replace('u', ''))
                                if steps > 0:
                                    if steps <= turn - 1:
                                        undo(steps, turn - 1)
                                        turn -= steps
                                    else:
                                        print('too many steps to undo!')
                                else:
                                    print('please type a '
                                          'value over 0 to undo!')
                            # ...when not
                            else:
                                print('unknown statement. '
                                      'please check out the help (h)!')
                            continue
                        # when input length is 1
                        else:
                            # when input contains an 'c'
                            """if cin.find('c') == 0:
                                print('computer-mode is not implemented yet! :(')
                                continue"""
                            # when input contains an 'h'
                            if cin.find('h') == 0:
                                help()
                                continue
                            # when input contains an 'q'
                            elif cin.find('q') == 0:
                                game = False
                                break
                            # when input is not valid
                            else:
                                print('unknown statement. '
                                      'please check out the helpfile (h)!')
                            # when input contains an 'r'
                            """elif cin.find('r') == 0:
                                empty_fields = 0"""
                # when input is empty
                else:
                    print('please make an input!')
                    continue

                # switch player
                if cur_player != 'p1':
                    cur_player = 'p1'
                else:
                    cur_player = 'p2'

            # when game-area is full
            else:
                round = False
                points_p1 = calculate_points('p1')
                points_p2 = calculate_points('p2')

                console_clear()
                print('points for black:', points_p1)
                print('points for white:', points_p2)

                # when player1 has more points than player2
                if points_p1 > points_p2:
                    print('the winner is black!')
                # when player2 has more points than player1
                elif points_p2 > points_p1:
                    print('the winner is white!')
                # when points are equal
                else:
                    print('points are equal. game is undecided!')

if __name__ == '__main__':
    main()