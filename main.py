from answer2flashcard import *
from sys import argv



def main():
    if len(argv)!=2: raise Exception(
        "Please only include the filepath to quiz results as "+
        "your command line argument!"
    )

    quiz2anki(argv[1])


if __name__ == "__main__":
    main()
