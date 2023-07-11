from tests import *
from answer2flashcard import *
import os

def runtests():
    print("Hello World")
    readtest()
    writetest()
    cleanupoutput()

def main():
    # runtests()
    # initialize_output()
    # first_answer()
    # quiz2anki(argv[1])
    fileswithinfolders()
    print("hi there")
    input_files = os.listdir("input")
    for file in input_files:
        filepath = os.fspath("input/"+file)
        quiz2anki(filepath)
        os.rename(filepath, "processed/"+file)

if __name__ == "__main__":
    main()
