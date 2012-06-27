import getopt, sys

"""
    API to the system
"""

def main():
    """
        main
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:", ["help", "adduser="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        print "%s --help for usage" % sys.argv[0]
        sys.exit(2)

    if len(opts) == 0:
        print "Remember the '--' before command!"
        sys.exit(1)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-a", "--adduser"):
            adduser(a)
        else:
            assert False, "unhandled option"

def adduser(in_user):

    try:
        #argument is a file of users
        f = open(in_user, 'r')
        for usr in f:
            print "Add: " + usr,
    except:
        #Argument is a single user
        print "Add " + in_user

def usage():
    """
    Print usage
    """

    print "Usage: %s [subcommand] [args] [options]\n" % sys.argv[0]
    print "Options:"
    print "    -h --help \tto show this help and exit\n"
    print "Type '%s [subcommand] -h, --help for help on a specific subcommand\n"
    print "Available subcommands"
    print "[user]"
    print "\t-a, --adduser"


if __name__ == "__main__":
    """
        If run as standalone program
    """
    if len(sys.argv) <= 1:
        usage()
        sys.exit(1)

    main()

