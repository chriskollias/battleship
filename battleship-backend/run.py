import Game

if __name__ == '__main__':
    battleshipgame = Game.BattleShipGame()
    battleshipgame.setup_game()
    player_one = battleshipgame.create_player('Player 1')
    battleshipgame.create_board(battleshipgame.dimx, battleshipgame.dimy, player_one)
    player_two = battleshipgame.create_player('Player 2')
    battleshipgame.create_board(battleshipgame.dimx, battleshipgame.dimy, player_two)
    battleshipgame.play()