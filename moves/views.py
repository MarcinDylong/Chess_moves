from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from moves.figures import Figure, pawn, rook, knight, bishop, queen, king


class index(View):
    """
    Index view with basics information
    """
    def get(self, request):
        return render(request, 'index.html')


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
                stat=status.HTTP_200_OK if len(data['availableMoves']) != 0 \
                    else status.HTTP_409_CONFLICT
            else:
                data['error'] = 'Field does not exist'
                stat=status.HTTP_409_CONFLICT
            
        else:
           data['error'] = 'Figure does not exist'
           stat = status.HTTP_404_NOT_FOUND

        return Response(data, stat)


class validateMove(APIView):
    """
    Check if move is valid
    """
    def get(self, request, figure, current_field, dest_field):
        """
        Args:
            figure (str): Chess figure (e.g rook)
            current_field (str): Field from chess board (e.g. H3)
            dest_field (str): Destination field from chess board

        Returns:
            [dict]: Information about move with validity check
        """
        ## Case sensivity
        figure = figure.lower()
        current_field = current_field.upper()
        dest_field = dest_field.upper()

        ## Init data
        data = {
            "move": None,
            "figure": figure,
            "error": None,
            "currentField": current_field,
            "destField": dest_field
            }

        ## Check figure
        if figure in Figure.allowed_figures:
            fig = eval(f'{figure}()')

            ## Check current field
            if fig.checkField(current_field):
                availableMoves = fig.listAvailableMoves(current_field)
                if dest_field in availableMoves:
                    stat=status.HTTP_200_OK
                    data['move'] = 'valid'
                else:
                    stat=status.HTTP_409_CONFLICT
                    data['move'] = 'invalid'
            else:
                data['error'] = 'Field does not exist'
                data['move'] = 'invalid'
                stat=status.HTTP_409_CONFLICT
            
        else:
           data['error'] = 'Figure does not exist'
           data['move'] = 'invalid'
           stat = status.HTTP_404_NOT_FOUND

        return Response(data, stat)

