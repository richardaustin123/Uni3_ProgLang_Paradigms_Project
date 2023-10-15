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
playerOneWins = False
playerTwoWins = False
playerOnesGo = True
playerTwosGo = False
gameOver = False
col = 0
row = 0

# Player one building array
playerOneBuilding = [[ 1, 0, 0, 0, 0],    # 16. 17. 18. 19. 20. 
                     [ 0, 0, 0, 0, 0],    # 11. 12. 13. 14. 15.
                     [ 0, 0, 0, 0, 0],    # 6.  7.  8.  9.  10.
                     [ 0, 0, 0, 0, 0]]    # 1.  2.  3.  4.  5.

# Player two building array
playerTwoBuilding = [[ 1, 0, 0, 0, 1],    # 16. 17. 18. 19. 20. 
                     [ 0, 1, 0, 1, 0],    # 11. 12. 13. 14. 15.
                     [ 0, 1, 0, 1, 0],    # 6.  7.  8.  9.  10.
                     [ 0, 0, 1, 0, 0]]    # 1.  2.  3.  4.  5.

# main()
def main():
    play()

# play()
# Kick off the game
def play():
    intro()
    game_loop()

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
    global playerOneWins, playerTwoWins, playerOnesGo, playerTwosGo, gameOver, row, col # Global variables 
    while playerOneWins == False and playerTwoWins == False and gameOver == False:      # While no one has won
        if gameOver == False:                                                               # If the game is not over
            display_both_buildings()                                                        # Display player one and two's buildings
            if playerOnesGo == True:                                                        # If it's player one's go   
                take_turn("1", row, col)                                                    # Take player one's turn
                gameOver = check_winner(gameOver, playerOneWins, playerTwoWins)          # Check if player one has won
                playerOnesGo = False                                                        # Set player one's go to false
                playerTwosGo = True                                                         # Set player two's go to true
            elif playerTwosGo == True:                                                      # Same as above but for player two
                take_turn("2", row, col)
                gameOver = check_winner(gameOver, playerOneWins, playerTwoWins)
                playerTwosGo = False
                playerOnesGo = True
        elif gameOver == True:
            print("Game over\n")

# display_playerone_building()
# Print player one's building
def display_playerone_building():
    print("\nPlayer 1's building")
    for row in playerOneBuilding:
        print(' '.join(map(str, row)))
    print("\n")

# display_playertwo_building()
# Print player two's building
def display_playertwo_building():
    print("Player 2's building")
    for row in playerTwoBuilding:
        print(' '.join(map(str, row)))
    print("\n")

# display_both_buildings()
def display_both_buildings():
    display_playerone_building()
    display_playertwo_building()

# take_turn(+player, +row, +col)
# Each player takes a turn and their building is updated
def take_turn(player, row, col):
    print("It's player " + player + "'s turn\n")
    print("Press 1 to save your building or press 0 to spread fire on your opponent...\n")
    waterOrFire = int(input("Enter 1 or 0: \n")) 
    roomNumber = int(input("Which room do you chose (1-20): \n")) # get the room number index position
    if player == "1" and waterOrFire == 1:
        row, col = update_building(roomNumber, row, col) # Get the row and column to be updated in the building array, based on the room number selected by the user
        playerOneBuilding[row][col] = 1
        above_and_below(player, waterOrFire, row, col)
    elif player == "1" and waterOrFire == 0:
        row, col = update_building(roomNumber, row, col)
        playerTwoBuilding[row][col] = 0
        above_and_below(player, waterOrFire, row, col)
    elif player == "2" and waterOrFire == 1:
        row, col = update_building(roomNumber, row, col)
        playerTwoBuilding[row][col] = 1
        above_and_below(player, waterOrFire, row, col)
    elif player == "2" and waterOrFire == 0:
        row, col = update_building(roomNumber, row, col)
        playerOneBuilding[row][col] = 0
        above_and_below(player, waterOrFire, row, col)

# update_building(+roomNumber, -row, -col)
# Get the row and column that needs to be updated in the building array, based on the room number selected by the user
def update_building(roomNumber, row, col):
    if 1 <= roomNumber <= 20:
        row = 3 - (roomNumber - 1) // 5   # e.g. roomNumber = 13 so 13 - 1 = 12 // 5 = 2 so row = 3 - 2 = 1 which is the second row (0, 1, 2, 3)
        col = (roomNumber - 1) % 5        # e.g. roomNumber = 13 so 13 - 1 = 12 % 5 = 2 so col = 2 which is the third column (0, 1, 2, 3, 4)
    return row, col

# above_and_below(+player, +waterOrFire, +row, +col)
# Spread water or fire (1 or 0) below or above the room selected by the user, if the toom below or above is already water or fire (1 or 0)
def above_and_below(player, waterOrFire, row, col):
    # As long as the user doesn't select water for the bottom row or fire for the top row
    # As water cant spread to the bottom if we're already at the bottom
    # and fire cant spread to the top if we're already at the top
    if not(waterOrFire == 1 and row == 3) or (waterOrFire == 0 and row == 0):
        # If p1 selects 1 (water) and the row below is 1 (water) then set all rows below to 1 (water)
        if ((player == "1" and waterOrFire == 1) and (playerOneBuilding[row + 1][col] == 1 or playerOneBuilding[row - 1][col] == 1)):
            # set all rows below row+1 to 1 in a loop
            for i in range(row + 1, len(playerOneBuilding)):
                playerOneBuilding[i][col] = 1
        # If p1 selects 0 (fire) and the row above is 0 (fire) then set all rows above to 0 (fire)
        elif ((player == "1" and waterOrFire == 0) and (playerTwoBuilding[row + 1][col] == 0 or playerTwoBuilding[row - 1][col] == 0)):
            # set all rows above row-1 to 0 in a loop
            for i in range(row - 1, -1, -1):
                playerTwoBuilding[i][col] = 0
        # If p2 selects 1 (water) and the row below is 1 (water) then set all rows below to 1 (water)
        elif ((player == "2" and waterOrFire == 1) and (playerTwoBuilding[row + 1][col] == 1 or playerTwoBuilding[row - 1][col] == 1)):
            # set all rows below row+1 to 1 in a loop
            for i in range(row + 1, len(playerTwoBuilding)):
                playerTwoBuilding[i][col] = 1
        # If p2 selects 0 (fire) and the row above is 0 (fire) then set all rows above to 0 (fire)
        elif ((player == "2" and waterOrFire == 0) and (playerOneBuilding[row + 1][col] == 0 or playerOneBuilding[row - 1][col] == 0)):
            # set all rows above row-1 to 0 in a loop
            for i in range(row - 1, -1, -1):
                playerOneBuilding[i][col] = 0


# check_winner(-gameOver, +playerOneWins, +playerTwoWins)
# Check if p1 or p2 has won, return gameOver
def check_winner(gameOver, playerOneWins, playerTwoWins):
    if check_player_one_win(playerOneWins) == True:
        gameOver = True
        display_both_buildings()
        print("Player 1 wins\n")
    elif check_player_two_win(playerTwoWins) == True:
        gameOver = True
        display_both_buildings()
        print("\nPlayer 2 wins\n")
    return gameOver

# check_player_one_win(-playerOneWins)
# If player one's building has no fire (all 1's) or player two's building is all fire (all 0's) then player one wins
def check_player_one_win(playerOneWins):
    if playerOneBuilding == [[ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1]] or playerTwoBuilding == [[ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0], 
                                                                        [ 0, 0, 0, 0, 0]]:
        playerOneWins = True
        return playerOneWins

# check_player_two_win(-playerTwoWins)
# If player two's building has no fire (all 1's) or player one's building is all fire (all 0's) then player two wins
def check_player_two_win(playerTwoWins):
    if playerTwoBuilding == [[ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1],
                             [ 1, 1, 1, 1, 1]] or playerOneBuilding == [[ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0],
                                                                        [ 0, 0, 0, 0, 0], 
                                                                        [ 0, 0, 0, 0, 0]]:
        playerTwoWins = True
        return playerTwoWins


# Run the main function
# Environment variables
if __name__ == "__main__":
    main()
