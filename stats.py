# Get number of words
def countWords(a):
    words = a.split()
    return len(words)


# Count of all chars including non-alphabetical
def countChars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars
