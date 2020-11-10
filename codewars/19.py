"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

def high(x):
    temp=0
    letters=" abcdefghijklmnopqrstuvwxyz"
    letter_list=list(x.split())
    for letter in letter_list:
        v=0
        for l in letter:
            v+=letters.index(l,0)
        if v>=temp:
            temp=v
            letter_dict={temp:letter}

    return letter_dict[temp]




print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
    # Code here