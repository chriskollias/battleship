from Ship import Ship
from Player import Player

# should extend Board
class ScanningBoard(object):
    def __init__(self, x: int, y: int, owner: Player) -> None:
        self.board_array = []
        self.ship_owner_dict = {}
        self.x = x
        self.y = y
        self.orientations = {'h': 'horizontally', 'H': 'horizontally', 'v': 'vertically', 'V': 'vertically'}
        self.owner = owner
        self.initialize_board()

    def print_board(self) -> None:
        #print('{}\'s Scanning Board'.format(self.owner.name))
        for row in range(0, self.x + 1):
            for col in range(0, self.y + 1):
                if row == 0 and col != 0:
                    print(col - 1, end=' ')
                elif col == 0 and row != 0:
                    print(row - 1, end=' ')
                elif row == 0 and col == 0:
                    print(' ', end=' ')
                elif row != 0 and col != 0:
                    print(self.board_array[row - 1][col - 1], end=' ')
            print('')
        print('')

    def initialize_board(self) -> None:
        for row in range(0, self.x):
            current_row = []
            for col in range(0, self.y):
                current_row.append('*')
            self.board_array.append(current_row)

    def update_ship_owner_dict(self, new_ship_owner_dict: dict) -> None:
        self.ship_owner_dict = new_ship_owner_dict

    def update_board(self, cords: list, update: str) -> None:
        x = int(cords[0])
        y = int(cords[1])
        self.board_array[x][y] = update

    def get_item_at_cord(self, cords: list) -> str:
        x = int(cords[0])
        y = int(cords[1])
        return self.board_array[x][y]