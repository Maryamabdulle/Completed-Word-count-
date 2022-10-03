"""Count words in file."""
from symbol import compound_stmt


input_file = open("test.txt")
word_counts = {}

for line in input_file:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        word_counts[word]= word_counts.get(word,0)+1
    
for word, count in word_counts.items():
    print(word, count)
    
    


# put your code here.
