from TicTacToe import *

Player1 = Player("Player 1")
Player2 = Player("Player 2")

Player1.setNextPlayer(Player2)
Player2.setNextPlayer(Player1)

newBoard = GameBoard()
currentPlayer = Player1

GUI = False

if GUI:
    # TODO: Add a GUI
    pass

else:
    # GUI-less mode main loop
    while True:

        # Draw the board
        newBoard.drawBoard(Player1, Player2)

        # Check for a winner
        if newBoard.checkForWinner():
            print(f"WINNER {newBoard.getWinner()}")
            break

        # Also check that the board isn't full yet
        elif None not in newBoard.getOwners():
            print(newBoard.getOwners())
            print("THE GAME ENDS IN A DRAW")
            break

        # Board isn't full, and we don't have a winner yet. Get some input
        else:
            # TODO Add catch for if player inputs a string
            choice = int(input(f"{currentPlayer}, Please enter a choice between 0 and 8: "))

            # Validate input
            if choice in range(9):
                chosenSquare = newBoard.getBoard()[choice]

                # Check that the chosen square is unowned
                if chosenSquare.getOwner() == None:
                    chosenSquare.setOwner(currentPlayer)
                    currentPlayer = currentPlayer.getNextPlayer()

                # chosen square is already taken
                else:
                    print(f"{chosenSquare} is already owned by {chosenSquare.getOwner()}. Please pick a new one.")

            # Player picked a number outside of the valid range
            else:
                print("\nInput must be a number between 0 and 8, please pick again")
