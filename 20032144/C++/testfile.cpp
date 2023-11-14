#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

class Building {
public:
    vector<vector<int>> buildingArray;

    Building() {
        buildingArray = {{1, 0, 0, 0, 1},
                         {0, 1, 0, 1, 0},
                         {0, 1, 0, 1, 0},
                         {0, 0, 1, 0, 0}};
    }

    void displayBuilding() {
        for (auto &row : buildingArray) {
            for (int &cell : row) {
                cout << cell << " ";
            }
            cout << endl;
        }
    }

    void spread_water(int row, int column) {
        buildingArray[row][column] = 1;
        bool flag = false;
        for (int i = 0; i < 4; i++) {
            if (flag && buildingArray[i][column] == 1) {
                for (int waterRow = i; waterRow < 4; waterRow++) {
                    buildingArray[waterRow][column] = 1;
                }
                return;
            }
            if (buildingArray[i][column] == 1) {
                flag = true;
            }
        }
    }

    void spread_fire(int row, int column) {
        buildingArray[row][column] = 0;
        bool flag = false;
        for (int i = 3; i >= 0; i--) {
            if (flag && buildingArray[i][column] == 0) {
                for (int fireRow = i; fireRow >= 0; fireRow--) {
                    buildingArray[fireRow][column] = 0;
                }
                return;
            }
            if (buildingArray[i][column] == 0) {
                flag = true;
            }
        }
    }

    bool check_win() {
        vector<vector<int>> win1 = {{1, 1, 1, 1, 1},
                                    {1, 1, 1, 1, 1},
                                    {1, 1, 1, 1, 1},
                                    {1, 1, 1, 1, 1}};
        vector<vector<int>> win0 = {{0, 0, 0, 0, 0},
                                    {0, 0, 0, 0, 0},
                                    {0, 0, 0, 0, 0},
                                    {0, 0, 0, 0, 0}};
        return buildingArray == win1 || buildingArray == win0;
    }
};

class Game {
private:
    Building playerOneBuilding;
    Building playerTwoBuilding;
    bool playerOneWins = false;
    bool playerTwoWins = false;
    bool playerOnesGo = true;
    bool playerTwosGo = false;
    bool gameOver = false;

public:
    void play() {
        intro();
        game_loop();
    }

    void intro() {
        cout << "Welcome to Saviour vs Scorcher\n";
        cout << "YOUR BUILDING IS ON FIRE\n";
        cout << "And so is your opponents...\n";
        cout << "You hate your opponent...\n";
        cout << "You can save your building... or destroy your opponents...\n";
        cout << "1 = Water\n";
        cout << "0 = Fire\n";
        cout << "Press enter to continue\n";
        cin.get();
        cout << "If you stack two 1's on top of each other, then the water will flow down to all rooms directly below\n";
        cout << "If you stack two 0's on top of each other, then the fire will flow up to all rooms directly above\n";
        cout << "Press enter to continue\n";
        cin.get();
        display_both_buildings();
        cout << "Press enter to continue\n";
        cin.get();
        cout << "These are the building numbers\n";
        display_building_numbers();
        cout << "Press enter to start\n";
        cin.get();
    }

    void display_both_buildings() {
        playerOneBuilding.displayBuilding();
        playerTwoBuilding.displayBuilding();
    }

    void display_building_numbers() {
        cout << "16. 17. 18. 19. 20.\n";
        cout << "11. 12. 13. 14. 15.\n";
        cout << "6. 7. 8. 9. 10.\n";
        cout << "1. 2. 3. 4. 5.\n";
    }

    void game_loop() {
        while (!playerOneWins && !playerTwoWins && !gameOver) {
            display_both_buildings();
            if (playerOnesGo) {
                take_turn(1);
                // Check if player one has won
                playerOnesGo = false;
                playerTwosGo = true;
            } else if (playerTwosGo) {
                take_turn(2);
                // Check if player two has won
                playerTwosGo = false;
                playerOnesGo = true;
            }
        }
    }

    void take_turn(int player) {
        cout << "It's player " << player << "'s turn\n";
        cout << "Press 1 to spread water in your building or press 0 to spread fire on your opponent\n";
        int waterOrFire = check_integer("Enter 1 or 0: \n");
        int roomNumber = check_integer("Which room do you chose (1-20): \n");
        int row = 0;
        int col = 0;
        tie(row, col) = update_building(roomNumber);
        if (player == 1) {
            if (waterOrFire == 1) {
                playerOneBuilding.spread_water(row, col);
            } else if (waterOrFire == 0) {
                playerTwoBuilding.spread_fire(row, col);
            }
        } else if (player == 2) {
            if (waterOrFire == 1) {
                playerTwoBuilding.spread_water(row, col);
            } else if (waterOrFire == 0) {
                playerOneBuilding.spread_fire(row, col);
            }
        }
    }

    int check_integer(string prompt) {
        int player_input;
        while (true) {
            cout << prompt;
            cin >> player_input;
            if (cin.fail()) {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cout << "**************** Invalid input ****************\n";
            } else {
                return player_input;
            }
        }
    }

    pair<int, int> update_building(int roomNumber) {
        if (roomNumber < 1 || roomNumber > 20) {
            throw invalid_argument("Invalid room number");
        }
        int row = 3 - (roomNumber - 1) / 5;
        int col = (roomNumber - 1) % 5;
        return make_pair(row, col);
    }

    void check_winner() {
        if (playerOneBuilding.check_win()) {
            gameOver = true;
            display_both_buildings();
            cout << "Player 1 wins\n";
        } else if (playerTwoBuilding.check_win()) {
            gameOver = true;
            display_both_buildings();
            cout << "Player 2 wins\n";
        }
    }
};

int main() {
    Game game;
    game.play();
    return 0;
}