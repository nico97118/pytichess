

class Piece:

    def __init__(self, color):
        self.color = color

    def move(self, origine, destination):
        if is_move_valid(origine,destination):
            #move on the table
        if is_ennemy(destination):
            #remove ennemy

    def is_ennemy(self,destination):
        pass
        #if destination is not same color : return True

class King(Piece):
    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False
        #if (dc,dl) same color : return False

        for i in range(-1, 1):
            for j in range(-1, 1):
                if (oc+i, ol+j)==(dc, dl):
                    return True
        return False

class Queen(Piece):


    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False
        if oc-dc == ol-dl: # is Diagonal
            return True
        if oc == dc || ol == dl: # Same Line or col
            return True
        else
            return False

class Rock(Piece):
    def is_move_valid(self, origine, destination):
        oc, ol = origine
        dc, dl = destination
        if origine == destination:
            return False
        if oc == dc or ol == dl: # Same line or col
            return True
        else
            return False

class Bishop(Piece):
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
