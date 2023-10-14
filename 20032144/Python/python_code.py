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
col = 0
row = 0

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
def playerOneWin(playerOneWinner):
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
def playerTwoWin(playerTwoWinner):
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
def checkWinner(gameOver, playerOneWinner, playerTwoWinner):
    playerOneWin(playerOneWinner)
    playerTwoWin(playerTwoWinner)
    if playerOneWinner == True:
        print("Player 1 wins\n")
        gameOver = True
    elif playerTwoWinner == True:
        print("Player 2 wins\n")
        gameOver = True
    return gameOver

# take_turn(+player)
def take_turn(player, row, col):
    print("It's player " + player + "'s turn\n")
    print("Press 1 to save your building or press 0 to spread fire on your opponent...\n")
    waterOrFire = int(input("Enter 1 or 0: \n")) 
    move = int(input("Which room do you chose (1-20): \n")) # get the move index position
    if player == "1" and waterOrFire == 1:
        row, col = update_building(move, row, col)
        playerOneBuilding[row][col] = 1 # User enters 1-20 where 1 is the bottom of the building and 20 is the top so we need to reverse the index (19 - flat number) and then - 1 as array is 0-19 not 1-20
        display_playerone_building()
    elif player == "1" and waterOrFire == 0:
        row, col = update_building(move, row, col)
        playerTwoBuilding[row][col] = 0
        display_playertwo_building()
    elif player == "2" and waterOrFire == 1:
        row, col = update_building(move, row, col)
        playerTwoBuilding[row][col] = 1
        display_playertwo_building() 
    elif player == "2" and waterOrFire == 0:
        row, col = update_building(move, row, col)
        playerOneBuilding[row][col] = 0
        display_playerone_building()

# update_building(+move, -row, -col)
def update_building(move, row, col):
    if 1 <= move <= 20:
        row = 3 - (move - 1) // 5
        col = (move - 1) % 5
    return row, col

# intro()
def intro():
    print("\nYOU'RE BUILDING IS ON FIRE\n")
    print("And so is your opponents...\n")
    print("You hate your opponet...\n")
    print("You can save your building... or destroy your opponents...\n")
    print("1 = No fire")
    print("0 = Fire!\n")
    print(input("Press enter to start\n"))
    display_playerone_building()
    display_playertwo_building()
    print(input("Press enter to continue\n"))
    print("These are the building numbers\n")
    display_building_numbers()
    print(input("Press enter to continue\n"))

# display_building_numbers()
def display_building_numbers():
    print(" 16.  17.  18.  19.  20.")
    print(" 11.  12.  13.  14.  15.")
    print(" 6.   7.   8.   9.   10.")
    print(" 1.   2.   3.   4.   5.\n")

# game_loop()
def game_loop():
    global playerOneWinner, playerTwoWinner, playerOnesGo, playerTwosGo, gameOver, row, col
    if gameOver == False:
        display_playerone_building()
        display_playertwo_building()
        if playerOnesGo == True:
            take_turn("1", row, col)
            checkWinner(gameOver, playerOneWinner, playerTwoWinner)
            playerOnesGo = False
            playerTwosGo = True
        elif playerTwosGo == True:
            take_turn("2", row, col)
            checkWinner(gameOver, playerOneWinner, playerTwoWinner)
            playerTwosGo = False
            playerOnesGo = True
    elif gameOver == True:
        print("Game over\n")

# play()
# Kick off the game
def play():
    intro()
    game_loop()

# main()
def main():
    play()

# Run the main function
# Environment variables
if __name__ == "__main__":
    main()
