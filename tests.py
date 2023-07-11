from os import remove

def readtest():
    input_file = open(r"test.txt", "r")
    print(input_file.read())
    input_file.close()
    print("End of readtest")


def writetest():
    file_writer = open(r"output.txt", "w")
    file_writer.write("This is\na new text document")
    file_writer.close()
    file_reader = open(r"output.txt", "r")
    print(file_reader.read())
    file_reader.close()
    print("End of writetest")

def cleanupoutput():
    remove("output.txt")
