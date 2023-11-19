

# Global variables
playerOneWins = False
playerTwoWins = False
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
    print("\Welcome to Saviour vs Scorcher\n")
    print("\nYOUR BUILDING IS ON FIRE\n")
    print("And so is your opponents...\n")
    print("You hate your opponent...\n")
    print("You can save your building... or destroy your opponents...\n")
    print("1 = Water")
    print("0 = Fire\n")
    print(input("Press enter to continue\n"))
    print("If you stack two 1's on top of each other, then the water will flow down to all rooms directly below\n")
    print("If you stack two 0's on top of each other, then the fire will flow up to all rooms directly above\n")
    print(input("Press enter to continue\n"))
    display_both_buildings()
    print(input("Press enter to continue\n"))
    print("These are the building numbers\n")
    display_building_numbers()
    print(input("Press enter to start\n"))

# display_building_numbers()
def display_building_numbers():
    print(" 16.  17.  18.  19.  20.")
    print(" 11.  12.  13.  14.  15.")
    print(" 6.   7.   8.   9.   10.")
    print(" 1.   2.   3.   4.   5.\n")

# game_loop()
def game_loop():
    global playerOneWins, playerTwoWins, playerOnesGo, playerTwosGo, gameOver           # Global variables 
    while playerOneWins == False and playerTwoWins == False and gameOver == False:      # While no one has won
            display_both_buildings()                                                    # Display player one and two's buildings
            if playerOnesGo == True:                                                    # If it's player one's go   
                take_turn("1")                                                          # Take player one's turn
                gameOver = check_winner(gameOver, playerOneWins, playerTwoWins)         # Check if player one has won
                playerOnesGo = False                                                    # Set player one's go to false
                playerTwosGo = True                                                     # Set player two's go to true
            elif playerTwosGo == True:                                                  # Same as above but for player two
                take_turn("2")
                gameOver = check_winner(gameOver, playerOneWins, playerTwoWins)
                playerTwosGo = False
                playerOnesGo = True

# display_both_buildings()
def display_both_buildings():
    print("Player 1's building\n")
    display_building(playerOneBuilding)
    print("Player 2's building\n")
    display_building(playerTwoBuilding)

# display_building(+buildingArray)
# Print the building array with a given player's building
def display_building(buildingArray):
    for row in buildingArray:
        print(' '.join(map(str, row))) # Print the row with a space between each number
    print("\n")

# take_turn(+player)
# Each player takes a turn and their building is updated
def take_turn(player):
    print("It's player " + player + "'s turn\n")
    print("Press 1 to spread water in your building or press 0 to spread fire on your opponent\n")
    waterOrFire = check_integer("Enter 1 or 0: \n")
    roomNumber = check_integer("Which room do you chose (1-20): \n") # Get the room number index position
    row = 0
    col = 0
    row, col = update_building(roomNumber, row, col)    # Get the row and column to be updated in the building array, based on the room number selected by the user
    if player == "1":
        if waterOrFire == 1:
            spread_water(playerOneBuilding, row, col)   # If P1 chose water then spread water in P1's building
        elif waterOrFire == 0:
            spread_fire(playerTwoBuilding, row, col)    # If P1 chose fire then spread fire in P2's building
    elif player == "2":
        if waterOrFire == 1:
            spread_water(playerTwoBuilding, row, col)   # If P2 chose water then spread water in P2's building
        elif waterOrFire == 0:
            spread_fire(playerOneBuilding, row, col)    # If P2 chose fire then spread fire in P1's building

# check_integer(+number)
# Check if the user input is an integer
def check_integer(number):
    while True:
        player_input = input(number)
        try:
            return int(player_input)
        except ValueError:
            print("**************** Invalid input ****************\n")

# update_building(+roomNumber, -row, -col)
# Get the row and column that needs to be updated in the building array, based on the room number selected by the player
def update_building(roomNumber, row, col):
    if 1 <= roomNumber <= 20:
        row = 3 - (roomNumber - 1) // 5   # e.g. roomNumber = 13 so 13 - 1 = 12 // 5 = 2 so row = 3 - 2 = 1 which is the second row (0, 1, 2, 3)
        col = (roomNumber - 1) % 5        # e.g. roomNumber = 13 so 13 - 1 = 12 % 5 = 2 so col = 2 which is the third column (0, 1, 2, 3, 4)
    return row, col

# spread_water(+buildingArray, +row, +column)
# Pass in the building (p1's or p2's) and in the column for the room number index the player selected
# If player selected water (1) and there is a 1 above or below (two 1's on top of each other) 
# then spread the water down the column
def spread_water(buildingArray, row, column):
    buildingArray[row][column] = 1
    flag = False
    # loop for each row
    for row in range(0, 4):
        # check the flag (flag true when we are water and we have found another water)
        if(flag == True and buildingArray[row][column] == 1): 
            # flow the water down the building column
            for waterRow in range(row, 4):
                buildingArray[waterRow][column] = 1 # set that row and column index to 1
            return
        # if we are water then flag true
        if(buildingArray[row][column] == 1):
            flag = True

# spread_fire(+buildingArray, +row, +column)
# Pass in the building (p1's or p2's) and in the column for the room number index the player selected
# If player selected fire (0) and there is a 0 above or below (two 0's on top of each other)
# then spread the fire up the column
def spread_fire(buildingArray, row, column):
    buildingArray[row][column] = 0
    flag = False
    # loop for each row
    for row in range(3, 0, -1):
        # check the flag
        if(flag == True and buildingArray[row][column] == 0):
            # flow the fire up the building column
            # range(the current row, down to including 0, down 1 each loop)
            for fireRow in range(row, -1, -1): # start at row and go down to -1 (down to 0 as python range goes up to but not including the last number)
                buildingArray[fireRow][column] = 0
            return 
        # if we are fire then flag true
        if(buildingArray[row][column] == 0):
            flag = True


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
