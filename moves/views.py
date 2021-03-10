from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class Figure:
    def listAvailableMoves(self, currentField):
        raise NotImplementedError('Method is not yet implemented!')
        
    def validateMove(self, currentField, moveField):
        raise NotImplementedError('Method is not yet implemented!')

class pawn(Figure):
    
    def __str__(self):
        return 'Pawn'

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
    def get(self, request, figure, current_field):

        data = {'figure': figure,
                'current_field': current_field
        }

        return Response(data)


class validateMove(APIView):
    def get(self, request, figure, current_field, move_field):
        
        data = {'figure': figure,
                'current_field': current_field,
                'move_field': move_field
        }

        return Response(data)

