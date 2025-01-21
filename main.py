def main():
    bookPath = "books/frankenstein.txt"
    text = getText(bookPath)
    num_words = countWords(text)
    print(f"{num_words} found in the document")
    chars = countChars(text)
    #Sort dict by values
    sortedChars = sorted(chars.items(), key = lambda x:x[1], reverse=True)
    #Remove non alphabetical
    sortedChars = filter(lambda x: x[0].isalpha(),  sortedChars)
    for c in sortedChars:
        print(f"The '{c[0]}' character was found {c[1]} times")
#Get number of words
def countWords(a):
    words = a.split()
    return len(words)
def getText(path):
    with open(path) as f:
        return f.read()
#Count of all chars including non-alphabetical
def countChars(text):
    chars = {}
    for c in text:
        lowered  = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars
main()
