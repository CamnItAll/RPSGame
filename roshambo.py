import sys, random, time

def point_you():
    global score_you # "global" lets you use variables from outside a def
    score_you += 1
    print("This point goes to you!")
    time.sleep(1)
def point_me():
    global score_me
    score_me += 1
    print("This point goes to me!")
    time.sleep(1)
def tied(result):
    if result == 'r':
        print("""
            _______                          _______
        ---'   ____)                        (____   '___
              (_____)                      (_____)
              (_____)                      (_____)
              (____)                        (____)
        ---.__(___)                          (___)__.---
        """)
    elif result == 'p':
        print("""
            ________                        _______
        ---'    ____)____              ____(____    '___
                   ______)            (______
                  _______)            (_______
                 _______)              (_______
        ---.__________)                  (__________.---
        """)
    elif result == 's':
        print("""
            ________                         ________
        ---'    ____)____               ____(____    '___
                   ______)             (______
               __________)             (__________
              (____)                         (____)
        ---.__(___)                           (___)__.---
        """)

#############################################################################

print("Let's play a game of ro-sham-bo.")
time.sleep(1)
print("First to 10 points wins.")
time.sleep(1)

score_you = 0
score_me = 0

while True: #Main game loop
    print("Score\nYou: %s\nMe: %s" % (score_you, score_me))
    time.sleep(1)
    # %s offers another way of adding variables to the string.
    # Anyway...

    # Win/Lose Conditions
    if score_you == 10:
        print("You win!")
        time.sleep(1)
        break
    if score_me == 10:
        print("You lose!")
        time.sleep(1)
        break

    # Player input loop
    while True:
        print("Make your move...\n(r)ock, (p)aper, (s)cissors, or e(x)it.")
        your_move = input(">")
        if your_move == 'x':
            print("Well, FUCK you then!")
            time.sleep(1)
            sys.exit()
        if your_move == 'r' or your_move == 'p' or your_move == 's':
            break # Go to the output section.
        print("A- *hem*.")

    move_num = random.randint(1, 3)
    # 1 = Rock, 2 = Paper, 3 = Scissors.
    if move_num == 1:
        my_move = 'r'
    elif move_num == 2:
        my_move = 'p'
    elif move_num == 3:
        my_move = 's'

    print("ROCK!")
    time.sleep(0.5)
    print("PAPER!")
    time.sleep(0.5)
    print("SCISSORS!")
    time.sleep(0.5)
    print("SHOOT!")

    # The output section
    if your_move == my_move:
        tied(your_move)
        time.sleep(1)
        print("It's a tie.")
        time.sleep(1)
    elif your_move == 'r' and my_move == 's':
        # Note: Triple quotes lets you write multiple string lines!
        print("""
            _______                         ________
        ---'   ____)                   ____(____    '___
              (_____)                 (______
              (_____)                 (__________
              (____)                        (____)
        ---.__(___)                          (___)__.---
        """)
        time.sleep(1)
        point_you()
    elif your_move == 'p' and my_move == 'r':
        print("""
            ________                         _______
        ---'    ____)____                   (____   '___
                   ______)                 (_____)
                  _______)                 (_____)
                 _______)                   (____)
        ---.__________)                      (___)__.---
        """)
        time.sleep(1)
        point_you()
    elif your_move == 's' and my_move == 'p':
        print("""
            ________                        ________
        ---'    ____)____              ____(____    '___
                   ______)            (______
               __________)            (_______
              (____)                   (_______
        ---.__(___)                      (__________.---
        """)
        time.sleep(1)
        point_you()
    elif your_move == 'r' and my_move == 'p':
        print("""
            _______                         ________
        ---'   ____)                   ____(____    '___
              (_____)                 (______
              (_____)                 (__________
              (____)                   (_______
        ---.__(___)                      (__________.---
        """)
        time.sleep(1)
        point_me()
    elif your_move == 'p' and my_move == 's':
        print("""
            ________                        _______
        ---'    ____)____              ____(____    '___
                   ______)            (______
                  _______)            (__________
                 _______)                   (____)
        ---.__________)                      (___)__.---
        """)
        time.sleep(1)
        point_me()
    elif your_move == 's' and my_move == 'r':
        print("""
            ________                         _______
        ---'    ____)____                   (____   '___
                   ______)                 (_____)
               __________)                 (_____)
              (____)                        (____)
        ---.__(___)                          (___)__.---
        """)
        time.sleep(1)
        point_me()
    time.sleep(1)
