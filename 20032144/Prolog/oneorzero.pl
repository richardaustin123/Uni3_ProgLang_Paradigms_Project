% chose_fire_or_water :-
%     format('~nPress 1 for water or 0 for fire: ~n'),
%     read(FireOrWater),
%     format('You chose ~w~n', [FireOrWater]),
%     check_one_or_zero(FireOrWater).

% % If player doesnt enter 1 or 0, the first chose_fire_or_water will fail and will try again here
% % Which tells the player they inputted wrong and loops back to the first chose_fire_or_water
% chose_fire_or_water :-
%     format('~nIncorrect input~n'),
%     chose_fire_or_water.

% %! check_one_or_zero(+FireOrWater)
% % Check if player inputs 1 or 0 on the attempt below 
% % If fail, the first instant of chose_fire_or_water will run the fail case above
% check_one_or_zero(1) :- !.

% % Check if player inputs 0
% check_one_or_zero(0) :- !.


whatnumber :- 
    format('Start'),
    oneOrZero(Number),
    format('You chose ~w', [Number]).

oneOrZero(Number) :-
    format("Choose 1 or 0: "),
    get_char(InputChar),
    atom_number(InputChar, Number),
    check_one_or_zero(Number).

oneOrZero(Number) :-
    format("Incorrect input~n"),
    oneOrZero(Number).

% %! check_one_or_zero(+FireOrWater)
% Check if player inputs 1 or 0 on the attempt below 
% If fail, the first instant of chose_fire_or_water will run the fail case above
check_one_or_zero(1) :- !.

% % Check if player inputs 0
check_one_or_zero(0) :- !.

    % (InputChar = '1' ; InputChar = '0')

:- whatnumber.
