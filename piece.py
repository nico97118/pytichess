

class Piece:

    def __init__(self, color):
        self.color = color
        self.name = name

    def is_move_valid(self, origine,destination):
        print("This piece has no move, please report")

    def is_ennemy(self,destination):
        if Game.at(destination) != self.color:
            return True
        else:
            return False

    def is_ally(self,destination):
        if Game.at(destination) == self.color:
            return True
        else:
            return False


class King(Piece):
    def __init__(self,color):
        self.color= color
        self.name = "King"

    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False

        for i in range(-1, 1):
            for j in range(-1, 1):
                if (oc+i, ol+j)==(dc, dl):
                    return True
        return False

class Queen(Piece):
    def __init__(self, color):
        self.color = color
        self.name  = "Queen"


    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False
        if oc-dc == ol-dl: # is Diagonal
            return True
        if oc == dc or ol == dl: # Same Line or col
            return True
        else:
            return False

class Rook(Piece):
    def __init__(self, color):
        self.color = color
        self.name = "Rook"

    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False
        if oc == dc or ol == dl: # Same line or col
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self,color):
        self.color = color
        self.name = "Bishop"

    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False
        if(oc-dc)==(ol-dl): # Same diag
            return True
        else:
            return False

class Knight(Piece):
    def __init__(self, color):
        self.color = color
        self.name = "Knight"

    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False
        if oc-dc == 2 or oc-dc == -2:
            if ol-dl == 1 or ol-dl == -1:
                return True
        elif ol-dl == 2 or ol-dl == -2:
            if oc-dc == 1 or oc-dc == -1:
                return True
        else:
            return False

class Pawn(Piece):
    def __init__(self,color):
        self.color = color
        self.name = "Pawn"
    def is_move_valid(self, origine, destination):
        if origine == destination:
            return False
        oc, ol = origine
        dc, dl = destination
        if dc-oc == 1:
            return True
        elif dc-oc == 1 and (dl-ol== 1 or dl - ol == -1)  and is_ennemy(destination):
            return True
        else:
            return False
