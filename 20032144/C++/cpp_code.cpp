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
                std::cout << building[i][j] << " ";
            }
            std::cout << std::endl;
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
        std::cout << "Player One's Building: " << std::endl;
        playerOneBuilding.displayBuilding();
        std::cout << std::endl;
        std::cout << "Player Two's Building: " << std::endl;
        playerTwoBuilding.displayBuilding();
        std::cout << std::endl;
    }

    void playGame() {
        while (true) {
            displayBothBuildings();
            std::cout << "Player One or Player Two? ";
            std::cin >> player;

            if (player == 1 || player == 2) {
                std::cout << "Press 1 to spread water in your building or press 0 to spread fire on your opponent\n";
                std::cout << "Enter 1 or 0: ";
                std::cin >> waterOrFire;
                std::cout << "Which room do you chose (1-20): ";
                std::cin >> roomNumber;
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
            std::cout << "Invalid room number\n";
        }
        row = 3 - (roomNumber - 1) / 5;
        col = (roomNumber - 1) % 5;
    }
};

int main() {
    Game gameInstance;
    gameInstance.playGame();

    return 0;
}
