from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

from moves.figures import Figure, pawn, rook, knight, bishop, queen, king



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
        ## Case sensivity
        figure = figure.lower()
        current_field = current_field.upper()


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
           stat = status.HTTP_404_NOT_FOUND

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

