new_corpus = open('sponjibobu.txt', 'w')

with open('spongebobtext.txt', 'r') as corpus:
    for line in corpus:
        if (line.split(' ')[0]) == "SpongeBob:":
            new_corpus.write(line)

new_corpus.close()
