import random
import csv

def generate_syllable():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrst'
    
    # Generating a syllable in the form of CVC
    syllable = random.choice(consonants) + random.choice(vowels) + random.choice(consonants)
    
    return syllable

def generate_word(num_syllables):
    syllables = [generate_syllable() for _ in range(num_syllables)]
    
    # Shuffling the syllables to create the final word
    random.shuffle(syllables)
    
    return ''.join(syllables)

def survey():
    answers = {}
    
    answers["Are you a native English speaker?"] = input("Are you a native English speaker? ")
    answers["Is English your second language?"] = input("Is English your second language? ")
    answers["Did you like the generated results?"] = input("Did you like the generated results? ")
    answers["Pick another word you would have chosen."] = input("Pick another word you would have chosen. ")
    answers["Would you ever use the word you selected with your peers?"] = input("Would you ever use the word you selected with your peers? ")
    answers["Define the word. What do you think it's associated with?"] = input("Define the word. What do you think it's associated with? ")
    
    return answers

def save_survey(all_answers, file_name="Memepotent Research Survey Answers.csv"):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Answer"])
        for question, answer in all_answers.items():
            writer.writerow([question, answer])
    print(f"Survey answers saved to {file_name}")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'sure', 'ya', 'ye', 'y']:
            return True
        elif response in ['no', 'nah', 'nou', 'n']:
            return False
        else:
            print("Sorry, but that's an invalid input. Please try again.")

def main():
    all_answers = {}

    # Collecting the user's name
    name = input("Your Name: ")
    all_answers["Name"] = name

    print(f"Hi, {name}! This program aims to help you find the next big meme-able word.")
    try_program = get_yes_no_input("Would you like to give it a try? (yes/no): ")
    all_answers["Try Program"] = "yes" if try_program else "no"

    if not try_program:
        print("Thank you! Have a great day.")
        return

    # Asking the user for the number of syllables per word
    num_syllables = int(input("How many syllables per word? "))
    all_answers["Number of syllables per Word"] = num_syllables
    
    # Asking the user for the number of words to generate
    num_words = int(input("How many words would you like to generate? "))
    all_answers["Number of words to Generate"] = num_words
    
    # Generating the words
    words = [generate_word(num_syllables) for _ in range(num_words)]
    
    # Printing the generated words
    for i, word in enumerate(words, 1):
        print(f"Word {i}: {word}")

    # Asking the user to select a word from the list
    word_choice = int(input(f"Which word (1-{num_words}) would you like to use in a sentence? ")) - 1
    selected_word = words[word_choice]
    all_answers["Selected Word"] = selected_word

    # List of TOTALLY random sentences
    sentences = [
        "The {} quickly jumped over the lazy dog.",
        "Can you {} the recipe for the new dish?",
        "Every morning, the {} sings beautifully.",
        "She decided to {} her dreams and move to a new city.",
        "The {} in the garden bloomed overnight.",
        "I need to {} these documents by tomorrow.",
        "His ability to {} well made him a great leader.",
        "The {} of the forest are filled with mysteries.",
        "You should {} the truth, no matter how hard it is.",
        "The {} was a symbol of hope for the villagers.",
        "Banna was NOT happy with his {}.",
        "Lubaba buried the poor {}.",
        "Hasan was not his last {}.",
        "Greendale is promoting {} again.",
        "She is my {}.",
        "A {} a day keeps the doctor away.",
        "Would you like to {} this book?",
        "The {} sparkled in the sunlight.",
        "How do you {} your coffee?",
        "The {} was lost in thought.",
        "To {} or not to {}, that is the question.",
        "The {} painted a masterpiece.",
        "I want to {} this opportunity.",
        "The {} flew high in the sky.",
        "Do you know how to {}?",
        "The {} stood tall and proud.",
        "She will {} to the music.",
        "The {} was an expert in its field.",
        "He can {} with the best of them.",
        "The {} tasted delicious.",
        "Let's {} to the finish line.",
        "The {} was very informative.",
        "We should {} our plans.",
        "The {} was surprisingly friendly.",
        "I couldn't {} what I saw.",
        "The {} was decorated beautifully.",
        "Do you think you can {} this challenge?",
        "The {} was awarded first place.",
        "Let's {} this puzzle together.",
        "The {} was a hidden gem.",
        "How do you plan to {} this task?",
        "The {} played all night long.",
        "Do you think you can {} in this competition?",
        "The {} danced gracefully.",
        "What do you {} about this idea?",
        "The {} was full of energy.",
        "How can we {} this situation?",
        "The {} was the best I've ever had.",
        "Let's {} to the top of the mountain.",
        "The {} was incredibly brave.",
        "Do you know how to {} this problem?",
        "The {} was celebrated by everyone.",
        "How can we {} this mistake?",
        "The {} shone brightly in the sky.",
        "Can you {} this riddle?",
        "The {} was ancient and wise."
    ]

    while True:
        # Selecting a random sentence and formatting it with the selected word
        sentence = '\n\t"' + random.choice(sentences).format(selected_word) + '"'

        # Printing the sentence with the selected word
        print(f"Here is your sentence: {sentence}")

        # Asking if the user wanna see the word in another sentence
        another_sentence = get_yes_no_input("Would you like to see it in another sentence? (yes/no): ")
        if not another_sentence:
            break

    all_answers["Generated Sentence"] = sentence

    # Asking the user if they wanna take a short survey
    take_survey = get_yes_no_input("Would you like to take a short survey? (yes/no): ")
    all_answers["Take Survey"] = "yes" if take_survey else "no"

    if take_survey:
        survey_answers = survey()
        all_answers.update(survey_answers)

        # Thanking the user and asking if they wanna save their answers
        
        save_answers = get_yes_no_input("Thank you so much for your time! Would you like to save your answers? (yes/no): ")
        if save_answers:
            save_survey(all_answers)
        else:
            print("Thank you! Your answers have not been saved.")
    else:
        print("Thank you! Have a great day.")

if __name__ == "__main__":
    main()

