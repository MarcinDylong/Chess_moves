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



class testPawnValidateMoves(APITestCase):

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


#### Bishop tests


#### Queen tests


#### King tests