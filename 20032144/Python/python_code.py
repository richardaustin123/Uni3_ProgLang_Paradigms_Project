# Fire building game

#    P1 Builing            
# [ 0, 1, 1, 1, 0],    # 16. 17. 18. 19. 20. 

# [ 1, 0, 1, 0, 1],    # 11. 12. 13. 14. 15.

# [ 1, 0, 1, 0, 1],    # 6.  7.  8.  9.  10.

# [ 0, 1, 1, 1, 0]]    # 1.  2.  3.  4.  5.


#    P2 Building          
# [ 0, 1, 1, 1, 0],    # 16. 17. 18. 19. 20. 

# [ 1, 0, 1, 0, 1],    # 11. 12. 13. 14. 15.

# [ 1, 0, 1, 0, 1],    # 6.  7.  8.  9.  10.

# [ 0, 1, 1, 1, 0]]    # 1.  2.  3.  4.  5.

# Globle variables
playerOneWinner = False
playerTwoWinner = False
playerOnesGo = True
playerTwosGo = False
gameOver = False

# Player one building array
playerOneBuilding = [[ 1, 0, 0, 0, 1],    # 16. 17. 18. 19. 20. 
                     [ 0, 1, 0, 1, 0],    # 11. 12. 13. 14. 15.
                     [ 0, 1, 0, 1, 0],    # 6.  7.  8.  9.  10.
                     [ 0, 0, 1, 0, 0]]    # 1.  2.  3.  4.  5.

# Player two building array
playerTwoBuilding = [[ 1, 0, 0, 0, 1],    # 16. 17. 18. 19. 20. 
                     [ 0, 1, 0, 1, 0],    # 11. 12. 13. 14. 15.
                     [ 0, 1, 0, 1, 0],    # 6.  7.  8.  9.  10.
                     [ 0, 0, 1, 0, 0]]    # 1.  2.  3.  4.  5.

# Set the building
building = ["-"] * 20

# display_playerone_building()
# Use the previously made building array of "-"s to display the building
def display_playerone_building():
    # print(building[0],  building[1],  building[2],  building[3],  building[4])  # - - - - -
    # print(building[5],  building[6],  building[7],  building[8],  building[9])  # - - - - -
    # print(building[10], building[11], building[12], building[13], building[14]) # - - - - -
    # print(building[15], building[16], building[17], building[18], building[19]) # - - - - -
    print("Player 1's building")
    for row in playerOneBuilding:
        print(' '.join(map(str, row)))
    print("\n")

# display_playertwo_building()
# Use the previously made building array of "-"s to display the building
def display_playertwo_building():
    # print(building[0],  building[1],  building[2],  building[3],  building[4])  # - - - - -
    # print(building[5],  building[6],  building[7],  building[8],  building[9])  # - - - - -
    # print(building[10], building[11], building[12], building[13], building[14]) # - - - - -
    # print(building[15], building[16], building[17], building[18], building[19]) # - - - - -
    print("Player 2's building")
    for row in playerOneBuilding:
        print(' '.join(map(str, row)))
    print("\n")

# playerOneWin()
def playerOneWin():
    if playerOneBuilding == [[ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1]] or playerTwoBuilding == [[ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0], 
                                                                        [ 0, 0, 0, 0, 0]]:
        playerOneWinner = True
    return playerOneWinner

# playerTwoWin()
def playerTwoWin():
    if playerTwoBuilding == [[ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1]] or playerOneBuilding == [[ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0], 
                                                                        [ 0, 0, 0, 0, 0]]:
        playerTwoWinner = True
    return playerTwoWinner

# checkWinner()
def checkWinner():
    if playerOneWin() == True:
        print("Player 1 wins\n")
        gameOver = True
    elif playerTwoWin() == True:
        print("Player 2 wins\n")
        gameOver = True

# take_turn(+player)
def take_turn(player):
    print("It's player " + player + "'s turn\n")
    print("Press 1 to save your building or press 0 to spread fire on your opponent...\n")
    waterOrFire = int(input("Enter 1 or 0: \n")) 
    move = int(input("Enter move index (1-20): \n")) # get the move index position
    if player == "1" and waterOrFire == 1:
        playerOneBuilding[move-1] = 1
    elif player == "1" and waterOrFire == 0:
        playerTwoBuilding[move-1] = 0
    elif player == "2" and waterOrFire == 1:
        playerTwoBuilding[move-1] = 1
    elif player == "2" and waterOrFire == 0:
        playerOneBuilding[move-1] = 0

def intro():
    print("YOU'RE BUILDINGS ON FIRE\n")
    print("And so is your opponents...\n")
    print("You hate your opponet...\n")
    print("You can save your building... or destroy your opponents...\n")
    print("1 = No fire\n")
    print("0 = Fire!\n")

# game_loop()
def game_loop():
    global playerOneWinner, playerTwoWinner, playerOnesGo, playerTwosGo, gameOver
    if gameOver == False:
        display_playerone_building()
        display_playertwo_building()
        if playerOnesGo == True:
            take_turn("1")
            checkWinner()
            playerOnesGo = False
            playerTwosGo = True
        elif playerTwosGo == True:
            take_turn("2")
            checkWinner()
            playerTwosGo = False
            playerOnesGo = True
    elif gameOver == True:
        print("Game over\n")

# main()
def main():
    game_loop()

# Run the main function
# Environment variables
if __name__ == "__main__":
    main()
