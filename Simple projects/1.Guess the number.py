import random

RANGE = range(1, 101)
TRYS = 5


def guess_the_number(original_num, new_num):
    if original_num == new_num:
        return True
    return False


def hints_generator(hint, magic_num):
    current_hint = random.choice(hint)
    value = None
    if current_hint == "bigger":
        value = random.choice([x for x in range(1, magic_num)])

        if value not in RANGE or not value:
            value = 100
        return f"The magic number is bigger than {value}!"
    elif current_hint == "smaller":
        value = random.choice([x for x in range(magic_num + 1, magic_num + 15)])
        if value not in RANGE or not value:
            value = 1
        return f"The magic number is smaller than {value}!"
    elif current_hint == 'divide':
        divisible = []
        for i in range(2, 10):
            if magic_num % i == 0:
                divisible.append(i)
        if not divisible:
            return hints_generator(hint, magic_num)
        return f"The magic number is divisible by {random.choice(divisible)}."
    elif current_hint == "between":
        upper_limit = magic_num + 15
        lower_limit = magic_num - 5
        if upper_limit > 100:
            upper_limit = 100
        elif lower_limit <= 0:
            lower_limit = 1
            return f"The magic number is somewhere between {lower_limit} and {upper_limit}."
    elif current_hint == "not_divisible":
        not_divisible = []
        for i in range(2, 10):
            if magic_num % i != 0:
                not_divisible.append(i)
        if not not_divisible:
            return hints_generator(hint, magic_num)
        return f"The magic number is not divisible by {random.choice(not_divisible)}."


# generate number
print("Can you guess the number?")

random_num = random.randint(1, 100)
hints = ["bigger", "smaller", "between", "divide", "not_divisible"]
guessed_num = None
steps = 0

while True:
    guess_number = input("Try your luck! Choose a number between 1 and 100! : ")
    if guess_number.isdigit() and int(guess_number) in RANGE:
        guess_number = int(guess_number)
        steps += 1
        if guess_the_number(random_num, guess_number):
            print("Your sixth sense is working! Congratulations!")
            print(f"You got it in {steps} steps! ")
            guessed_num = guess_number
            break
        elif steps == TRYS:
            print("You ran out of luck!")
            break

        else:
            new_answer = input(
                f"You guessed wrong, young one. You have {TRYS - steps} trys left, do you want a hint? (Y/N): ")
            while new_answer != "Y" and new_answer != "N":
                print("Choose Y or N for answer!")
                new_answer = input()
            if new_answer == "Y":
                print(hints_generator(hints,  random_num))
                continue
            continue
    else:
        print("Please choose an integer between 1 and 100.")
