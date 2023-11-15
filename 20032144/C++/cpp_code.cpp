#include <iostream>

using namespace std;

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

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                building[i][j] = startingBuilding[i][j];
            }
        }
    }

    void displayBuilding() {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                cout << building[i][j] << " ";
            }
            cout << endl;
        }
    }

    void updateBuilding(int row, int col, int waterOrFire) {
        if (row >= 0 && row < 4 && col >= 0 && col < 5) {
            building[row][col] = waterOrFire;
        }
    }

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

    int building[4][5];
};

class Game {
private:
    Building playerOneBuilding;
    Building playerTwoBuilding;

public:
    string player; 
    int roomNumber, row, col;
    int waterOrFire;
    bool gameOver = false;
    bool playerOneWins = false;
    bool playerTwoWins = false;
    bool playerOnesGo = true;
    bool playerTwosGo = false;

    // displayBothBuildings()
    void displayBothBuildings() {
        cout << "Player One's Building: " << endl;
        playerOneBuilding.displayBuilding();
        cout << endl;
        cout << "Player Two's Building: " << endl;
        playerTwoBuilding.displayBuilding();
        cout << endl;
    }

    // gameLoop()
    void gameLoop() {
        while (!gameOver) {
            check_winner();
            displayBothBuildings();
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
        if(check_player_win(playerOneBuilding)) {
            cout << "Player One wins" << endl;
            gameOver = true;
        }
        if(check_player_win(playerTwoBuilding)) {
            cout << "Player Two wins" << endl;
            gameOver = true;
        }
    }

    // check_player_win(+building)
    // Pass in a player's building and see if their building is all 1s or all 0s
    bool check_player_win(Building playerBuidling) {
        bool allOnes = true;
        bool allZeros = true;
        for(int i=0; i<4; i++) {
            for(int j=0; j<5; j++) {
                if(playerBuidling.building[i][j] != 1) {
                    allOnes = false;
                }
                if(playerBuidling.building[i][j] != 0) {
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

int main() {
    Game gameInstance;
    gameInstance.gameLoop();

    return 0;
}
