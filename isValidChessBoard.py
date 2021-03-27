#The function defined below isValidChessBoard accepts a dictionary with items
#{location1:chess_piece1, location2:chess_piece2} and evaluates whether or not
#the chess board is valid according to the following rules: must be types bKing,
#wKing, etc., cannot be duplicate pieces (9 black pawns, 3 white bishops, etc.),
#Kings must be present, and pieces must be at real locations (1a - 8h). To do
#this I needed to develop lists of possible moves and allowable pieces, and 
#another dictionary to track the number of pieces allowed per piece type.


#Generate list of possible moves
letters = ['a','b','c','d','e','f','g', 'h']
possibleMoves = []
for i in range(8):
    for j in range(len(letters)):
        possibleMoves.append(str(i) + letters[j])

#Generate list of pieces
pieces = ['King','Queen','Bishop','Knight','Rook','Pawn']
pieces *= 2
for i in range(len(pieces)):
    if i <=5:
        pieces[i] = 'w' + pieces[i]
    else:
        pieces[i] = 'b' + pieces[i]

#Generate dictionary of number of pieces allowed per piece type
piecesCount = {}
for i in range(len(pieces)):
    if pieces[i] == 'wKing' or pieces[i] == 'bKing' or pieces[i] == 'wQueen' or pieces[i] == 'bQueen':
        piecesCount[pieces[i]] = 1
    elif pieces[i] == 'wPawn' or pieces[i] == 'bPawn':
        piecesCount[pieces[i]] = 8
    else:
        piecesCount[pieces[i]] = 2


def isValidChessBoard(board):
    
    #Create lists that represent the pieces and their locations.
    boardPieces = list(board.values())
    boardLocations = list(board.keys())
    
    #Determine if types of pieces that exist on board are allowed.
    for i in range(len(boardPieces)):
        if boardPieces[i] not in pieces:
            print("Invalid Piece on the Board: " + boardPieces[i])
            return False
    
    #Determine if duplicate pieces are on the board.
    for k in range(len(boardPieces)):
        if boardPieces.count(boardPieces[k]) > piecesCount.get(boardPieces[k]):
            print("Duplicate pieces on the board: " + boardPieces[k])
            return False
    
    #Determine if kings are not present.
    if boardPieces.count('wKing') != 1 or boardPieces.count('bKing') != 1:
        print('Where is your king bro?')
        return False
    
    #Determine if pieces are on valid locations.
    for j in range(len(boardLocations)):
        if boardLocations[j] not in possibleMoves:
            print("Piece at Invalid Location: " + boardLocations[j])
            return False
    
    #Otherwise return True --> Board is acceptable.
    print('Board is acceptable.')
    return True

#Generate test boards and validate function. This tests what happens if you
#provide a board with 9 black pawns.
testBoard1 = {'2a':'bPawn', '2b':'bPawn', '3a':'bKing', '4b': 'wKing', '1a':'bPawn', '1b':'bPawn','1c':'bPawn','1d':'bPawn','1e':'bPawn','1f':'bPawn', '1g':'bPawn'}
isValidChessBoard(testBoard1)
        