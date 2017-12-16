
In PyTum (original: Pu Tum) two people play against each other on a 7x7 game area. One player puts white stones, the other player puts black stones onto the area. Before the start, random fields are blocked by an odd value of stones. After that, the players alternate with their turns. The goal is to have as many stones as possible in a row. It does not matter if the rows are set vertically or horizontally and how many rows. Diagonal lines are not counted. All scored points of the respective lines are summed up. After every field is occupied, the player with higher points is the winner.

How points are calculated:
3 stones in a line: 3 points
4 stones in a line: 10 points
5 stones in a line: 25 points
6 stones in a line: 56 points
7 stones in a line: 119 points

For the console, following inputs are allowed (* is a wildcard for digits):

//Before start and during the game:
r* - starts new round (* is an odd value of the fields to be blocked; *>= 5, *<=13)
q - quits whole program

//Only during the game:
** - set stone on the game area (first * for rows, second * for columns; *>=1, *<=7)
u* - undo moves from the game (* is for the steps to undo; *>0)
h - show this manual/helpfile
