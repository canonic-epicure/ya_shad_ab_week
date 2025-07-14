import random


k = 1000


right_prob = 2 / 3

zero_count = 0

steps = []

def model():
    global steps
    global zero_count

    room = 0

    step = 0

    while room < k:
        step += 1

        if room == 0:
            zero_count += 1
            room = 1
            steps.append(1)
        else:
            x = random.random()

            if (x < right_prob):
                room += 1
                steps.append('right')
            else:
                room -= 1
                steps.append('left')

    return step


print(model())

print(zero_count)

print(steps)