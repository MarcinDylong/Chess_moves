# The simple REST application supporting the game of chess:
The application consist of two adresses:
 - [GET] `/api/{chess-figure}/{current-field}`;  Return possible moves for given figure from given field
 - [GET] `/api/{chess-figure}/{current-field}/{dest-field}`; Validate move for given figure from given field to other field.

Both adresses not include beats or possible collision with different figures (of the same colour).

### Board
<img src='https://upload.wikimedia.org/wikipedia/commons/2/2c/AAA_SVG_Chessboard_and_chess_pieces_02.svg' width='500' height='600'>

### Allowed figure:                
- pawn 
- rook 
- knight 
- bishop 
- queen 
- king 

### Responses
 - 200 - When everything is ok
 - 404 - When asked for not allowed figure (names are not case sensitive)
 - 409 - When asked for field outside board
 - 500 - Server error
            
Important!
Pawn cannot appear on line 1 or 8, they start from lines 2 or 7 (see image above) and when reach last line
they transform to quuen therefore thay cannot appear on respective last line. For this reason asking for pawn on line 1 or 8 will return 409 error<br>
Also for sake of simplicity app return moves for white pawns.
    
### Examples:
- **[GET] '/api/rook/a1'** will return
```
    {
        "availableMoves": [
            "A2",
            "A3",
            "A4",
            "A5",
            "A6",
            "A7",
            "A8",
            "B1",
            "C1",
            "D1",
            "E1",
            "F1",
            "G1",
            "H1"
        ],
        "error": null,
        "figure": "rook",
        "currentField": "A1"
    }
```
- **[GET] '/api/rook/a1/a6'** will return:
``` 
    {
        "move": "invalid",
        "figure": "rook",
        "error": "Move in not valid",
        "currentField": "A1",
        "destField": "B6"
    }
```
- **[GET] '/api/rook/b10'** will return:
```
    {
        "availableMoves": [],
        "error": "Field does not exist",
        "figure": "rook",
        "currentField": "B10"
    }
```

# How to run it:

Clone repository and run app with IDE of your choice:

```bash
$ # Clone repository 
$ git clone https://github.com/MarcinDylong/Chess_moves.git
$ cd Chess
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Install modules
$ pip3 install -r requirements.txt
$
$ # Start the application
$ python3 manage.py runserver
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/):

```bash
$ # Clone repository 
$ git clone https://github.com/MarcinDylong/Chess_moves.git
$ cd Chess
$
$ # Run docker
$
$ docker-compose up
$
$ # Access the web app in browser: http://0.0.0.0:8000/
```