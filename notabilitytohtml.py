""" Notability to HTML converter """

import sys

class nreader():
    """ Read and parse Notability format """
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


if __name__ == "__main__":
    main()
