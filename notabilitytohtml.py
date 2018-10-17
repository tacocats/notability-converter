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
        """ Unzips the file, parses it, turns information into a structure. """
        self.file_name = file_name
        self.directory = directory

        self.unzipFiles()
        self.parsePlistFiles(os.path.join(self.directory, file_name.split(".note")[0]))

    def unzipFiles(self):
        """ Unzip specified file to specified location """
        with zipfile.ZipFile(self.file_name, 'r') as fn:
            fn.extractall(self.directory)
    
    def parsePlistFiles(self, d):
        """ Parses the plist files """
        for subdir, dirs, files in os.walk(d):

            # Loop through the files
            for f in files:
                try:
                    # Check extention on the file
                    ext = f.split('.')[1]
                    if ext == 'plist':

                       # Open it and parse it
                        try:
                            with open(os.path.join(d,subdir, f), 'rb') as fp:
                                print(os.path.join(d,subdir, f))
                                pl = plistlib.load(fp)
                        except plistlib.InvalidFileException:
                            pass

                except IndexError:
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
    r.readFile("Notes chapter 3.3 to 3.4.note")


if __name__ == "__main__":
    #main()
    test()
