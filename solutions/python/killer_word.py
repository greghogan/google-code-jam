#!/usr/bin/env python

from collections import defaultdict

ORD_A = ord('a')

def find_best_word_naive(alphabet, words):
    best_score = 0
    best_word = None

    for choice in words:
        score = 0
        letters_to_match = len(choice)

        # Select all other words with the same length as the chosen word
        other = [word for word in words if word != choice and len(word) == len(choice)]

        for letter in alphabet:
            if letter in choice:
                for i in range(len(choice)):
                    # Only keep words which match choice, both having the letter
                    # or not having the each location
                    if choice[i] == letter:
                        letters_to_match -= 1
                        other = [word for word in other if word[i] == letter]
                    else:
                        other = [word for word in other if word[i] != letter]
                if letters_to_match == 0:
                    # Word completed
                    break
            else:
                # The letter will be skipped if not in any word
                if letter in ''.join(other):
                    score += 1
                    other = [word for word in other if letter not in word]

        if score > best_score or not best_word:
            best_score = score
            best_word = choice

    return best_word


def run_one_naive(alphabet, words):
    # This is a good indication that this algorithm is slow
    return [find_best_word_naive(alphabet, words) for alphabet in alphabets]


class Word:
    def __init__(self, index, word):
        self.index = index
        self.word = word

        # Map the character mask for each letter to an integer;
        # for example caravan and pajamas both map 'a' to 42
        self.chr_count = [0] * 26
        for idx, chr in enumerate(word):
            self.chr_count[ord(chr) - ORD_A] += 1 << idx

    def __repr__(self):
        return self.word


def find_best_word(alphabet, index, bins, score):
    # Recursively find the highest word score from a group of bins

    best_score = -1
    best_word = None

    letter = ord(alphabet[index]) - ORD_A

    # The first time called, chr_count is actually the length of each word in
    # the bin, but this works since length cannot be zero
    for chr_count, bin in bins.iteritems():
        # A mask of zero means no match was found in the word; only add a point
        # if the letter was found in a different word resulting in another bin
        if len(bins) > 1 and chr_count == 0:
            bin_score = score + 1
        else:
            bin_score = score

        if len(bin) == 1:
            bin_word = bin[0]
        else:
            # Recursively find the best word, sub-splitting the current bin
            sub_bins = defaultdict(list)
            for word in bin:
                sub_bins[word.chr_count[letter]].append(word)

            bin_score, bin_word = find_best_word(alphabet, index+1, sub_bins, bin_score)

        # If two words have the same score, choose the word which came first in the list
        if bin_score > best_score or (bin_score == best_score and bin_word.index < best_word.index):
            best_score = bin_score
            best_word = bin_word

    return best_score, best_word


def run_one(alphabets, words):
    # Rather than searching by a nested loop as with the naive solution, divide
    # the words into bins based on length and then each character selection

    # Create Words and divide by length
    bins = defaultdict(list)

    for idx, word in enumerate(words):
        bins[len(word)].append(Word(idx, word))

    # Find the highest scoring word for each alphabet
    best_words = []
    for alphabet in alphabets:
        score, word = find_best_word(alphabet, 0, bins, 0)
        best_words.append(word.word)

    return best_words


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Number of teams
        N, M = [int(i) for i in lines.popleft().split(' ')]

        words = []
        for n in range(N):
            words.append(lines.popleft().rstrip('\r\n'))

        alphabets = []
        for m in range(M):
            alphabets.append(lines.popleft().rstrip('\r\n'))

        best_words = run_one(alphabets, words)

        output.append('Case #{0}: {1}'.format(t + 1, ' '.join(best_words)))

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque([line.rstrip('\r\n') for line in file.readlines()])
        output = run(lines)
        print os.linesep.join(output)
