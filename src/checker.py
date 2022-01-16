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
  
     def checkWinner(self) :
        countw = 0
        countr = 0
        for i in self.board:
            for j in i:
                if j == 1 or j == 3:
                    countw += 1
                elif j == 2 or j == 4:
                    countr += 1
                else:
                    continue
        if countr == 0:
            self.isWon = 'white'
        elif countw == 0:
            self.isWon = 'red'
    def changeTurn(self) :
        if self.whoseMove == "white":
            self.whoseMove = "red"
        elif self.whoseMove == "red":
            self.whoseMove = "white"    
        
