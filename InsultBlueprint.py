import functools
import random
import sys
import streamlit as st


def applyto(*args):
    return functools.reduce(lambda l, r: r(l), args)


def read_file(filename):
    content = None
    with open(filename) as fin:
        content = [line.rstrip('\n') for line in fin]
    return content


def combine(*args):
    return [random.choice(arg) for arg in args]


def format_insult(lst):
    return ' '.join(['Thou'] + lst) + '!'


def insult(*args):
    return applyto(
        [read_file(it) for it in list(args)],
        lambda content: combine(*content),
        format_insult
     )

if __name__ == "__main__":
    filenames = ['FILES/w1.txt', 'FILES/w2.txt', 'FILES/w3.txt']
    filenames = sys.argv[1:] or filenames
    st.write(insult(*filenames))
