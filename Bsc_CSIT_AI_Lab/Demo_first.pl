% Definitions of facts

father(john, peter).
father(john, paul).
mother(mary, peter).

% Definitions of rules

is_sibling(X,Y) :- father(Z,X), father(Z,Y), X\=Y.
is_child(X,Y) :- father(Y,X).
is_father(X,Y) :- father(X,Y).
is_mother(X,Y) :- mother(X,Y).