#Text_To_Angelic.py

#This code takes in a .txt file, reverses every word in that file, and returns a file next to the input called "[input]_angelic.txt"
#The code is extremely simple by design, so is not resistant to unexpected characters or filetypes.
#To use, call it from the terminal with: python text_to_angelic.py [filepath of target .txt file]
#Example usage: python text_to_angelic.py /Users/name/Desktop/to_reverse.txt

import sys
import string
import os

def flip_words_in_line(line):
    edited_line = []
    #we accept the definition that a word is some letters surrounded by a gap, therefore xnopyt, AAAAAAAAAAAAAAAA--
    for word in line.split(" "):
        for punctuation in ".,!?-–_;—\"\“":
            word = word.replace(punctuation,"")
        edited_line.append(word[::-1].lower())
    edited_line = " ".join(edited_line)
    return edited_line

def convert_texts(filepath, protected_words = []):
    try:
        output_path = filepath[:-4] + "_angelic.txt"
        #output_path = "_angelic.txt"
    except:
        print("Could not parse file")
        exit()
    with open(filepath,"r") as file:
        with open(output_path,"w") as write_file:
            for line in file:
                write_file.write(flip_words_in_line(line.replace("\n", "")))
                write_file.write("\n")

#this is the code that will actually run when the python is executed
if __name__ == "__main__":
    filepath = sys.argv[1]
    convert_texts(filepath)
