import os
ANSWER_IDENTIFIER = " ( Missed)\n"

def initialize_output(filepath): #Returns path to newly init'd file
    #Open file containing answers and get tag from first line
    get_name = open(filepath, "r") 
    firstline = get_name.readline()
    tag = firstline.split(" - ")[1].strip().replace(" ", "_")
    get_name.close()
    #generate output file using tag as the name
    output_path = "output/"+tag+".txt"
    new_output = open(output_path, "w")
    new_output.write("tags:" + tag)
    new_output.close()
    return output_path
    
def first_answer(filepath):
    question = "\n"
    answer = ""
    quiz = open(filepath, "r")
    quiz.readline() #Have to skip the first line
    thisline = quiz.readline().strip()
    while (not(thisline.startswith("Your answer"))):
        if thisline.endswith(ANSWER_IDENTIFIER):
             thisline = thisline.removesuffix(ANSWER_IDENTIFIER) + "\n"
             answer += thisline
        question += thisline
        thisline = quiz.readline()
        print(question + "\n" + answer + "end")

def all_answers(filepath):
    anki_formatted_quiz = "\n"
    quiz = open(filepath, "r")
    quiz.readline() #Have to skip the first line
    thisline = quiz.readline().strip()
    j = 0 #j is for janky (Allows for proper line break only on the first question)
    for line in quiz:
        question = ""
        answer = ""
        i = 0 #Neccesary for line break between question and answer choices
        while (not(thisline.startswith("Your answer"))):
            if j == 1: question += "\n"
            if i == 1: question += "\n"
            if thisline.endswith(ANSWER_IDENTIFIER):
                thisline = thisline.removesuffix(ANSWER_IDENTIFIER) + "\n"
                answer += thisline
            if thisline != "\n": question += thisline
            thisline = quiz.readline()
            i += 1
            j += 1
        anki_formatted_quiz += "\""+question+"\"" + ";" + "\""+answer+"\"\n"
        thisline = quiz.readline()
    return anki_formatted_quiz

#I would like this function to accept a filepath and create an output with name based on the tag
def quiz2anki(filepath):
    print(filepath)
    output_path = initialize_output(filepath)
    output_file = open(output_path, "a")
    output_file.write(all_answers(filepath))
    