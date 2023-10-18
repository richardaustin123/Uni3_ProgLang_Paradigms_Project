% consult('/Users/richardaustin/Documents/GitHub/Uni3_ProgLang_Paradigms_Project/20032144/Prolog/prolog_code.pl').

hello_world :- 
    format('Hello World!~n').


% Player one building array
playerOneBuilding([[ 1, 0, 0, 0, 1],    % 16. 17. 18. 19. 20. 
                   [ 0, 1, 0, 1, 0],    % 11. 12. 13. 14. 15.
                   [ 0, 1, 0, 1, 0],    % 6.  7.  8.  9.  10.
                   [ 0, 0, 1, 0, 0]]).   % 1.  2.  3.  4.  5.

% Player two building array
playerTwoBuilding([[ 1, 0, 0, 0, 1],    % 16. 17. 18. 19. 20. 
                   [ 0, 1, 0, 1, 0],    % 11. 12. 13. 14. 15.
                   [ 0, 1, 0, 1, 0],    % 6.  7.  8.  9.  10.
                   [ 0, 0, 1, 0, 0]]).   % 1.  2.  3.  4.  5.

% play/0
play :-
    intro,
    game_loop.

% intro/0
% Into the game
intro :-
    format('~nYOUR BUILDING IS ON FIRE~n'),
    format('And so is your opponents...~n'),
    format('You hate your opponet...~n'),
    format('You can save your building... or destroy your opponents...~n'),
    format('1 = Water~n'),
    format('0 = Fire~n'),
    format('Press enter to start~n'),
    display_both_buildings,
    format('Press enter to continue~n'),
    format('These are the building numbers~n'),
    display_building_numbers,
    format('~nPress enter to continue~n').

% display_building_numbers/0
display_building_numbers :-
    format('~n 16.  17.  18.  19.  20.~n'),
    format(' 11.  12.  13.  14.  15.~n'),
    format(' 6.   7.   8.   9.   10.~n'),
    format(' 1.   2.   3.   4.   5.~n').

% game_loop/0
game_loop :-
    format('~nLets begin~n').
    % display_both_buildings.

% display_both_buildings/0
% Print the building of both players
display_both_buildings :-
    playerOneBuilding(PlayerOneBuilding),   % Set player one building array
    playerTwoBuilding(PlayerTwoBuilding),   % Set player two building array
    format('~nPlayer One Building:~n'),     
    display_building(PlayerOneBuilding),    % Print player one building
    format('~nPlayer Two Building:~n'),
    display_building(PlayerTwoBuilding).    % Print player two building

% display_building(+buildingArray)
% Print the building recursively by looping through each row
display_building([]).

display_building([BuildingFloor | RemainingFloors]) :-
    print_row(BuildingFloor),               % Print the current row
    nl,                                     % New line
    display_building(Rest).                 % Loop back to print the remaining rows in the building

% print_row(+row)
% Print a row of the building recursively by looping through each element (room number)
print_row([]).

print_row([RoomNumber | RemainingRooms]) :-
    write(RoomNumber),                      % Print the room number
    write(' '),                             % Print a space between the room number 
    print_row(RemainingRooms).              % Loop back to print the rest of the numebr in the row


:- play.