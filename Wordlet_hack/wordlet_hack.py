
from ast import Constant
from pathlib import Path
import operator
from tkinter import N

file = Path.home() / 'OneDrive' / '桌面' / 'engmix.txt'
#'OneDrive - VolTra' / 'VolTra Doc (Bird)' / 'Python Learning' / 'Wordlet_hack' / 'test.txt'


# The program is for hacking wordle which have 5-letter words only.
n_words = 5


########################################
########################################
########################################


# check the appering requency of a letter individully
def check_letter_frequency(input_word_list, available_letters):
    check_word_list = input_word_list.copy()
    freq_dict = {}

    # set up the avaliable letters
    for i in available_letters:
        freq_dict[i] = [0] * n_words 


    # count the frequency of a letter in different position of a word. 
    for i in range(n_words):
        for word in check_word_list:
            if word[i] in freq_dict:
                freq_dict[word[i]][i] += 1
    
    return freq_dict

# check the appering pobability of a letter individully
def letter_prob_check(input_dict, input_words_list, word_len):
    check_dict = input_dict.copy()
    total = [0] * n_words

    dict_prob = {}

    for letter in a_to_z:
        dict_prob[letter] = [0] * word_len

    if len(input_words_list) != 0:
        for i in range(word_len):
            for letter in a_to_z:
                total[i] += check_dict[letter][i]
            for letter in a_to_z:
                dict_prob[letter][i] = check_dict[letter][i] / total[i]
    print(dict_prob)
    
    return dict_prob


# check if the words in the text file is all small letter.
def is_allowed_specific_char(string, avaliable_letters):
    is_allowed = True
    for letter in string:
        if letter not in avaliable_letters:
            is_allowed = False
    return is_allowed



# Get the word list from the text file with a desginated word lenght.
def extract_words_from_the_file(file_path, word_len):
    word_list = []

    with file_path.open('r',encoding='utf-8') as f:
        for line in f:
            if len(line) == word_len + 1  and is_allowed_specific_char(line[:word_len], a_to_z):
                word_list.append(line.rstrip('\n'))

    print(len(word_list),' words are in the list.')
    return word_list


# filter the words which have the avalible letters only
def filtering_word_list(inpuit_word_list, available_letter):
    word_list = inpuit_word_list.copy()
    new_word_list = []

    for word in word_list:
        if is_allowed_specific_char(word, available_letter):
                new_word_list.append(word)

    print(len(new_word_list),' words are in the list.')
    return new_word_list

# Output a new word list which have the letter at the confirmed position.
def with_confirmed_letter(word_list, confirmed_position, confirmed_letter):
    old_word_list = word_list.copy()
    new_word_list = []
    for the_word in old_word_list:
        if confirmed_letter == the_word[confirmed_position]:
            new_word_list.append(the_word)

    print(len(new_word_list),'words left which have the letter',confirmed_letter,'at that position.')
    return new_word_list

# Output a new word list which have the letter which not at that position.
def with_exist_letter(word_list, not_at_that_position, exist_letter):
    old_word_list = word_list.copy()
    new_word_list = []
    
    for the_word in old_word_list:
        if (exist_letter in the_word) and (exist_letter != the_word[not_at_that_position]):
            new_word_list.append(the_word)
    
    print(len(new_word_list),'words left which have the letter',exist_letter,'not at that position.')
    return new_word_list


# calculate the probability of each word fulfilling all rules
def check_words_probabilities(input_word_list, input_letter_prob_dict):

    check_word_list = input_word_list.copy()
    check_letter_prob = input_letter_prob_dict.copy()
    total_prob = 0
    
    words_prob = {}
    
    for word in check_word_list:
        words_prob[word] = 1
        for i in range (n_words):
            if word[i] in check_letter_prob:
                words_prob[word] *= check_letter_prob[word[i]][i]
    
    # to normalize the probabilities so that it add up to 100 finally.
    adjusted_words_prob = words_prob.copy()
    total_prob = sum(words_prob.values())
    for word in adjusted_words_prob:
        adjusted_words_prob[word] = words_prob[word]/total_prob

    return adjusted_words_prob


# get the top 10 words with highest probability
def select_most_possible_words(input_words_prob, show_number):
    
    check_words_prob = input_words_prob.copy()
    top_prob = {"": 0}

    if len(check_words_prob) == 0:
        print('There is no word can fulfill all the critira!')

    else:
        for word in check_words_prob:
            min_top_word = min(top_prob, key = top_prob.get)
            if  check_words_prob[word] > top_prob[min_top_word]:
                top_prob[word] = check_words_prob[word]
                if len(top_prob) == show_number:
                    top_prob.pop(min_top_word)

        for word in sorted(top_prob, key=top_prob.get, reverse=True):
            percentage = "{:.4%}".format(top_prob[word])  
            print(word, ":", percentage)
    
        return top_prob
        

#############################################
#############################################

# Main page
    
while True:

    words = []
    a_to_z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    words = extract_words_from_the_file(file, n_words)

    dict = check_letter_frequency(words, a_to_z)

    letter_prob_dict = letter_prob_check(dict, words, n_words)

    words_prob_dict = check_words_probabilities(words, letter_prob_dict)

    top10_words = select_most_possible_words(words_prob_dict,10)


        

    ##############################
    ## Getting user input ########

    word_found = False
    letter_confirmed = ['?'] * n_words
    letter_exist =['?'] * n_words


    while not word_found:
        
        ans_found = input("Have you found the word? (Y/N) ")
        if ans_found == "Y" or ans_found =="y":
            word_found = True
            break
        
        print("current status:", end='')
        print(letter_confirmed)
    
        ans_confirmed = input("Can you confirm any new letter(s)?  ")
        for i in range(len(ans_confirmed)):
            if ans_confirmed[i] != "?":
                letter_confirmed[i] = ans_confirmed[i]
                words = with_confirmed_letter(words, i, ans_confirmed[i])
    

        print("current status:", end='')
        print(letter_exist)

        ans_exist = input("Can you confirm any new letter(s) exist but not at the position?  ")
        for i in range(len(ans_exist)):
            if ans_exist[i] != "?":
                letter_exist[i] = ans_exist[i]
                words = with_exist_letter(words, i, letter_exist[i])
                
    
        
        print("Avaliable letters:", end='')
        print(a_to_z)

        ans_filtered = input("Can you filter out any new letter(s)?")
        if ans_filtered != '':
            for i in ans_filtered:
                if i in a_to_z:
                    a_to_z.remove(i)
            words = filtering_word_list(words, a_to_z)


    ###################################################

        
        
        dict = check_letter_frequency(words, a_to_z)

        letter_prob_dict = letter_prob_check(dict, words, n_words)

        words_prob_dict = check_words_probabilities(words,letter_prob_dict)

        top10_words = select_most_possible_words(words_prob_dict,20)

