class Figure:

    allowed_figures = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
    board_num = '12345678'
    board_let = 'ABCDEFGH'

    def checkField(self, field):
        """Check if given field is within board

        Args:
            field (str): Field name (e.g E4)

        Returns:
            [bool]: True or False
        """
        if field[0] in self.board_let and field[1] in self.board_num \
           and len(field) == 2:
            return True
        else:
            return False

    def changeToCoordinates(self, field):
        """
        Change name of Field to coordinates (e.g E4 -> (5,4))

        Args:
            field (str): Field name

        Returns:
            [tuple]: Field coordinates
        """
        coord = (
            self.board_let.index(field[0]) + 1, 
            int(field[1])
            )
        return coord

    def changeToField(self, coordinates):
        """
        Change field coordinates to name (e.g (6,7) -> F7 )

        Args:
            coordinates (tuple): Field coordinates

        Returns:
            [str]: Field name
        """
        field = ''.join([
            self.board_let[coordinates[0]-1], 
            str(coordinates[1])
            ])
        return field


    def listAvailableMoves(self, currentField):
        raise NotImplementedError('Method is not yet implemented!')
        
    def validateMove(self, currentField, moveField):
        raise NotImplementedError('Method is not yet implemented!')

class pawn(Figure):
    
    def __str__(self):
        return 'Pawn'

    def listAvailableMoves(self, currentField):
        ## Change to coordinates
        coord = self.changeToCoordinates(currentField)

        if coord[1] in [1,8]:
            # Pawns start from 2nd line so Field on 1st line is wrong field
            # If pawns reach 8th line they are promoted to figure so they cannot
            # be on 8th line.
            return []
        else:
            ## Determine moves for pawn
            move = (coord[0], coord[1]+1)
            ## Change to Field name
            newField = self.changeToField(move)
            return [newField]

    def validateMove(self, currentField, moveField):
        if moveField in self.listAvailableMoves(currentField):
            return True
        else:
            return False
        

class rook(Figure):
    
    def __str__(self):
        return 'Rook'
    
class knight(Figure):
    
    def __str__(self):
        return 'Knight'
    
class bishop(Figure):
    
    def __str__(self):
        return 'Bishop'
    
class queen(Figure):
    
    def __str__(self):
        return 'Queen'
    
class king(Figure):
    
    def __str__(self):
        return 'King'