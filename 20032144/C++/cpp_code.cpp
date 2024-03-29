#include <iostream>

using namespace std;

// Building class
class Building {
public:
    Building() {
        int startingBuilding[4][5] = {
            {1, 0, 0, 0, 1},
            {0, 1, 0, 1, 0},
            {0, 1, 0, 1, 0},
            {0, 0, 1, 0, 0}
        };

        // test 
        // {1, 1, 1, 1, 1},
        // {1, 1, 1, 1, 1},
        // {1, 1, 1, 1, 1},
        // {0, 1, 1, 1, 1}

        // Set the building array to the starting building
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                building[i][j] = startingBuilding[i][j]; 
            }
        }
    }

    // display_building()
    void display_building() {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                cout << building[i][j] << " ";
            }
            cout << endl;
        }
    }

    // spread_water(+row, +col)
    // Spread water down from the row and column of the chosen room
    // if above or below is a 1
    void spread_water(int row, int col) {
        building[row][col] = 1;
        bool flag = false;
        for (int i = 0; i < 4; i++) {
            if (flag && building[i][col] == 1) {
                for (int waterRow = i; waterRow < 4; waterRow++) {
                    building[waterRow][col] = 1;
                }
                return;
            }
            if (building[i][col] == 1) {
                flag = true;
            }
        }
    }

    // spread_fire(+row, +col)
    // Spread fire up from the row and column of the chosen room
    // if above or below is a 0 
    void spread_fire(int row, int col) {
        building[row][col] = 0;
        bool flag = false;
        for (int i = 3; i >= 0; i--) {
            if (flag && building[i][col] == 0) {
                for (int fireRow = i; fireRow >= 0; fireRow--) {
                    building[fireRow][col] = 0;
                }
                return;
            }
            if (building[i][col] == 0) {
                flag = true;
            }
        }
    }

    // building array, 4 rows, 5 columns
    int building[4][5];
};

// Game class
class Game {
// Building objects
private:
    Building playerOneBuilding;
    Building playerTwoBuilding;

// Variables
public:
    string player; 
    int roomNumber, row, col;
    int waterOrFire;
    bool gameOver = false;
    bool playerOneWins = false;
    bool playerTwoWins = false;
    bool playerOnesGo = true;
    bool playerTwosGo = false;

    // intro()
    void intro() {
        cout << "Welcome to Saviour vs Scorcher\n";
        cout << "\nYOUR BUILDING IS ON FIRE\n";
        cout << "And so is your opponents...\n";
        cout << "You hate your opponent...\n";
        cout << "You can save your building... or destroy your opponents...\n";
        cout << "1 = Water";
        cout << "0 = Fire\n";
        cout << "Press enter to continue\n";
        cin.ignore();
        cout << "If you stack two 1's on top of each other, then the water will flow down to all rooms directly below\n";
        cout << "If you stack two 0's on top of each other, then the fire will flow up to all rooms directly above\n";
        cout << "Press enter to continue\n";
        cin.ignore();
        display_both_buildings();
        cout << "Press enter to continue\n";
        cin.ignore();
        cout << "These are the building numbers\n";
        display_building_numbers();
        cout << "Press enter to start\n\n";
        cin.ignore();
    }

    // display_building_numbers()
    void  display_building_numbers() {
        cout << (" 16.  17.  18.  19.  20.\n");
        cout << (" 11.  12.  13.  14.  15.\n");
        cout << (" 6.   7.   8.   9.   10.\n");
        cout << (" 1.   2.   3.   4.   5.\n\n");
    }

    // display_both_buildings()
    void display_both_buildings() {
        cout << "Player One's Building: " << endl;
        playerOneBuilding.display_building();
        cout << endl;
        cout << "Player Two's Building: " << endl;
        playerTwoBuilding.display_building();
        cout << endl;
    }

    // game_loop()
    void game_loop() {
        while (!gameOver) {
            check_winner();
            display_both_buildings();
            if (playerOnesGo) {
                take_turn("1");
                playerOnesGo = false;
                playerTwosGo = true;
            }
            else if (playerTwosGo) {
                take_turn("2");
                playerTwosGo = false;
                playerOnesGo = true;
            }
        }
    }

    // check_winner()
    void check_winner() {
        if(check_player_win(playerOneBuilding, playerTwoBuilding)) {
            cout << "Player One wins" << endl;
            display_both_buildings();
            gameOver = true;
        }
        if(check_player_win(playerTwoBuilding, playerOneBuilding)) {
            cout << "Player Two wins" << endl;
            display_both_buildings();
            gameOver = true;
        }
    }

    // check_player_win(+building)
    // Pass in a player's building and see if their building is all 1s or all 0s
    bool check_player_win(Building playingPlayerBuidling, Building opponentPlayerBuidling) {
        bool allOnes = true;
        bool allZeros = true;
        for(int i=0; i<4; i++) {
            for(int j=0; j<5; j++) {
                if(playingPlayerBuidling.building[i][j] != 1) {
                    allOnes = false;
                }
                if(opponentPlayerBuidling.building[i][j] != 0) {
                    allZeros = false;
                }
            }
        }
        return allOnes || allZeros;
    }

    // take_turn()
    void take_turn(string player) {
        cout << "It's Player " << player << "'s turn\n";
        choose_water_or_fire();
        get_row_col(roomNumber, row, col);

        if (player == "1") {
            if (waterOrFire == 1) {
                playerOneBuilding.spread_water(row, col);
            } else if (waterOrFire == 0) {
                playerTwoBuilding.spread_fire(row, col);
            } 
        } else if (player == "2") {
            if (waterOrFire == 1) {
                playerTwoBuilding.spread_water(row, col);
            } else if (waterOrFire == 0) {
                playerOneBuilding.spread_fire(row, col);
            }
        }
    }

    // choose_water_or_fire()
    void choose_water_or_fire() {
        cout << "Press 1 to spread water in your building or press 0 to spread fire on your opponent\n";
        bool validInput = false;
        while (validInput == false) {
            cout << "Enter 1 or 0: ";
            cin >> waterOrFire;
            if (waterOrFire == 1) {
                break;
                validInput = true;
            } else if (waterOrFire == 0) {
                break;
                validInput = true;
            } else {
                cout << "Invalid number\n";
                validInput = false;
            }
        }
    }

    // get_row_col()
    // Get the row and column from the room number the player chose
    void get_row_col(int roomNumber, int& row, int& col) {
        bool validInput = false;
        while (validInput == false) {
            cout << "Which room do you chose (1-20): ";
            cin >> roomNumber;
            if (roomNumber < 1 || roomNumber > 20) {
                cout << "Invalid room number\n";
            } else {
                row = 3 - (roomNumber - 1) / 5;
                col = (roomNumber - 1) % 5;
                validInput = true;
                break;
            }
        }
    }

};

// main()
// Create a game instance and call the game_loop() function
int main() {
    Game gameInstance;
    gameInstance.intro();
    gameInstance.game_loop();

    return 0;
}
