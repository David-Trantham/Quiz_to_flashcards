import os
QUIZ = "Exam 1001 practice quiz.txt"
ANSWER_IDENTIFIER = " ( Missed)\n"

def initialize_output():
    #TODO: Could also use the tag for filename
    #Open file containing answers and get tag from first line
    get_name = open(QUIZ, "r")
    firstline = get_name.readline()
    tag = firstline.split(" - ")[1].strip()
    get_name.close()
    #generate output file called output.txt
    new_output = open(r"output.txt", "w")
    new_output.write("tags:" + tag)
    new_output.close()
    
def first_answer():
    question = ""
    answer = ""
    quiz = open(QUIZ, "r")
    quiz.readline() #Have to skip the first line
    thisline = quiz.readline().strip()
    while (not(thisline.startswith("Your answer"))):
        if thisline.endswith(ANSWER_IDENTIFIER):
             thisline = thisline.removesuffix(ANSWER_IDENTIFIER) + "\n"
             answer += thisline
        question += thisline
        thisline = quiz.readline()
        print(question + "\n" + answer + "end")

def all_answers():
    quiz = open(QUIZ, "r")
    quiz.readline() #Have to skip the first line
    thisline = quiz.readline().strip()
    for line in quiz:
        question = ""
        answer = ""
        while (not(thisline.startswith("Your answer"))):
            if thisline.endswith(ANSWER_IDENTIFIER):
                thisline = thisline.removesuffix(ANSWER_IDENTIFIER) + "\n"
                answer += thisline
            question += thisline
            thisline = quiz.readline()
        print(question + ";" + answer)
        thisline = quiz.readline()

#I would like this function to accept a filepath and create an output with name based on the tag
def quiz2anki(filepath):
    print(filepath)


