from Ship import Ship
from Player import Player

# Should extend Board
class PlacementBoard(object):
    def __init__(self, x: int, y: int, owner: Player) -> None:
        self.board_array = []
        self.ship_owner_dict = {}
        self.x = x
        self.y = y
        self.orientations = {'h': 'horizontally', 'H': 'horizontally', 'v': 'vertically', 'V': 'vertically'}
        self.owner = owner
        self.initialize_board()

    def print_board(self, placement: bool) -> None:
        if placement:
            print('{}\'s Placement Board'.format(self.owner.name))
        else:
            print('{}\'s Board'.format(self.owner.name))
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
        if not placement:
            print('')

    def initialize_board(self) -> None:
        for row in range(0, self.x):
            current_row = []
            for col in range(0, self.y):
                current_row.append('*')
            self.board_array.append(current_row)

    def update_ship_owner_dict(self, new_ship_owner_dict: dict) -> None:
        self.ship_owner_dict = new_ship_owner_dict

    def shoot_cord(self, cord: list) -> bool:

        try:
            x = int(cord[0])
            y = int(cord[1])

            if x > self.x - 1:
                print('{}, {} is not in bounds of our {} X {} board.'.format(x, y, self.x, self.y))
                return False
            elif y > self.y - 1:
                print('{}, {} is not in bounds of our {} X {} board.'.format(x, y, self.x, self.y))
                return False
            target = self.board_array[x][y]
        except:
            print('{}, {} is not in bounds of our {} X {} board.'.format(x, y, self.x, self.y))
            return False
        if target == '*':
            return True
        elif target == 'X' or target == 'O':
            print('You have already fired at {}, {}.'.format(x, y))
            return False
        else:
            target_id = self.board_array[x][y]
            # this updating needs to happen later
            # self.board_array[x][y] = 'X'
            return True

    def place_ship(self, ship: Ship) -> bool:
        cords = ship.cord
        dir = ship.direction
        hitpoints = int(ship.hitpoints)
        startx = int(cords[0])
        starty = int(cords[1])

        list_of_cords_to_update = []
        list_of_ship_strings_to_update = []
        list_of_overlapping_ships = []

        try:
            if dir == 'v':
                for i in range(startx, startx + hitpoints):
                    if i > (self.x - 1) or starty > (self.y - 1):
                        # hanging off edge!
                        print('Cannot place {} {} at {}, {} because it would end up out of bounds.'.format(ship.name,
                                                                                                           self.orientations[
                                                                                                               dir],
                                                                                                           startx,
                                                                                                           starty))
                        return False
                    elif self.board_array[i][starty] == '*':
                        list_of_cords_to_update.append([i, starty])
                        string_cords = str(i) + ',' + str(starty)
                        string_cords = string_cords.replace(' ', '')
                        list_of_ship_strings_to_update.append(string_cords)
                    else:
                        overlapping_ship = self.board_array[i][starty]
                        list_of_overlapping_ships.append(overlapping_ship)

            elif dir == 'h':
                for i in range(starty, starty + hitpoints):
                    if startx > (self.x - 1) or i > (self.y - 1):
                        # hanging off edge!
                        print('Cannot place {} {} at {}, {} because it would end up out of bounds.'.format(ship.name,
                                                                                                           self.orientations[
                                                                                                               dir],
                                                                                                           startx,
                                                                                                           starty))
                        return False
                    elif self.board_array[startx][i] == '*':
                        list_of_cords_to_update.append([startx, i])
                        string_cords = str(startx) + ',' + str(i)
                        string_cords = string_cords.replace(' ', '')
                        list_of_ship_strings_to_update.append(string_cords)
                    else:
                        overlapping_ship = self.board_array[startx][i]
                        list_of_overlapping_ships.append(overlapping_ship)

            if len(list_of_overlapping_ships) > 0:
                list_of_overlapping_ships.sort()
                list_of_overlapping_ships = list(dict.fromkeys(list_of_overlapping_ships))
                print('Cannot place {} {} at {}, {} because it would overlap with {}'.format(ship.name,
                                                                                              self.orientations[
                                                                                                  dir],
                                                                                              startx,
                                                                                              starty,
                                                                                              list_of_overlapping_ships))
                return False

            for item in list_of_cords_to_update:
                self.update_board(item, ship.name[0])

            for item in list_of_ship_strings_to_update:
                self.ship_owner_dict[item] = ship.owner

            return True
        except:
            return False

    def update_board(self, cords: list, update: str) -> None:
        x = int(cords[0])
        y = int(cords[1])
        #print(f'Adding {update} to[{x}][{y}] on {self.owner.name}\'s PLACEMENT board')
        self.board_array[x][y] = update

    def get_item_at_cord(self, cords: list) -> str:
        x = int(cords[0])
        y = int(cords[1])
        return self.board_array[x][y]