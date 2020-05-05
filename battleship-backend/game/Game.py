from Board import Board
from Player import Player
from Ship import Ship


class BattleShipGame(object):
    def __init__(self) -> None:
        self.current_turn = 0
        self.game_over = False
        self.boat_dict = {}
        self.dimx = 0
        self.dimy = 0
        self.players = []
        self.orientations = {'h': 'horizontally', 'H': 'horizontally', 'v': 'vertically', 'V': 'vertically'}

    def play(self) -> None:
        while not self.game_over:
            self.enter_move(self.players[self.current_turn])

    def shoot(self, cord: list, player: Player) -> bool:
        #result = self.board.shoot_cord(cord)
        #we want to shoot the other player's placement board
        other_player = self.get_other_player(player)

        result = other_player.placement_board.shoot_cord(cord)

        if not result:
            return False
        else:
            target_id = other_player.placement_board.get_item_at_cord(cord)
            if target_id == '*':
                print('Miss')
                player.scanning_board.update_board(cord, 'O')
                other_player.placement_board.update_board(cord, 'O')
                return True
            else:
                hit_player = other_player
                hit_player.hit_ship(target_id)
                player.scanning_board.update_board(cord, 'X')
                hit_player.placement_board.update_board(cord, 'X')
                return True

    def enter_move(self, player: Player) -> None:
        cords_valid = False
        first_time_asking = True
        while not cords_valid:
            if first_time_asking:
                player.scanning_board.print_board()
                player.placement_board.print_board()
                first_time_asking = False
            print('{}, enter the location you want to fire at in the form row, column:'.format(player.name))
            move_cords = self.get_cords_for_firing()
            valid_input = self.verify_valid_cords_for_firing(move_cords)
            if valid_input:
                valid_move = self.shoot(move_cords, player)
                cords_valid = valid_input and valid_move
                if cords_valid:
                    player.scanning_board.print_board()
                    player.placement_board.print_board()
        self.check_victory()
        self.switch_player()

    def verify_valid_cords_for_firing(self, cords: list) -> bool:
        try:
            if len(cords) != 2:
                return False
        except:
            print('{} is not in the form x,y'.format(cords))
            return False
        try:
            x = cords[0]
            x = int(x)
        except:
            print('Row should be an integer. {} is NOT an integer'.format(x))
            return False
        try:
            y = cords[1]
            y = int(y)
        except:
            print('Column should be an integer. {} is NOT an integer'.format(y))
            return False
        return True

    def verify_valid_cords_for_setup(self, cords: list, boat_name: str, dir: str) -> bool:
        try:
            if len(cords) != 2:
                return False
        except:
            print('{} is not in the form x,y'.format(cords))
            return False
        try:
            x = cords[0]
            x = int(x)
        except:
            print('{} is not a valid value for row.\nIt should be an integer between 0 and {}'.format(x,
                                                                                                       self.board.x - 1))
            return False
        try:
            y = cords[1]
            y = int(y)
        except:
            print('{} is not a valid value for column.\nIt should be an integer between 0 and {}'.format(y,
                                                                                                          self.board.y - 1))
            return False
        if x > (self.dimx - 1) or y > (self.dimy - 1):
            print('Cannot place {} {} at {}, {} because it would be out of bounds.'.format(boat_name,
                                                                                           self.orientations[dir], x,
                                                                                           y))
            return False
        elif x < 0 or y < 0:
            print('Cannot place {} {} at {}, {} because it would be out of bounds.'.format(boat_name,
                                                                                           self.orientations[dir],
                                                                                           x,
                                                                                           y))

            return False
        return True

    def check_victory(self) -> None:
        player1 = self.players[0]
        player2 = self.players[1]

        try:
            if player1.list_of_ships == []:
                print('{} won the game!'.format(player2.name))
                self.game_over = True
        except:
            pass
        try:
            if player2.list_of_ships == []:
                print('{} won the game!'.format(player1.name))
                self.game_over = True
        except:
            pass

    def switch_player(self) -> None:
        if self.current_turn == 0:
            self.current_turn = 1
        elif self.current_turn == 1:
            self.current_turn = 0

    def create_board(self, x: int, y: int, player: Player) -> None:
        print('{}\'s Placement Board'.format(player.name))
        player.placement_board = Board(x, y)
        player.placement_board.print_board()
        player.scanning_board =  Board(x, y)
        self.place_ship(player)

    def create_player(self, player_id: str) -> Player:
        if player_id == 'Player 1':
            self.players.append(self.ver_player(player_id))
            return self.players[0]
        elif player_id == 'Player 2':
            self.players.append(self.ver_player(player_id))
            return self.players[1]

    def ver_player(self, player_id: str) -> str:
        playerone_ver = False
        while not playerone_ver:
            print('{} please enter your name:'.format(player_id))
            p1_name = input()
            if player_id == 'Player 2':
                if p1_name == self.players[0].name:
                    playerone_ver = False
                    print('Someone is already using {} for their name.\nPlease choose another name.'.format(p1_name))
                else:
                    playerone_ver = True
            else:
                playerone_ver = True
        return Player(p1_name)

    def get_cords_for_firing(self) -> list:
        cords = input()

        try:
            cords_list = cords.split(',')
            if len(cords_list) != 2:
                print('{} is not a valid location.\nEnter the firing location in the form row, column'.format(cords))
                return []
            x = cords.split(',')[0]
            y = cords.split(',')[1]
            return [x, y]
        except:
            print('{} is not a valid location.\nEnter the firing location in the form row, column'.format(cords))
            return []

    def get_cords(self) -> list:
        cords = input()
        try:

            cords_list = cords.split(',')
            if len(cords_list) != 2:
                print('{} is not in the form x,y'.format(cords))
                return []

            x = cords.split(',')[0]
            y = cords.split(',')[1]
            return [x, y]
        except:
            print('{} is not in the form x,y'.format(cords))
            return []

    def setup_game(self) -> None:
        try:
            # hardcoding to 10 for now
            self.dimx = 10
            self.dimy = 10
            #inputs = ['Patrol 2', 'Submarine 3', 'Destroyer 4', 'Battleship 5']
            inputs = ['Patrol 2']
            for line in inputs:
                boat_name = line.split(' ')[0]
                boat_hp = line.split(' ')[1]
                boat_hp = boat_hp.replace('\n', '')
                boat_hp = boat_hp.strip()
                self.boat_dict[boat_name] = boat_hp
        except:
            print('Error: Could not read config file')

    def place_ship(self, player: Player) -> None:
        for boat in self.boat_dict:
            boat_placed = False
            while not boat_placed:
                orientation_placed = False
                placement_cords_valid = False
                while orientation_placed is False or placement_cords_valid is False:

                    print(player.name,
                          'enter horizontal or vertical for the orientation of {} which is {} long:'.format(boat,
                                                                                                            self.boat_dict[
                                                                                                                boat]))
                    dir = input()
                    if dir[0] == 'h' or dir[0] == 'H':
                        result = self.verify_orientation(dir)
                        if result:
                            dir_two = 'h'
                            orientation_placed = True
                        else:
                            print('{} does not represent an Orientation'.format(dir))
                    elif dir[0] == 'v' or dir[0] == 'V':
                        result = self.verify_orientation(dir)
                        if result:
                            dir_two = 'v'
                            orientation_placed = True
                        else:
                            print('{} does not represent an Orientation'.format(dir))
                    else:
                        print('{} does not represent an Orientation'.format(dir))
                        orientation_placed = False

                    if orientation_placed:
                        print('{}, enter the starting position for your {} ship ,which is {} long, in the form row, column:'.format(player.name, boat, self.boat_dict[boat]))
                        cords = self.get_cords()
                        placement_cords_valid = self.verify_valid_cords_for_setup(cords, boat, dir_two)

                new_ship = Ship(direction=dir_two, cord=cords, name=boat, hitpoints=self.boat_dict[boat],
                                owner=player.name)
                try:
#                    placement_successful = self.board.place_ship(new_ship)
                    placement_successful = player.placement_board.place_ship(new_ship)
                    if placement_successful:
                        player.add_ship(new_ship)
                    boat_placed = placement_successful
                except Exception as e:
                    print('Error while placing boat', e)
                    pass

    def verify_orientation(self, dir: str) -> bool:
        try:
            dir = dir.lower()
            if dir in 'vertical' or dir in 'horizontal':
                return True
            else:
                return False
        except:
            return False

    def get_player_by_name(self, name: str) -> Player:
        if self.players[0].name == name:
            return self.players[0]
        elif self.players[1].name == name:
            return self.players[1]

    def get_other_player(self, current_player: Player) -> Player:
        if current_player == self.players[0]:
            return self.players[1]
        else:
            return self.players[0]