import random

def get_answers():
    answers = []
    answers_file = open("answers.txt", "r").readlines()
    for word in answers_file:
        word: str = word
        answers.append(word.strip())
    return answers
    
def main():
    print("Word Guesser!\nPlease enter any 5-letter word")
    
    
    answer_list = get_answers()
    answer = answer_list[random.randint(1, 10657)]
    guess = ""
    guesses = 6
    guesses_used = 0
    
    while guesses_used < guesses:
        if guess != answer:
            guesses_used += 1
            guess = str(input("Please input guess: "))
        else:
            print("You lose. The correct answer was " + answer + ".")
        
    if guess == answer:
        print("You Win")
    else:
        print("You lose. The correct answer was " + answer + ".")
        
main()