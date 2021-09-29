import os
import re
import string
import random

from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        # remove [text in here] which includes [Intro] [Chorus] and [Outro]
        text = re.sub(r'\[(.+)\]', ' ', text)

        # this removes excess whitespaces and makes spaces uniform
        # text      that look  like this -> text that looks like this
        text = ' '.join(text.split()) 
        text = text.lower() # makes everything lowercase

        # removes all punctuation as that would make a markov chain impossibly difficult
        # as Hello. and Hello wouldn't be considered equal for example
        text = text.translate(str.maketrans('', '', string.punctuation))

        words = text.split() # make list again 
        return words

def make_graph(words):
    g = Graph()

    previous_word = None

    # for each word
    for word in words:

        # check that word is in the graph, and if not then add it
        word_vertex = g.get_vertex(word)
        # if there was a previeous word, then add an edge if it does not already exit
        if previous_word:
            previous_word.increment_edge(word_vertex)
        # in the graph otherwise increment weight by 1
        # set our word to the previous word and iterate!
        previous_word = word_vertex

    # remember, we want ot generate the probability mappings for each vertex
    # this is a good place to do it before we return the graph, as we possess all
    # the neccesary info already.
    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    
    word = g.get_vertex(random.choice(words)) # pick a random word to start!
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main(artist):
    # step 1: get words from text

    # words = get_words_from_text('Learning/Kylie/Markov_chain/texts/hp_sorcerer_stone.txt')

    # for song lyrics
    words = []
    for song_file in os.listdir('Learning/Kylie/Markov_chain/songs/{}'.format(artist)):

        # Exclude this file, as its not a song text :D
        if song_file == '.DS_Store':
            continue

        song_words = get_words_from_text(f'Learning/Kylie/Markov_chain/songs/{artist}/{song_file}')
        words.extend(song_words)

    # step 2: create a graph from the words
    g = make_graph(words)

    # step 3: get the next word for x number of words (defined by length)
    # step 4: show to user
    composition = compose(g, words, 100)
    return ' '.join(composition)


if __name__ == '__main__':
    artist = 'avicii'
    print('\n')
    print(main(artist))