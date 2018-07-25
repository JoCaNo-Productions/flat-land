class GameException(Exception):
    pass

class DistanceTooLong(GameException):
    pass

class IllegalMove(DistanceTooLong):
    pass

class IllegalAttack(DistanceTooLong):
    pass
