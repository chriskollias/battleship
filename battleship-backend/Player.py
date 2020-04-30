from Ship import Ship
from Board import Board

class Player(object):
    def __init__(self, name:str) -> None:
        self.name = name
        self.list_of_ships = []
        self.ship_dict = {}
        self.scanning_board = None
        self.placement_board = None

    def add_ship(self, ship: Ship) -> None:
        self.list_of_ships.append(ship)
        self.ship_dict[ship.name[0]] = ship
        #self.placement_board.place_ship(ship)
        self.placement_board.print_board()

    def remove_ship(self, ship:Ship) -> None:
        self.list_of_ships.remove(ship)

    def hit_ship(self, target_id:str) -> None:
        hitpoints = self.ship_dict[target_id].decrease_hitpoints()

        if hitpoints >= 0:
            print('You hit {}\'s {}!'.format(self.ship_dict[target_id].owner, self.ship_dict[target_id].name))
        if hitpoints == 0:
            print('You destroyed {}\'s {}'.format(self.ship_dict[target_id].owner, self.ship_dict[target_id].name))

        if not self.ship_dict[target_id].alive:
            self.remove_ship(self.ship_dict[target_id])

    def check_victory(self) -> bool:
        length = len(self.list_of_ships)
        if length == 0:
            return True
        else:
            return False


