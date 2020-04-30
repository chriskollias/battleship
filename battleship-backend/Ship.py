class Ship(object):
    alive = True

    def __init__(self, direction: str, name: str, cord: list, hitpoints: int, owner: str) -> None:
        self.name = name
        self.direction = direction
        self.cord = cord
        self.hitpoints = int(hitpoints)
        self.owner = owner

    def print_ship_stat(self) -> None:
        print(self.name, self.cord, self.hitpoints)

    def check_ship_stat(self) -> None:
        if self.hitpoints == 0:
            self.alive = False

    def decrease_hitpoints(self) -> int:
        self.hitpoints -= 1
        self.check_ship_stat()
        return self.hitpoints
