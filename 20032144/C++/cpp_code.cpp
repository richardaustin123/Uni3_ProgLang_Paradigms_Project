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

private:
    int building[4][5];
};

class Game {
private:
    Building playerOneBuilding;
    Building playerTwoBuilding;

public:
    int player;
    int roomNumber, row, col;
    int waterOrFire;

    void displayBothBuildings() {
        cout << "Player One's Building: " << endl;
        playerOneBuilding.displayBuilding();
        cout << endl;
        cout << "Player Two's Building: " << endl;
        playerTwoBuilding.displayBuilding();
        cout << endl;
    }

    void gameLoop() {
        while (true) {
            displayBothBuildings();
            cout << "Player One or Player Two? ";
            cin >> player;

            if (player == 1 || player == 2) {
                cout << "Press 1 to spread water in your building or press 0 to spread fire on your opponent\n";
                cout << "Enter 1 or 0: ";
                cin >> waterOrFire;
                cout << "Which room do you chose (1-20): ";
                cin >> roomNumber;
                get_row_col(roomNumber, row, col);

                if (player == 1 && waterOrFire == 1) {
                    playerOneBuilding.updateBuilding(row, col, waterOrFire);
                } else if (player == 1 && waterOrFire == 0) {
                    playerTwoBuilding.updateBuilding(row, col, waterOrFire);
                } else if (player == 2 && waterOrFire == 1) {
                    playerTwoBuilding.updateBuilding(row, col, waterOrFire);
                } else if (player == 2 && waterOrFire == 0) {
                    playerOneBuilding.updateBuilding(row, col, waterOrFire);
                }
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
