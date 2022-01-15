class CheckersGame () :
    def __init__ (self) :
        self.coins = ('empty space','white checker','red checker','white king','red king')
        self.board =  [ [ 0, 2, 0, 2, 0, 2, 0, 2 ]
                      , [ 2, 0, 2, 0, 2, 0, 2, 0 ]
                      , [ 0, 2, 0, 2, 0, 2, 0, 2 ]
                      , [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                      , [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                      , [ 1, 0, 1, 0, 1, 0, 1, 0 ]
                      , [ 0, 1, 0, 1, 0, 1, 0, 1 ]
                      , [ 1, 0, 1, 0, 1, 0, 1, 0 ]
                      ]

        self.whoseMove = "white"
        self.isWon = 0
