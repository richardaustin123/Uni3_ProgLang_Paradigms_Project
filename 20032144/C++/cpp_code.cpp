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

    void displayBothBuildings() {
        cout << "Player One's Building: " << endl;
        playerOneBuilding.displayBuilding();
        cout << endl;
        cout << "Player Two's Building: " << endl;
        playerTwoBuilding.displayBuilding();
        cout << endl;
    }

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

    void take_turn(string player) {
        cout << "It's Player " << player << "'s turn\n";
        cout << "Press 1 to spread water in your building or press 0 to spread fire on your opponent\n";
        cout << "Enter 1 or 0: ";
        cin >> waterOrFire;
        cout << "Which room do you chose (1-20): ";
        cin >> roomNumber;
        get_row_col(roomNumber, row, col);

        if (player == "1") {
            if (waterOrFire == 1) {
                // playerOneBuilding.updateBuilding(row, col, waterOrFire);
                playerOneBuilding.spread_water(row, col);
            } else if (waterOrFire == 0) {
                // playerTwoBuilding.updateBuilding(row, col, waterOrFire);
                playerTwoBuilding.spread_fire(row, col);
            } 
        } else if (player == "2") {
            if (waterOrFire == 1) {
                // playerTwoBuilding.updateBuilding(row, col, waterOrFire);
                playerTwoBuilding.spread_water(row, col);
            } else if (waterOrFire == 0) {
                // playerOneBuilding.updateBuilding(row, col, waterOrFire);
                playerOneBuilding.spread_fire(row, col);
            }
        }
    }

    void get_row_col(int roomNumber, int& row, int& col) {
        if (roomNumber < 1 || roomNumber > 20) {
            cout << "Invalid room number\n";
        }
        row = 3 - (roomNumber - 1) / 5;
        col = (roomNumber - 1) % 5;
    }

};

int main() {
    Game gameInstance;
    gameInstance.gameLoop();

    return 0;
}
