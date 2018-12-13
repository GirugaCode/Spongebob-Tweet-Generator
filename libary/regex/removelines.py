corpus = open('sponjibobu.txt').read()
corpus = corpus.strip().replace('\n', ' ')

new_corpus = open('finalcorpus.txt', 'w')
new_corpus.write(corpus)
