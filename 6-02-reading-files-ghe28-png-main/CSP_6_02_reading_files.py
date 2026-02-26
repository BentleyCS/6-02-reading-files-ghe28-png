#You must make and submit your own test file and txt file with this assignment.
import os
def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, fileName)
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):

    f=open(fileName)
    longest =0
    for line in f:
        if len(line)>longest:
            longest=line
    return longest
    #Given a file return the longest line from within that file
    pass

def toBinary(fileName):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, fileName)
    f=open(file_path)
    result=[]
    while True:
        byte = f.read(8)
        if len(byte)==0:
            result.append(byte)
    f.close()
    return result

    return fileName
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    pass
