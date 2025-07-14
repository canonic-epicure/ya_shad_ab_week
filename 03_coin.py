from itertools import chain
import sys
import re

str = sys.stdin.read()

numbers = re.findall(r"\d+", str)

n = int(numbers[0])

# n = 5

if n == 1:
    print('0 1.0 0')
else:
    states = {
        'o' : {
            -1 : 1,
            0 : 1
        },
        'p' : {
            1 : 1,
            0 : 1
        }
    }

    for i in range(n - 2):
        new_states = {
            'o' : {},
            'p' : {}
        }
        new_states_o = new_states[ 'o' ]
        new_states_p = new_states[ 'p' ]

        for win, total in states[ 'o' ].items():
            if win - 1 in new_states_o:
                new_states_o[ win - 1 ] += total
            else:
                new_states_o[ win - 1 ] = total

            if win + 1 in new_states_p:
                new_states_p[ win + 1 ] += total
            else:
                new_states_p[ win + 1 ] = total

        for win, total in states[ 'p' ].items():
            if win in new_states_o:
                new_states_o[ win ] += total
            else:
                new_states_o[ win ] = total

            if win in new_states_p:
                new_states_p[ win ] += total
            else:
                new_states_p[ win ] = total

        states = new_states

    counter_x = 0
    counter_y = 0
    counter_n = 0

    counter_total = 0

    for win, total in chain(states[ 'o' ].items(), states[ 'p' ].items()):
        counter_total += total

        if win > 0:
            counter_x += total
        elif win < 0:
            counter_y += total
        else:
            counter_n += total

    print(counter_x / counter_total, counter_n / counter_total, counter_y / counter_total)

