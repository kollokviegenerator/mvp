import getopt, sys

"""
    Unifi API
"""

class apidraft:

    def __init__(self):
        self.user_management = UserManagement()
#        self.u = Unifisystem()

    def main(self, argv):
        """
            banana banana banana
        """
        try:
            opts, args = getopt.getopt(argv[1:], "ha:", ["help", "adduser="])
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
                self.usage()
                sys.exit()
            elif o in ("-a", "--adduser"):
                self.adduser(a)
            else:
                assert False, "unhandled option"

    def adduser(self, in_user):



        try:
            #argument is a file of users
            f = open(in_user, 'r')
            for usr in f:
                self.user_management.adduser(usr)
        except:
            #Argument is a single user
            self.user_management.adduser(in_user)


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
        print "type 'python %s -h,  --help'" % sys.argv[0]
        sys.exit(1)


    # Have to set DJANGO_SETTINGS_MODULE when run as standalone program
    # to get access to modules
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'kgen.settings'

    from api.management.usermanagement import UserManagement
    from api.management.tagmanagement import TagManagement
    from api.management.groupmanagement import GroupManagement
    from api.management.wishmanagement import WishManagement

    apidraft = apidraft()
    apidraft.main(sys.argv)
