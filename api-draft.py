import getopt, sys

"""
    Unifi API
"""

class apidraft:

    def __init__(self):
        self.user_management = UserManagement()

    def main(self, argv):
        """
            parse argv and execute the command(s)
        """
        try:
            opts, args = getopt.getopt(argv[1:],
                "hu:g:", ["help", "adduser=", "du=", "deleteuser=", "flushusers"])
        except getopt.GetoptError, err:
            # print help information and exit:
            print str(err) # will print something like "option -f not recognized"
            print "%s --help for usage" % sys.argv[0]
            sys.exit(2)

        if len(opts) == 0:
            print "Remember the '--' before command!"
            sys.exit(1)

        for o, a in opts:
            if o in ("-h", "--help"):
                self.usage()
                sys.exit()
            elif o in ("-u", "--adduser"):
                self.adduser(a)
            elif o in ("-g", "--addgroup"):
                print "adding group dummy text"
            elif o in("--du", "--deleteuser"):
                self.deleteuser(a)
            elif o in("--flushusers"):
                self.user_management.flush()
            else:
                assert False, "unhandled option"

    def adduser(self, in_user):

        """
            Add a user to the database
            @param in_user: the user to be added, can be a file or a single username
        """
        try:
            #argument is a file of users
            f = open(in_user, 'r')
            for usr in f:
                self.user_management.adduser(usr)

            f.close()
        except IOError:
            #Argument is a single user
            self.user_management.adduser(in_user)

    def deleteuser(self, in_user):
        """
            remove a user from the database
            @param in_user: the user to delete
        """

        try:
            #argument is a file of users
            f = open(in_user, 'r')
            for usr in f:
                self.user_management.deleteuser(usr)
        except IOError:
            self.user_management.deleteuser(in_user)


    def usage(self):
        """
        Print usage
        """

        print "Usage: %s [subcommand] [args] \n" % sys.argv[0]
        print "Help:"
        print "    -h --help \tto show this help and exit\n"
        print "Type '%s [subcommand] -h, --help for help on a specific subcommand (not impl. yet)\n"
        print "Available subcommands"
        print "[user]"
        print "\t-u, \t--adduser \t<user>"
        print "\t--du, \t--deleteuser \t<user>"


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
