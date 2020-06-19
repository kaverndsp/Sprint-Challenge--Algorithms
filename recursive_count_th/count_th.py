'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:  # base case
        return 0

    elif word[0:2] == 'th':
        # See if at 0 - 2 index, there is 'th' in the word. If there is, return + 1 and recurse that index back
        return 1 + count_th(word[2:])

    else:
        # If no 'th' is found, recurse by removing one index
        return count_th(word[1:])
