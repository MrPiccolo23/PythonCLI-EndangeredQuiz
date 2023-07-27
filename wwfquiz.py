import random
import time
import sys
import os
# ------------------------------------------------------------------------------------------
os.system("cls")
answer = []
ans_no = 0
keys = 0

def game():
    print("Welcome to the WWF Endangered Species Quiz!")
    time.sleep(2)
    print("The Endangered Animals desperately need your help! Poachers have captured and hidden them!!")
    time.sleep(3)
    print("If you can help remember what animals they are, we can use your magic knowledge to discover the keys needed to set them free from the rotten poachers!")
    time.sleep(2)
    print("Before each question you will roll a dice, once you roll an even number, you will be presented with a clue to help you guess the type of endangered animal!")
    time.sleep(4)
    Player = input("Press Enter to Play the WWF Quiz")
    time.sleep(2)
    # ------------------------------------------------------------------------------------------
    questions = [
        "Do you know who I am?",
        "Can you guess yet?",
        "Any ideas who I could be?",
        "WHO AM I??",
        "What could I be?",
        "What am I?",
        "Any guesses as to what I am?",
        "What could I be?",
        "Any big guesses?",
        "WHO could I be?",
        " "
    ]
    clues = [
        "For more than 100 million years we have covered vast distances across the world's oceans. We also have hard shells.",
        "An estimated 3,900 of us remain in the wild. We also have stripes, big claws and whiskers.",
        "We can reach lengths of more than 100 feet and weigh up to 200 tons. At the depths we communicate with complex and mysterious sounds.",
        "We live in forests high in the mountains, at elevations of 8,000 to 13,000 feet. Featured in a film called King Kong once or twice.",
        "We are social and gather in packs of around ten individuals, some packs number more than 40. Mans best friend, except wild! ",
        "Known for our distinctive red fur spending most of our time in trees. We share 96.4 percent of our genes with you humans and are highly intelligent creatures. ",
        "Our name is said to come from the Nepali word 'ponya,' which means bamboo or plant eating animal. We are the giant members of our family.",
        "Panthera native to the mountain ranges of Central and South Asia. We like snow and hide well with our markings. ",
        "We are the largest surviving land mammal in Asia. We knock down trees with our tusks but can also pick up something as small as a peanut.",
        "In 1938 a bird population survey was conducted, only 29 of us remained in the wild. We are slim and know for our whooping sounds."
    ]
    correct_answers = [
        "SEA TURTLE",
        "TIGER",
        "BLUE WHALE",
        "MOUNTAIN GORILLA",
        "WILD DOG",
        "ORANGUTAN",
        "GIANT PANDA",
        "SNOW LEOPARD",
        "ASIAN ELEPHANT",
        "WHOOPING CRANE"
    ]
    # ------------------------------------------------------------------------------------------
    def roll_dice():
        roll_again = input("\nPress Enter to roll the dice..")
        if roll_again == "":
            time.sleep(2)
            dice = random.randint(1, 6)
            print("\n" * 20)
            print("Your number is....{}".format(dice))
            print("---------------------------------------------")
            if ans_no < 10:
                if dice % 2 == 0:
                    question_func()
                else:
                    print("You Rolled odd! Try again!")
                    roll_dice()
            else:
                attenborough()
        else:
            print("You pressed wrong key before Enter!")
            roll_dice()
    # ------------------------------------------------------------------------------------------
    def question_func():
        global ans_no, keys, answer
        print_slow(f"You Rolled Even!\nClue: {clues[ans_no]}\n")
        print_slow(questions[ans_no])
        print()
        guess = input("Enter answer: ")
        guess = guess.upper()
        answer = correct_answers[ans_no]
        if answer == guess:
            print("Well done, you've gained a Key!")
            keys += 1
            time.sleep(2)
        else:
            print("WRONG!")
            print(f"The correct answer is: {correct_answers[ans_no]}")
            time.sleep(2)
        ans_no += 1
        if ans_no < 10:
            roll_dice()
        else:
            attenborough()
            ans_no = 0

    # ------------------------------------------------------------------------------------------
    def attenborough():
        print("\n" * 100)
        print_slow("Hello explorer! Sir David Attenborough here!!")
        print_slow(
            "We hope you enjoyed our WWF quiz in hope of raising awareness of just a few animals due to become extinct without our help")
        print_slow(
            "If we can understand who we need to help and why, we can begin to make a change in the world we share")
        time.sleep(1)
        print("Do you have 5 Keys?")
        time.sleep(2)
        print("\n" * 100)
        if keys >= (5):
            print("---------------------------------------------")
            print("CONGRATULATIONS YOU HAVE RELEASED THE ENDANGERED ANIMALS!!")
        else:
            print("---------------------------------------------")
            print("OH NO!! WE WILL HAVE TO SEND BIG DAVE!!")
            time.sleep(2)

    roll_dice()

# ------------------------------------------------------------------------------------------
# How fast you want the time in between letters to be (stands for "sleep time"
st = 0.07
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(st)
# ------------------------------------------------------------------------------------------
def play_again():
    response = input("Play again? (Y or N): ")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False
game()

# ------------------------------------------------------------------------------------------
while play_again():
    game()
print("Goodbye for now!")
# ------------------------------------------------------------------------------------------