"""Count words in file."""
import sys
filename = sys.argv[1]

word_count = {}

def normalize_word(word):
    word = word.lower()
    normal_word = ""
    acceptable_chars = 'abcdefghijklmnopqrstuvwxyz'
    acceptable_chars = acceptable_chars + "'" + "-"
    for char in word:
        if char in acceptable_chars:
            normal_word = normal_word + char
    return normal_word

def generate_word_count(filename = filename, word_count = word_count):
    """modifies dictionary 'word_count' to count words in filename"""

    word_count = {}

    for line in open(filename):
        line = line.rstrip()
        words = line.split(' ')
        for word in words:
            word = normalize_word(word)
            word_count[word] = word_count.get(word,0) + 1
    
    for word, count in word_count.items():
        print(f"{word} {count}")

generate_word_count()