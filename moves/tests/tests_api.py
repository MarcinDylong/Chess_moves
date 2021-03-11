from rest_framework.test import APITestCase

#### Pawn tests

class testPawnListAvailableMoves(APITestCase):

    def test_status_code_200(self):
        response = self.client.get('/api/pawn/h3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'pawn')
        self.assertEqual(response.data['currentField'], 'H3')

    def test_status_code_404(self):
        response = self.client.get('/api/dawn/h3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['figure'], 'dawn')
        self.assertEqual(response.data['currentField'], 'H3')
        self.assertEqual(response.data['error'], 'Figure does not exist')

    def test_status_code_409(self):
        response = self.client.get('/api/pawn/z3')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['figure'], 'pawn')
        self.assertEqual(response.data['currentField'], 'Z3')
        self.assertEqual(response.data['error'], 'Field does not exist')

    def test_case_sensitivity(self):
        response = self.client.get('/api/PaWn/a3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'pawn')
        self.assertEqual(response.data['currentField'], 'A3')

    def test_pawn_moves(self):
        response = self.client.get('/api/pawn/a3')
        self.assertEqual(response.data['availableMoves'], ['A4'])

    def test_pawn_moves(self):
        response = self.client.get('/api/pawn/b7')
        self.assertEqual(response.data['availableMoves'], ['B8'])

    def test_pawn_moves(self):
        response = self.client.get('/api/pawn/h2')
        self.assertEqual(response.data['availableMoves'], ['H3', 'H4'])

    def test_pawn_on_1_line(self):
        response = self.client.get('/api/pawn/a1')
        self.assertEqual(response.status_code, 409)

    def test_pawn_on_8_line(self):
        response = self.client.get('/api/pawn/h8')
        self.assertEqual(response.status_code, 409)



class testPawnValidateMoves(APITestCase):

    def test_valid_move1(self):
        response = self.client.get('/api/pawn/h3/h4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_valid_move2(self):
        response = self.client.get('/api/pawn/h2/h4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_invalid_figure(self):
        response = self.client.get('/api/dawn/h2/h4')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_current_field(self):
        response = self.client.get('/api/pawn/h1/h4')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move1(self):
        response = self.client.get('/api/pawn/h2/h5')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move2(self):
        response = self.client.get('/api/pawn/h2/h1')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    
#### Rook tests

class testRookListAvailableMoves(APITestCase):

    def test_status_code_200(self):
        response = self.client.get('/api/rook/h3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'rook')
        self.assertEqual(response.data['currentField'], 'H3')

    def test_status_code_404(self):
        response = self.client.get('/api/rok/h3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['figure'], 'rok')
        self.assertEqual(response.data['currentField'], 'H3')
        self.assertEqual(response.data['error'], 'Figure does not exist')

    def test_status_code_409(self):
        response = self.client.get('/api/rook/z3')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['figure'], 'rook')
        self.assertEqual(response.data['currentField'], 'Z3')
        self.assertEqual(response.data['error'], 'Field does not exist')

    def test_case_sensitivity(self):
        response = self.client.get('/api/RoOk/a3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'rook')
        self.assertEqual(response.data['currentField'], 'A3')

    def test_pawn_moves(self):
        response = self.client.get('/api/rook/a3')
        self.assertEqual(response.data['availableMoves'], 
        ['A1','A2','A4','A5','A6','A7','A8',
         'B3','C3','D3','E3','F3','G3','H3'
        ])

    def test_pawn_moves(self):
        response = self.client.get('/api/rook/e7')
        self.assertEqual(response.data['availableMoves'], 
        ['A7','B7','C7','D7','E1','E2','E3',
         'E4','E5','E6','E8','F7','G7','H7'
        ])



class testRookValidateMoves(APITestCase):

    def test_valid_move1(self):
        response = self.client.get('/api/rook/h3/h4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_valid_move2(self):
        response = self.client.get('/api/rook/h2/a2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_invalid_current_field(self):
        response = self.client.get('/api/rook/h1/e7')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move1(self):
        response = self.client.get('/api/rook/f4/g1')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move2(self):
        response = self.client.get('/api/rook/c5/f4')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')


#### Knight tests

class testKnightListAvailableMoves(APITestCase):

    def test_status_code_200(self):
        response = self.client.get('/api/knight/h3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'knight')
        self.assertEqual(response.data['currentField'], 'H3')

    def test_status_code_404(self):
        response = self.client.get('/api/kngith/h3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['figure'], 'kngith')
        self.assertEqual(response.data['currentField'], 'H3')
        self.assertEqual(response.data['error'], 'Figure does not exist')

    def test_status_code_409(self):
        response = self.client.get('/api/knight/z3')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['figure'], 'knight')
        self.assertEqual(response.data['currentField'], 'Z3')
        self.assertEqual(response.data['error'], 'Field does not exist')

    def test_case_sensitivity(self):
        response = self.client.get('/api/KniGHt/a3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'knight')
        self.assertEqual(response.data['currentField'], 'A3')

    def test_knight_moves(self):
        response = self.client.get('/api/knight/a1')
        self.assertEqual(response.data['availableMoves'], 
            ['B3','C2']
        )

    def test_knight_moves(self):
        response = self.client.get('/api/knight/h1')
        self.assertEqual(response.data['availableMoves'], 
            ['F2','G3']
        )

    def test_knight_moves(self):
        response = self.client.get('/api/knight/f4')
        self.assertEqual(response.data['availableMoves'], 
            ['D3','D5','E2','E6','G2','G6','H3','H5']
        )

    def test_knight_moves(self):
        response = self.client.get('/api/knight/b8')
        self.assertEqual(response.data['availableMoves'], 
            ['A6','C6','D7']
        )

class testKnightValidateMoves(APITestCase):

    def test_valid_move1(self):
        response = self.client.get('/api/knight/h3/f4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_valid_move2(self):
        response = self.client.get('/api/knight/e5/d3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_invalid_current_field(self):
        response = self.client.get('/api/knight/z1/e7')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move1(self):
        response = self.client.get('/api/knight/f4/f5')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move2(self):
        response = self.client.get('/api/knight/c5/a5')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

#### Bishop tests

class testBishopListAvailableMoves(APITestCase):

    def test_status_code_200(self):
        response = self.client.get('/api/bishop/h3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'bishop')
        self.assertEqual(response.data['currentField'], 'H3')

    def test_status_code_404(self):
        response = self.client.get('/api/beeshop/h3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['figure'], 'beeshop')
        self.assertEqual(response.data['currentField'], 'H3')
        self.assertEqual(response.data['error'], 'Figure does not exist')

    def test_status_code_409(self):
        response = self.client.get('/api/bishop/z3')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['figure'], 'bishop')
        self.assertEqual(response.data['currentField'], 'Z3')
        self.assertEqual(response.data['error'], 'Field does not exist')

    def test_case_sensitivity(self):
        response = self.client.get('/api/BiShOp/a3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'bishop')
        self.assertEqual(response.data['currentField'], 'A3')

    def test_bishop_moves(self):
        response = self.client.get('/api/bishop/a2')
        self.assertEqual(response.data['availableMoves'], 
            ['A1','A3','C1','C3','D4','E5','F6','G7','H8']
        )

    def test_bishop_moves(self):
        response = self.client.get('/api/bishop/d4')
        self.assertEqual(response.data['availableMoves'], 
            ['A1','A7','B2','B6','C3','C5','E3','E5','F2','F6','G1','G7','H8']
        )

    def test_bishop_moves(self):
        response = self.client.get('/api/bishop/a5')
        self.assertEqual(response.data['availableMoves'], 
            ['B4','B6','C3','C7','D2','D8','E1']
        )

    def test_bishop_moves(self):
        response = self.client.get('/api/bishop/g3')
        self.assertEqual(response.data['availableMoves'], 
            ['B8','C7','D6','E1','E5','F2','F4','H2','H4']
        )

class testBishoptValidateMoves(APITestCase):

    def test_valid_move1(self):
        response = self.client.get('/api/bishop/h3/d7')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_valid_move2(self):
        response = self.client.get('/api/bishop/e5/b2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_invalid_current_field(self):
        response = self.client.get('/api/bishop/z1/e7')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move1(self):
        response = self.client.get('/api/bishop/f4/a4')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move2(self):
        response = self.client.get('/api/bishop/c5/g3')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

#### Queen tests

class testQueenListAvailableMoves(APITestCase):

    def test_status_code_200(self):
        response = self.client.get('/api/queen/h3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'queen')
        self.assertEqual(response.data['currentField'], 'H3')

    def test_status_code_404(self):
        response = self.client.get('/api/quen/h3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['figure'], 'quen')
        self.assertEqual(response.data['currentField'], 'H3')
        self.assertEqual(response.data['error'], 'Figure does not exist')

    def test_status_code_409(self):
        response = self.client.get('/api/queen/z3')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['figure'], 'queen')
        self.assertEqual(response.data['currentField'], 'Z3')
        self.assertEqual(response.data['error'], 'Field does not exist')

    def test_case_sensitivity(self):
        response = self.client.get('/api/QuEeN/a3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['figure'], 'queen')
        self.assertEqual(response.data['currentField'], 'A3')

    def test_queen_moves(self):
        response = self.client.get('/api/queen/a2')
        self.assertEqual(response.data['availableMoves'], 
            ['A1','A2','A3','B1','B3','B4','B5','B6','B7','B8','C1','C2','C3',\
             'D2','D4','E2','E5','F2','F6','G2','G7','H2','H8'    
            ]
        )

    def test_queen_moves(self):
        response = self.client.get('/api/queen/d6')
        self.assertEqual(response.data['availableMoves'], 
            ['A3','A6','B4','B6','B8','C5','C6','C7','D1','D2','D3','D4','D5',\
             'D7','D8','E5','E6','E7','F4','F6','F8','G3','G6','H2','H6'    
            ]
        )


class testKingtValidateMoves(APITestCase):

    def test_valid_move1(self):
        response = self.client.get('/api/queen/h3/c3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_valid_move2(self):
        response = self.client.get('/api/queen/e5/a1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['move'], 'valid')

    def test_invalid_current_field(self):
        response = self.client.get('/api/queen/z1/e7')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move1(self):
        response = self.client.get('/api/queen/f4/b6')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')

    def test_invalid_move2(self):
        response = self.client.get('/api/queen/c5/g6')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.data['move'], 'invalid')


#### King tests