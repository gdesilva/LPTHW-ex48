# --Allowed lexicon--
# Direction words: north, south, east, west, down, up, left, right, back
# Verbs: go, stop, kill, eat
# Stop words: the, in, of, from, at, it
# Nouns: door, bear, princess, cabinet
# Numbers: any string of 0 through 9 characters

# Instructions:
# You want to take raw input from the user, carve it into words with split,
# analyze those words to identify their type, and finally make a sentence out
# of them.
#
# This scanner will take a string of raw input from a user and return
# a sentence that's composed of a list of tuples with the (TOKEN, WORD) pairings.
# If a word isn't part of the lexicon then it should still return the WORD but
# set the TOKEN to an error token. These error tokens will tell users they
# messed up.


directions = [
    'north',
    'south',
    'east',
    'west',
    'down',
    'up',
    'left',
    'right',
    'back'
]

verbs = [
    'go',
    'stop',
    'kill',
    'eat'
]

stop = [
    'the',
    'in',
    'of',
    'from',
    'at',
    'it'
]

nouns = [
    'door',
    'bear',
    'princess',
    'cabinet'
]

numbers = xrange(-9999999,9999999)

# TODO: a method to handle different cases - potential is force all input to
# convert to lower case, however this will cause tests to fail.

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None



def scan(inputwords):
    words = inputwords.split()
    word_list = []


    for i in words:
        if i in directions:
            word_list.append(('direction', i))
            print word_list

        elif i in verbs:
            word_list.append(('verb', i))
            print word_list

        elif i in stop:
            word_list.append(('stop', i))
            print word_list

        elif i in nouns:
            word_list.append(('noun', i))
            print word_list

        elif convert_number(i) in numbers:
            word_list.append(('number', convert_number(i)))

        else:
            word_list.append(('error', i))



    return word_list



# for manual testing:
# scan(raw_input('> '))
