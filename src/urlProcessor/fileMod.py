import os
import sys
file = os.path.dirname(__file__) + '/../text.txt'

class FileMod:

    def erase_file(self):
        # erase the file contents if already written to
        open(file, 'w').close()

    def write_file(self, chunks):
        with open(file, "a+", encoding="utf-8") as f:
            for chunk in chunks:
                if(len(chunk)!=0):
                    f.write(str(chunk) + " ")


    def read_file(self):
        return file