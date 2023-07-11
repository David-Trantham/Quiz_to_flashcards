from tests import *
from answer2flashcard import *
from sys import argv

def runtests():
    print("Hello World")
    readtest()
    writetest()
    cleanupoutput()

def main():
    if len(argv)!=2: raise Exception(
        "Please only include the filepath to quiz results as "+
        "your command line argument!"
    )
    # runtests()
    # initialize_output()
    # first_answer()
    quiz2anki(argv[1])


if __name__ == "__main__":
    main()
