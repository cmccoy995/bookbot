import sys
from stats import countChars, countWords


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookPath = sys.argv[1]
    text = getText(bookPath)
    num_words = countWords(text)
    print(f"Found {num_words} total words")
    chars = countChars(text)
    # Sort dict by values
    sortedChars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    # Remove non alphabetical
    sortedChars = filter(lambda x: x[0].isalpha(), sortedChars)

    for c in sortedChars:
        print(f"{c[0]}: {c[1]}")


# Get number of words
# ef countWords(a):
#   words = a.split()
#   return len(words)
def getText(path):
    with open(path) as f:
        return f.read()


# Count of all chars including non-alphabetical
# ef countChars(text):
#   chars = {}
#   for c in text:
#       lowered  = c.lower()
#       if lowered in chars:
#           chars[lowered] += 1
#       else:
#           chars[lowered] = 1

#   return chars
main()
