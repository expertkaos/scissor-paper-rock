from microbit import *
import random

MIDDLE = pin1
RING = pin2

mbaseline = MIDDLE.read_analog()
rbaseline = RING.read_analog()

SCISSOR = Image('99009:' '99090:' '00900:' '99090:' '99009:')
ROCK = Image('09990:' '99999:' '99999:' '99999:' '09990:')
PAPER = Image('99999:' '99999:' '99999:' '99999:' '99999:')
LOSE = Image('09000:' '09000:' '09000:' '09000:' '09999:')
WIN = Image('90909:' '90909:' '90909:' '90909:' '09090:')

options = ["prob", ROCK, PAPER, SCISSOR]

def read(baseline, FINGER):
    if abs(FINGER.read_analog() - baseline) > 3:
        return True
    else:
        return False

while True:

    shaken = 0
    start = 0

    while shaken < 3:
        if running_time() - start >= 5000:
            shaken = 0

        if accelerometer.is_gesture('shake'):
            shaken += 1
            start = running_time()

        sleep(500)

    ring = read(rbaseline, RING)
    middle = read(mbaseline, MIDDLE)
    computer = random.randint(1, 3)

    if ring == True and middle == True:
        player = 1
    elif ring == False and middle == False:
        player = 2
    elif ring == False and middle == True:
        player = 3
    else:
        player = 0

    display.show(options[player])
    sleep(1000)
    display.clear()
    sleep(1000)
    display.show(options[computer])
    sleep(2000)

    if player == computer:
        display.show('T')
    elif player == 1:
        if computer == 3:
            display.show(WIN)
        else:
            display.show(LOSE)
    elif player == 2:
        if computer == 1:
            display.show(WIN)
        else:
            display.show(LOSE)
    elif player == 3:
        if computer == 2:
            display.show(WIN)
        else:
            display.show(LOSE)
    else:
        display.show('error')



    sleep(5000)

