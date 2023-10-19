% consult('/Users/richardaustin/Documents/GitHub/Uni3_ProgLang_Paradigms_Project/20032144/Prolog/allonestest.pl').

% Predicate to check if a list contains all 1's.
% Check if a list contains all ones
contains_all_ones([]).
contains_all_ones([1 | Rest]) :- 
    contains_all_ones(Rest).

% Check if a matrix contains all ones
matrix_contains_all_ones([]).
matrix_contains_all_ones([Row | Rest]) :-
    contains_all_ones(Row),
    matrix_contains_all_ones(Rest).

contains_all_zeros([]).
contains_all_zeros([0 | Rest]) :- 
    contains_all_zeros(Rest).

% Check if a matrix contains all zeros
matrix_contains_all_zeros([]).
matrix_contains_all_zeros([Row | Rest]) :-
    contains_all_zeros(Row),
    matrix_contains_all_zeros(Rest).

% Predicate to check if a matrix contains all 1's or all 0's.
checkArray(Matrix) :-
    (matrix_contains_all_ones(Matrix) ->
        format('Winner: All 1s\n');
    matrix_contains_all_zeros(Matrix) ->
        format('Winner: All 0s\n');
    true).

% Example usage:
% Define a matrix, and then call checkArray to check if it contains all 1's or all 0's.
matrix1([[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]).

matrix2([[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]).

matrix3([[1, 0, 1],
         [0, 1, 0],
         [1, 0, 1]]).

playerOneBuilding([[ 0, 0, 0, 0, 0],    % 16. 17. 18. 19. 20. 
                   [ 0, 0, 0, 0, 0],    % 11. 12. 13. 14. 15.
                   [ 0, 0, 0, 0, 0],    % 6.  7.  8.  9.  10.
                   [ 0, 0, 0, 0, 0]]).   % 1.  2.  3.  4.  5.

:- matrix1(Matrix), checkArray(Matrix).
:- matrix2(Matrix), checkArray(Matrix).
:- matrix3(Matrix), checkArray(Matrix).
:- playerOneBuilding(P1Building), format('P1 building'), checkArray(P1Building).
