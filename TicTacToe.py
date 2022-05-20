class Square:
    def __init__(self):
        self.owner = None
        self.isOwned = False
        self.index = 0

    def setOwner(self, newOwner):
        self.owner = newOwner
        self.isOwned = True

    def getOwner(self):
        return self.owner

    def setIndex(self, newIndex):
        self.index = newIndex
    def getIndex(self):
        return self.index

    def __repr__(self):
        return f"Square {self.index}"


class GameBoard:
    def __init__(self):
        self.__board = []
        self.constructBoard()
        self.winner = None

    def constructBoard(self):
        for x in range(9):
            newSquare = Square()
            newSquare.setIndex(x)
            self.__board.append(newSquare)

    def getBoard(self):
        return self.__board

    def getOwners(self):
        tmp = []
        for square in self.getBoard():
            tmp.append(square.getOwner())
        return tmp

    def getWinner(self):
        return self.winner

    def setOwner(self, newOwner, index=0):
        self.getBoard()[index].setOwner(newOwner)

    def checkForWinner(self):
        board = self.getBoard()
        isWinner = False

        # Check for 3 across
        for x in range(0, 9, 3):
            if board[x].getOwner() == board[x+1].getOwner() == board[x+2].getOwner() != None:
                isWinner = True
                self.winner = board[x].getOwner()

        # Check for 3 down
        for x in range(3):
            if board[x].getOwner() == board[x+3].getOwner() == board[x+6].getOwner() != None:
                isWinner = True
                self.winner = board[x].getOwner()

        # Check for Diagonals
        if board[0].getOwner() == board[4].getOwner() == board[8].getOwner() != None:
            isWinner = True
            self.winner = board[0].getOwner()
        if board[2].getOwner() == board[4].getOwner() == board[6].getOwner() != None:
            isWinner = True
            self.winner = board[2].getOwner()

        return isWinner

    def drawBoard(self, xPlayer, oPlayer):
        board = self.getBoard()
        prettyBoard="""
        0 # 1 # 2
        #########
        3 # 4 # 5
        #########
        6 # 7 # 8
        """
        for square in board:
            if square.getOwner() == xPlayer:
                prettyBoard = prettyBoard.replace(str(square.getIndex()), "X")
            elif square.getOwner() == oPlayer:
                prettyBoard = prettyBoard.replace(str(square.getIndex()), "O")


        print(prettyBoard)

    def __str__(self):
        return str(self.__board)


class Player:
    def __init__(self, name="New Player"):
        self.__nextPlayer = None
        self.__name = name

    def setName(self, newName):
        self.__name = newName

    def getName(self):
        return self.__name

    def setNextPlayer(self, newNextPlayer):
        self.__nextPlayer = newNextPlayer

    def getNextPlayer(self):
        return self.__nextPlayer

    def __str__(self):
        return str(self.__name)
