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

def all_answers(filepath):
    anki_formatted_quiz = "\n"
    quiz = open(filepath, "r")
    quiz.readline() #Have to skip the first line
    thisline = quiz.readline().strip()
    for line in quiz:
        question = ""
        answer = ""
        while (not(thisline.startswith("Your answer"))):
            if thisline.endswith(ANSWER_IDENTIFIER):
                thisline = thisline.removesuffix(ANSWER_IDENTIFIER) + "\n"
                answer += thisline
            if thisline != "\n": question += thisline
            thisline = quiz.readline()
        anki_formatted_quiz += "\""+question+"\"" + ";" + "\""+answer+"\"\n"
        thisline = quiz.readline()
    return anki_formatted_quiz

#I would like this function to accept a filepath and create an output with name based on the tag
def quiz2anki(filepath):
    output_path = initialize_output(filepath)
    output_file = open(output_path, "a")
    output_file.write(all_answers(filepath))
    