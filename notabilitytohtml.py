""" Notability to HTML converter """

import sys
import plistlib
import zipfile
import os

class nreader():
    """ Read and parse Notability format """

    def __init__(self):
        pass

    def readFile(self, file_name, directory=os.getcwd()):
        self.file_name = file_name
        self.directory = directory

        self.unzipFiles()

    def unzipFiles(self):
        """ Unzip specified file to specified location """
        with zipfile.ZipFile(self.file_name, 'r') as fn:
            fn.extractall(self.directory)
    
    def parsePlst(self):
        pass
    

def displayHelp():
    print ("Arguments:")
    print ("-h Display this help menu")
    print ("-i Input file")
    print ("-o Output file")

def main():
    # Get command line arguments
    if len(sys.argv) < 2:
        displayHelp()

    for arg in sys.argv[1:]:
        print (arg)

def test():
    r = nreader()
    r.readFile("testfile.note")


if __name__ == "__main__":
    #main()
    test()
