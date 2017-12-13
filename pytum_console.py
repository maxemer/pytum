"""
PyTum Game in Console and Functions
from EPR-Job No.5
"""
from random import randint
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

class Field():
    """class: field"""
    def __init__(self, col = 0, row = 0, state = 'em'):
        """constructor"""
        self.col = col
        self.row = row
        self.state = state
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
    def set_state(self, new_state):
        """set a new state of the field"""
        self.state = new_state

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
            cout += '- '
    cout += str(cur_row) + '\n⌊ 1 2 3 4 5 6 7 ⌋'
    print(cout)
    
def main():
    """Main-Program for the Game"""

    def change_state(col, row, new_state):
        """change state by column and row"""
        ok = False
        # run through all fields in the area
        for field in area:
            # when found specific field
            if field.get_col() == col and field.get_row() == row:
                # when field is empty, set new state and break the loop
                if field.get_state() == 'em':
                    ok = True
                    field.set_state(new_state)
                    break
        return ok

    def block_random_fields():
        """blocks a random count of fields
        (between 5 and 13 and returns it)
        of random positions in the area"""
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

    # start values
    cols = 7
    rows = 7
    area = generate_area(cols, rows)
    cur_player = 'p1'
    empty_fields = cols * rows

    """# test-print the objects
    for field in area:
        print(field.get_row(), field.get_col(), field.get_state())"""

    # decrease 'empty_fields'-var by blocked fields
    empty_fields -= block_random_fields()

    # round loop
    while True:
        console_output(area)
        #print(empty_fields)

        # when game-area is not full
        if empty_fields > 0:
            cin = input('--> ')
            # when input length is not valid, print error and continue
            if len(cin) > 2 or len(cin) < 1:
                print('please enter from 1 to 2 characters!')
                continue
            # when input length is valid
            else:
                # when inputs are not valid to the game columns and rows,
                # print error and continue
                if int(cin[0]) > rows or int(cin[1]) > cols:
                    print('your inputs are out of range!')
                    continue
                # when inputs are valid
                else:
                    # when field is not empty, print error and continue
                    if not change_state(int(cin[1]), int(cin[0]), cur_player):
                        print('please choose an empty field!')
                        continue
                    # when field is empty, decreases 'empty_fields'-var
                    else:
                        empty_fields -= 1

            # switch player
            if cur_player != 'p1':
                cur_player = 'p1'
            else:
                cur_player = 'p2'
        # when game-area is full
        else:
            cur_player = 'p1'

if __name__ == '__main__':
    main()