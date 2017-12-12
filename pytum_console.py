"""
PyTum Functions
from EPR-Job No.5
"""
from random import randint
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

#dic = {(1, 1): 'em', (1, 2): 'em', (1, 3): 'em', (1, 4): 'em', (1, 5): 'em', (1, 6): 'em', (1, 7): 'em', (2, 1): 'em', (2, 2): 'em', (2, 3): 'em', (2, 4): 'em', (2, 5): 'em', (2, 6): 'em', (2, 7): 'em', (3, 1): 'em', (3, 2): 'em', (3, 3): 'em', (3, 4): 'em', (3, 5): 'em', (3, 6): 'em', (3, 7): 'em', (4, 1): 'em', (4, 2): 'em', (4, 3): 'em', (4, 4): 'em', (4, 5): 'em', (4, 6): 'em', (4, 7): 'em', (5, 1): 'em', (5, 2): 'em', (5, 3): 'em', (5, 4): 'em', (5, 5): 'em', (5, 6): 'em', (5, 7): 'em', (6, 1): 'em', (6, 2): 'em', (6, 3): 'em', (6, 4): 'em', (6, 5): 'em', (6, 6): 'em', (6, 7): 'em', (7, 1): 'em', (7, 2): 'em', (7, 3): 'em', (7, 4): 'em', (7, 5): 'em', (7, 6): 'em', (7, 7): 'em'}

class Field():
    """Class Field"""
    def __init__(self, col = 0, row = 0, state = 'em'):
        self.col = col
        self.row = row
        self.state = state
    def get_col(self):
        return self.col
    def get_row(self):
        return self.row
    def get_state(self):
        return self.state
    def set_state(self, new_state):
        self.state = new_state

def generate_area(cols, rows):
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
    cur_row = 1
    cout = '⌈ 1 2 3 4 5 6 7 ⌉\n' + str(cur_row) + ' '

    #run through all fields in the area
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
        ok = False
        for field in area:
            if field.get_col() == col and field.get_row() == row:
                if field.get_state() == 'em':
                    ok = True
                    field.set_state(new_state)
                    break
        return ok

    def block_random_fields():
        while True:
            rand = randint(5, 13)
            #print(rand)
            if rand % 2:
                break
            else:
                continue
        c = 0
        while c < rand:
            if change_state(randint(1, cols), randint(1, rows), 'bl'):
                c += 1
        return rand

    cols = 7
    rows = 7
    area = generate_area(cols, rows)
    cur_player = 'p1'
    empty_fields = cols * rows

    """# test-print the objects
    for field in area:
        print(field.get_row(), field.get_col(), field.get_state())"""

    empty_fields -= block_random_fields()

    while True:
        console_output(area)
        #print(empty_fields)

        if empty_fields > 0:
            cin = input('--> ')
            if len(cin) > 2 or len(cin) < 1:
                print('please enter from 1 to 2 characters!')
                continue
            else:
                if int(cin[0]) > rows or int(cin[1]) > cols:
                    print('your inputs are out of range!')
                    continue
                else:
                    if not change_state(int(cin[1]), int(cin[0]), cur_player):
                        print('please choose an empty field!')
                        continue
                    else:
                        empty_fields -= 1

            # switch player
            if cur_player != 'p1':
                cur_player = 'p1'
            else:
                cur_player = 'p2'
        else:
            cur_player = 'p1'

if __name__ == '__main__':
    main()