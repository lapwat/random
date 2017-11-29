#!/usr/bin/env python
import random

# read word list of 2125 most common english words
words = []
for line in open('word_list.txt', 'rb'):
    word = line.strip().decode('utf-8')
    words.append(word)

# use urandom to pick up 4 random words
r = random.SystemRandom()
password = ' '.join([r.choice(words) for _ in range(4)])

print(password)
