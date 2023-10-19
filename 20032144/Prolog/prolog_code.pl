% consult('/Users/richardaustin/Documents/GitHub/Uni3_ProgLang_Paradigms_Project/20032144/Prolog/prolog_code.pl').

hello_world :- 
    format('Hello World!~n').


% Player one building array
playerOneBuilding([[ 0, 0, 0, 0, 0],    % 16. 17. 18. 19. 20. 
                   [ 0, 0, 0, 0, 0],    % 11. 12. 13. 14. 15.
                   [ 0, 0, 0, 0, 0],    % 6.  7.  8.  9.  10.
                   [ 0, 0, 0, 0, 0]]).   % 1.  2.  3.  4.  5.

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
    get_char(_), % User input "_" as we dont care about the input here, no need for a variable 
    display_both_buildings,
    format('Press enter to continue~n'),
    get_char(_),
    format('~nThese are the building numbers~n'),
    display_building_numbers,
    format('~nPress enter to continue~n'),
    get_char(_).

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
    playerOneBuilding(PlayerOneBuilding),
    playerTwoBuilding(PlayerTwoBuilding),
    check_winner(PlayerOneBuilding, PlayerTwoBuilding), !,
    display_both_buildings, 
    format('~nAyup~n').

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Check winner %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%! check_winner(+PlayerOneBuilding, +PlayerTwoBuilding)
% Check if player one has won 
% If fail, check_winner will run the next attempt below, for p2
check_winner(PlayerOneBuilding, PlayerTwoBuilding) :-
    check_player_one_win(PlayerOneBuilding, PlayerTwoBuilding),
    format('Player 1 wins~n'), !.

% Check if player two has won
% If fail, check_winner will fail and the game will continue on the next attempt
check_winner(PlayerOneBuilding, PlayerTwoBuilding) :-
    check_player_two_win(PlayerOneBuilding, PlayerTwoBuilding),
    format('Player 2 wins~n'), !.

% If neither player has won, the game will continue
check_winner(_PlayerOneBuilding, _PlayerTwoBuilding) :- !.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Check player win %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%! check_player_one_win(+PlayerOneBuilding, +PlayerTwoBuilding)
% Check if player one has won by extinguishing their own building 
check_player_one_win(PlayerOneBuilding, _PlayerTwoBuilding) :-
    building_extinguished(PlayerOneBuilding).

% Check if player one has won by burning down their opponents building
check_player_one_win(_PlayerOneBuilding, PlayerTwoBuilding) :-
    building_in_flames(PlayerTwoBuilding).

%! check_player_two_win(+PlayerOneBuilding, +PlayerTwoBuilding)
% Check if player two has won by extinguishing their own building
check_player_two_win(_PlayerOneBuilding, PlayerTwoBuilding) :-
    building_extinguished(PlayerTwoBuilding).

% Check if player two has won by burning down their opponents building
check_player_two_win(PlayerOneBuilding, _PlayerTwoBuilding) :-
    building_in_flames(PlayerOneBuilding).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Building put out or on fire %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%! is_room_water(+buildingArray)
% Check if building is all 1's (water)
is_room_water([]).                          % Base case
is_room_water([1 | Rest]) :-                % If the current room is 1 (water)
    is_room_water(Rest).                    % Loop back to check the rest of the building

% Check if a matrix contains all ones
building_extinguished([]).                  % Base case
building_extinguished([Row | Rest]) :-      % Separate the matrix (building) into the current row and the rest of the matrix
    is_room_water(Row),                     % Check if the current row is all 1's (water)
    building_extinguished(Rest).            % Loop back to check the rest of the building

%! is_room_fire(+buildingArray)
% Check if building is all 0's (fire)
is_room_fire([]).                           % Same as above but for 0's (fire)
is_room_fire([0 | Rest]) :- 
    is_room_fire(Rest).

% Check if a matrix contains all ones
building_in_flames([]).
building_in_flames([Row | Rest]) :-
    is_room_fire(Row),
    building_in_flames(Rest).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Take turn %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%! take_turn(+PlayerOneBuilding, +PlayerTwoBuilding)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Start game %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:- play.