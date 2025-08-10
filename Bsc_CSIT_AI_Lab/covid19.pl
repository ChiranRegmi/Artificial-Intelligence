start :-
    write('COVID-19 Expert System'), nl,
    write('Answer with yes. or no.'), nl,

    ask('Do you have a fever?', Fever),
    ask('Do you have a cough?', Cough),
    ask('Do you have a sore throat?', Throat),
    ask('Have you lost your sense of taste or smell?', TasteLoss),

    (
        Fever = yes,
        Cough = yes,
        Throat = yes,
        TasteLoss = yes
    ->
        write('You may have COVID-19. Please consult a doctor.')
    ;
        write('You are unlikely to have COVID-19. Stay safe.')
    ), nl.

ask(Question, Answer) :-
    write(Question), nl,
    read(Answer).
