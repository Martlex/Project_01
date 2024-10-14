#!/usr/bin/env python3

"""
project_01: 1st project to ENGETO Online Python Academy

author: Martin Alex Urbiš
email: urbis.martin@gmail.com
discord: segen0
"""

""" change log
* 12-10-2024 *
1) bug fix - evaluation individual words (discarding punctuation marks)
2) adjustment of bar graph after fix issue in 1)
3) processing more than 3 text slots in the stack
4) formating of end of program message

* 14-10-2024 *
1) update of text info about number of text slots 
in the stack - variable is used there instead of string literal
"""

# variable declaration
# credentials definition (user, pasword)
credentials: dict = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

login_username: str  # user name for login
login_password: str  # password name for login
login_eval: bool  # return value for login evaluation
analyse_option: str  # option value for main processing
TEXTS: list  # texts to be analyzed
longest: int  # longest word (number of char) in the selected TEXT
option_processing: int  # option selected by user for TEXTS processing
words_len: list = []  # list with lenghts of individual words in selected TEXTS
ident_word: int  # leng of word for indentation
number_text_slots: int = 0  # number texts slots in the stack for option
option_driver: bool = True  # loop driver for option of user's input

TEXTS = [
    """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]

# get number of text slots from the stack
number_text_slots = len(TEXTS)


def credentials_evaluation(username: str, password: str) -> bool:
    """returns True or False depending on whether
    the login has passed or not"""

    for key in credentials:
        if credentials.get(username) == password:
            login_eval = True
            break
        else:
            login_eval = False
    return login_eval


def text_analysis(sentence_container: str) -> tuple:
    """core function for analyze required text via user option"""

    get_word_count: int = 0  #  number of words in analyzed text
    number_titlecase_words: int = 0  #  number of titlecase words
    number_uppercase_words: int = 0  #  number of uppercase words
    number_lowercase_words: int = 0  #  number of lowercase words
    number_numeric_strings: int = 0  #  number of numeric strings
    sum_numeric_stings: int = 0  # sum all the numbers

    # business logic
    get_word_count = len(sentence_container)
    for word in sentence_container:
        if word.istitle():
            number_titlecase_words = number_titlecase_words + 1
        if word.isupper():
            if word.isalpha():
                number_uppercase_words = number_uppercase_words + 1
        if word.islower():
            number_lowercase_words = number_lowercase_words + 1
        if word.isnumeric():
            number_numeric_strings = number_numeric_strings + 1
            sum_numeric_stings = sum_numeric_stings + int(word)

    # outputs from processing
    return (
        get_word_count,
        number_titlecase_words,
        number_uppercase_words,
        number_lowercase_words,
        number_numeric_strings,
        sum_numeric_stings,
    )


def get_word_longest_lengths(words: str) -> int:
    """function to find the longest length in the list"""
    res = max(words, key=len)

    return len(res)


def get_offset_right_side(ident_word: int) -> str:
    """get offset of the right side of the graphic output according to the word length -
    the function returns number of spaces from left side of chart"""
    DEFAULT: int = 17  # constant for offset calculation

    return " " * (DEFAULT - ident_word)


def remove_end_punctuation(item: str) -> str:
    # 07-10-2024, doplneno k odstraneni chyb v grafu
    """remove the punctuation at the end of the word"""

    punctuation: tuple = (",", ".", ":", "?", "!", ";")  # punctation marks for
    # comparison

    punctation_mark: str  # isolated punctation mark from the word
    new_word: (
        str  # the original word modified in case of punctation at the end
    )

    # get last char from the word
    punctation_mark = item[-1]

    if punctuation.count(punctation_mark) == 0:
        # there is no punctuation mark in the word
        new_word = item
    else:
        # remove punctuation
        new_word = item[0 : len(item) - 1]

    return new_word


def input_validation(input: str, number_text_slots: int) -> bool:
    """user's input validation - the input may only be to the extent
    specified in the instructions for selecting the text number to be analyzed
    """

    if input.isalpha():
        return False
    else:
        if int(input) >= 1 and int(input) <= number_text_slots:
            return True
        else:
            return False


# *** main program  ***
# user's login
print(
    "Please, enter your credentials (username, password - use Enter for confirmation of the entry) \n"
)

login_username = input("username: ")
login_password = input("password: ")

# credentials evaluation
if credentials_evaluation(login_username, login_password) is not True:
    print("unregistered user, terminating the program ...")
    exit()

print("----------------------------------------")
print(f"Welcome to the app, {login_username}")
print(f"We have {number_text_slots} texts to be analyzed.")
print("----------------------------------------")

# option for TEXTS processing
while option_driver:
    # analyse_option = input("Enter a number btw. 1 and 3 to select: ")
    analyse_option = input(
        f"Enter a number btw. 1 and {number_text_slots} to select: "
    )

    # check user's input 10-10-2024
    if input_validation(analyse_option, number_text_slots) is True:
        for i in range(1, number_text_slots + 1):
            if int(analyse_option) == i:
                option_processing = i - 1
                option_driver = False
    #  processing of inadmissible input
    else:
        if analyse_option != "end":
            print(
                "Incorrect choice, plese try again or enter 'end' to exit program.\n"
            )
        else:
            print("\nThe program has been terminated by the user.")
            exit()


# selected TEXTS processing
output_formating: tuple  # one row of output
output_formating = text_analysis(TEXTS[option_processing].split())

# text analyse output
print("----------------------------------------")
print(f"There are {output_formating[0]} words in the selected text.")
print(f"There are {output_formating[1]} titlecase words.")
print(f"There are {output_formating[2]} uppercase words.")
print(f"There are {output_formating[3]} lowercase words.")
print(f"There are {output_formating[4]} numeric strings.")
print(f"The sum of all the numbers {output_formating[5]} ")
print("----------------------------------------")
print("LEN|  OCCURENCES        |NR.")
print("----------------------------------------")


# bar chart - word frequencies according to length (chars)
# return length of longest word
longest = get_word_longest_lengths(TEXTS[option_processing].split())

# read data to list
for word in TEXTS[option_processing].split():
    words_len.append(len(remove_end_punctuation(word)))

# final processing & print output
# go thru individual words in the list and return details for bar chart
for i in range(longest):
    spaces_from_left: str = get_offset_right_side(words_len.count(i + 1))
    # output shorter than a double-digit number (for alignment)
    if i + 1 <= 9:
        # filter out words with zero length
        if words_len.count(i + 1) != 0:
            print(
                "",
                i + 1,
                "|",
                "*" * words_len.count(i + 1),
                spaces_from_left,
                "|",
                words_len.count(i + 1),
            )
    # output equal or longer than a double-digit number (for alignment)
    else:
        # filter out words with zero length
        if words_len.count(i + 1) != 0:
            print(
                i + 1,
                "|",
                "*" * words_len.count(i + 1),
                spaces_from_left,
                "|",
                words_len.count(i + 1),
            )

print("\n* Info: zero length words are suppressed in the bar chart.\n")

print("* * * End of Processing * * *\n")
