import pytest

from moves.figures import Figure, pawn, rook, knight, bishop, queen, king

#### Test class methods

class TestFigureMethods():
    def setup(self):
        self.fig = Figure()

    def test_attributes(self):
        assert self.fig.allowed_figures == \
            ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king'], \
            'Should be "[\'pawn\', \'rook\', \'knight\', \'bishop\', \'queen\', \'king\']"'
        assert self.fig.board_num == '12345678', 'Should be "12345678"'
        assert self.fig.board_let == 'ABCDEFGH', 'Should be "ABCDEFGH"'


    def test_checkField(self):
        assert self.fig.checkField('E5') == True, 'Should be true'
        assert self.fig.checkField('E10') == False, 'Should be false'
        assert self.fig.checkField('A5') == True, 'Should be true'
        assert self.fig.checkField('D5') == True, 'Should be true'
        assert self.fig.checkField('R5') == False, 'Should be false'
        assert self.fig.checkField('S15') == False, 'Should be false'
        assert self.fig.checkField('A8') == True, 'Should be true'
        assert self.fig.checkField('H1') == True, 'Should be true'
            

    def test_transformMethods(self):
        assert self.fig.changeToField(self.fig.changeToCoordinates('E5')) == \
            'E5', 'Should be E5'
        assert self.fig.changeToField(self.fig.changeToCoordinates('A1')) == \
            'A1', 'Should be A1'
        assert self.fig.changeToField(self.fig.changeToCoordinates('H8')) == \
            'H8', 'Should be H8'
        assert self.fig.changeToField(self.fig.changeToCoordinates('G6')) == \
            'G6', 'Should be G6'
        assert self.fig.changeToField(self.fig.changeToCoordinates('C4')) == \
            'C4', 'Should be C4'

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_method_raise_error(self):
        self.fig.listAvailableMoves('E5') 
        self.fig.validateMove('E5','E6')

