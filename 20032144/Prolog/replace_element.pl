% replace(RoomIndex, Building, ReplaceWith, NewBuilding) :-
%     format('List: ~w~n', [Building]),
%     nth0(RoomIndex, Building, _, ReplaceThis),
%     nth0(RoomIndex, NewBuilding, ReplaceWith, ReplaceThis).

% :- replace(2, [1, 2, 3, 4, 5], 10, NewBuilding), format('List: ~w~n', [NewBuilding]).

% replace([RowIndex, ColIndex], Building, ReplaceWith, NewBuilding) :-
%     replace_in_row(RowIndex, ColIndex, Building, ReplaceWith, NewBuilding).

% % Helper predicate to replace the value at RowIndex, ColIndex in a row
% replace_in_row(0, ColIndex, [Row|Rest], ReplaceWith, [NewRow|Rest]) :-
%     replace_in_col(ColIndex, Row, ReplaceWith, NewRow).
% replace_in_row(RowIndex, ColIndex, [Row|Rest], ReplaceWith, [Row|NewRest]) :-
%     RowIndex > 0,
%     NextRowIndex is RowIndex - 1,
%     replace_in_row(NextRowIndex, ColIndex, Rest, ReplaceWith, NewRest).

% % Helper predicate to replace the value at ColIndex in a list
% replace_in_col(0, [_|Rest], ReplaceWith, [ReplaceWith|Rest]).
% replace_in_col(ColIndex, [X|Rest], ReplaceWith, [X|NewRest]) :-
%     ColIndex > 0,
%     NextColIndex is ColIndex - 1,
%     replace_in_col(NextColIndex, Rest, ReplaceWith, NewRest).

% :- replace([1, 1], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10, NewBuilding), format('Building: ~w~n', [NewBuilding]).

% Base case: If we're on the bottom row, stop spreading water
% spread_water(Building, Row, Col, Building) :-
%     check_already_on_bottom_row(Row).


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

buildingOne([   [0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0]]).

buildingTwo([   [1, 0, 0], 
                [1, 0, 0], 
                [1, 0, 0], 
                [1, 0, 0]]).

% Test cases
test :-
    buildingOne(BuildingOne),
    buildingTwo(BuildingTwo),
    format('BuildingOne before: ~w~n', [BuildingOne]),
    spread_water(BuildingOne, 1, 1, NewBuilding), format('BuildingOne after: ~w~n', [NewBuilding]),
    format('BuildingTwo before: ~w~n', [BuildingTwo]),
    spread_fire(BuildingTwo, 3, 0, BrandNewBuilding), format('BuildingTwo after: ~w~n', [BrandNewBuilding]).
    
:- test.

% :-  spread_water([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1, NewBuilding), format('Building: ~w~n', [NewBuilding]),
%     spread_fire([[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]], 3, 0, BrandNewBuilding), format('Building: ~w~n', [BrandNewBuilding]).