:- dynamic(current_turn/1).
current_turn(1).

buildingOne([   [ 1, 0, 0, 0, 1],    % 16. 17. 18. 19. 20. 
                [ 0, 1, 0, 1, 0],    % 11. 12. 13. 14. 15.
                [ 0, 1, 0, 1, 0],    % 6.  7.  8.  9.  10.
                [ 0, 0, 1, 0, 0]]).   % 1.  2.  3.  4.  5.

buildingTwo([   [ 1, 0, 0, 0, 0],    % 16. 17. 18. 19. 20. 
                [ 1, 0, 0, 0, 0],    % 11. 12. 13. 14. 15.
                [ 1, 0, 0, 0, 0],    % 6.  7.  8.  9.  10.
                [ 1, 0, 0, 0, 0]]).   % 1.  2.  3.  4.  5.

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
    format('Press enter to numbers~n'),
    get_char(_), % User input "_" as we dont care about the input here, no need for a variable 
    format('If you stack two 1s on top of each other, then the water will flow down to all rooms directly below\n'),
    format('If you stack two 0s on top of each other, then the fire will flow up to all rooms directly above\n'),
    format('Press enter to continue~n'),
    get_char(_),
    display_both_buildings,
    format('Press enter to continue~n'),
    get_char(_),
    format('~nThese are the building numbers~n'),
    display_building_numbers,
    format('~nPress enter to start~n'),
    get_char(_).

% display_both_buildings/0
% Print the building of both players
display_both_buildings :-
    buildingOne(BuildingOne),
    buildingTwo(BuildingTwo),
    format('~nPlayer One Building:~n'),     
    display_building(BuildingOne),    % Print player one building
    format('~nPlayer Two Building:~n'),
    display_building(BuildingTwo).    % Print player two building

% display_building(+buildingArray)
% Print the building recursively by looping through each row
display_building([]).

display_building([BuildingFloor | RemainingFloors]) :-
    print_row(BuildingFloor),               % Print the current row
    nl,                                     % New line
    display_building(RemainingFloors).                 % Loop back to print the remaining rows in the building

%! print_row(+row)
% Print a row of the building recursively by looping through each element (room number)
print_row([]).

print_row([RoomNumber | RemainingRooms]) :-
    write(RoomNumber),                      % Print the room number
    write(' '),                             % Print a space between the room number 
    print_row(RemainingRooms).              % Loop back to print the rest of the numebr in the row

% display_building_numbers/0
display_building_numbers :-
    format('~n 16.  17.  18.  19.  20.~n'),
    format(' 11.  12.  13.  14.  15.~n'),
    format(' 6.   7.   8.   9.   10.~n'),
    format(' 1.   2.   3.   4.   5.~n').

% game_loop/0
game_loop :-
    format('~nLets begin~n'),
    buildingOne(BuildingOne),
    buildingTwo(BuildingTwo),
    display_both_buildings, 
    % check_winner(BuildingOne, BuildingTwo), !,
    whos_turn(Player),
    take_turn(Player, BuildingOne, BuildingTwo).

game_loop :-
    game_loop.

% Test cases
test :-
    buildingOne(BuildingOne),
    buildingTwo(BuildingTwo),
    whos_turn(Player),
    take_turn(Player, BuildingOne, BuildingTwo).

%! whos_turn(-Player)
% Check whos turn it is
whos_turn(Player) :-
    current_turn(Player),               % Get the current player from memory
    switch_turn.                        % Switch the player

%! switch_turn
switch_turn :-
    retract(current_turn(Player)),      % Retract the current player from memory
    NextPlayer is 3 - Player,           % Switch between 1 and 2 
    assert(current_turn(NextPlayer)).   % Assert (store) the new player to memory

take_turn(Player, BuildingOne, BuildingTwo) :-
    format('~nIts player ~ws turn~n', [Player]),
    format('BuildingOne before: ~w~n', [BuildingOne]),
    format('BuildingTwo before: ~w~n', [BuildingTwo]),
    format('Input 0 to spread fire and 1 to spead water: ~n'),
    get_char(FireOrWaterChar),
    format('~nPress enter~n'),
    get_char(_),
    atom_number(FireOrWaterChar, FireOrWater),
    get_char(_),
    format('~nChoose a room to spread to: ~n'),
    get_char(RoomNumberChar),
    atom_number(RoomNumberChar, RoomNumber),
    update_building(RoomNumber, Row, Col),
    player_turn(FireOrWater, BuildingOne, BuildingTwo, Row, Col),
    display_both_buildings.
    % spread_water(BuildingOne, 1, 1, NewBuilding), format('BuildingOne after: ~w~n', [NewBuilding]),
    % spread_fire(BuildingTwo, 3, 0, BrandNewBuilding), format('BuildingTwo after: ~w~n', [BrandNewBuilding]).

chose_fire_or_water(FireOrWater) :-
    format('Input 0 to spread fire and 1 to spead water: ~n'),
    get_char(FireOrWaterChar),
    atom_number(FireOrWaterChar, FireOrWater).

chose_room_number(RoomNumber) :-
    format('~nChoose a room to spread to: ~n'),
    get_char(RoomNumberChar),
    atom_number(RoomNumberChar, RoomNumber).

update_building(RoomNumber, Row, Col) :-
    Row is 3 - (RoomNumber - 1) // 5,
    Col is (RoomNumber - 1) mod 5.

player_turn(0, _, BuildingTwo, Row, Col) :-
    spread_fire(BuildingTwo, Row, Col, BrandNewBuilding),
    format('~nBuildingTwo after: ~w~n', [BrandNewBuilding]).

player_turn(1, BuildingOne, _, Row, Col) :-
    spread_water(BuildingOne, Row, Col, NewBuilding),
    format('~nBuildingOne after: ~w~n', [NewBuilding]).

% If on the bottom row, this predicate will run and replace only the room they chose
spread_water(Building, Row, Col, NewBuilding) :-
    check_already_on_bottom_row(Row),
    replace([Row, Col], Building, 1, NewBuilding).

% Recursive case: Spread water to the room below and continue recursion
spread_water(Building, Row, Col, NewBuilding) :-
    not(check_already_on_bottom_row(Row)), % Check if we're not on the bottom row
    replace([Row, Col], Building, 1, IntermediateBuilding), % Spread water to the current room
    NextRow is Row + 1,
    spread_water(IntermediateBuilding, NextRow, Col, NewBuilding).


%! check_already_on_bottom_row(+Row)
% Check if the room is on the bottom row
% Cant spread water down if already on the bottom row
check_already_on_bottom_row(Row) :-
    Row = 3.

%! replace(+[RowIndex, ColIndex], +Building, +ReplaceWith, -NewBuilding)
replace([RowIndex, ColIndex], Building, ReplaceWith, NewBuilding) :-
    replace_in_row(RowIndex, ColIndex, Building, ReplaceWith, NewBuilding).

%! replace_in_row(+RowIndex, +ColIndex, +Building, +ReplaceWith, -NewBuilding)
replace_in_row(0, ColIndex, [Row|Rest], ReplaceWith, [NewRow|Rest]) :-
    replace_in_col(ColIndex, Row, ReplaceWith, NewRow).

replace_in_row(RowIndex, ColIndex, [Row|Rest], ReplaceWith, [Row|NewRest]) :-
    RowIndex > 0,
    NextRowIndex is RowIndex - 1,
    replace_in_row(NextRowIndex, ColIndex, Rest, ReplaceWith, NewRest).

%! replace_in_col(+ColIndex, +Row, +ReplaceWith, -NewRow)
replace_in_col(0, [_|Rest], ReplaceWith, [ReplaceWith|Rest]).

replace_in_col(ColIndex, [X|Rest], ReplaceWith, [X|NewRest]) :-
    ColIndex > 0,
    NextColIndex is ColIndex - 1,
    replace_in_col(NextColIndex, Rest, ReplaceWith, NewRest).

%! spread_fire(+Building, +Row, +Col, -NewBuilding)
spread_fire(Building, Row, Col, NewBuilding) :-
    check_already_on_top_row(Row),
    replace([Row, Col], Building, 0, NewBuilding).

spread_fire(Building, Row, Col, NewBuilding) :-
    not(check_already_on_top_row(Row)),
    replace([Row, Col], Building, 0, TempBuilding),
    NextRow is Row - 1,
    spread_fire(TempBuilding, NextRow, Col, NewBuilding).

%! check_already_on_top_row(+Row)
check_already_on_top_row(Row) :-
    Row = 0.

    
:- play.

% :-  spread_water([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1, NewBuilding), format('Building: ~w~n', [NewBuilding]),
%     spread_fire([[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]], 3, 0, BrandNewBuilding), format('Building: ~w~n', [BrandNewBuilding]).
