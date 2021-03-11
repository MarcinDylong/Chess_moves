from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class Figure:

    allowed_figures = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
    board_num = '12345678'
    board_let = 'abcdefgh'

    def checkField(self, field):
        """Check if given field is within board

        Args:
            field (str): Field name (e.g E4)

        Returns:
            [bool]: True or False
        """
        if field[0] in self.board_let and field[1] in self.board_num:
            return True
        else:
            return False

    def changeToCoordinates(self, field):
        coord = (
            self.board_let.index(field[0]) + 1, 
            int(field[1])
            )
        return coord

    def changeToField(self, coordinates):
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



class listMoves(APIView):
    """
    Return list of available moves for given figure from given field
    """
    def get(self, request, figure, current_field):
        """
        Args:
            figure (str): Chess figure (e.g rook)
            current_field (str): Field from chess board (e.g. H3)

        Returns:
            [dict]: data about possible moves for figure from current field,
                    in case of error, information what caused it
        """
        ## Init data and status
        data = {
                "availableMoves": [],
                "error": None,
                "figure": figure,
                "currentField": current_field
                }
        
        ## Check figure
        if figure in Figure.allowed_figures:
            fig = eval(f'{figure}()')

            ## Check current field
            if fig.checkField(current_field):
                data['availableMoves'] = fig.listAvailableMoves(current_field)
                stat=status.HTTP_200_OK
            else:
                data['error'] = 'Field does not exist'
                stat=status.HTTP_409_CONFLICT
            
        else:
           data['error'] = 'Figure does not exist'
           stat = status.HTTP_400_BAD_REQUEST

        return Response(data, stat)


class validateMove(APIView):
    def get(self, request, figure, current_field, move_field):
        
        data = {
            "move":"valid",
            "figure": figure,
            "error": None,
            "currentField": current_field,
            "destField": move_field
            }

        return Response(data)

