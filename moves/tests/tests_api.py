from rest_framework.test import APITestCase

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



class testValidateMoves(APITestCase):

    def test_status_code(self):
        response = self.client.get('/api/pawn/h3/h5')
        self.assertEqual(response.status_code, 200)