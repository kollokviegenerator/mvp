
"""
    The unifi command line interface
"""
from mvp.models import Student, Oracle
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db import transaction

class UserManagement:

    """
        Takes care of user management (adding, removing, updating ...)
    """
    def __init__(self):
        pass

    @transaction.commit_manually
    def adduser(self, usr):
        """
            Add a user
            @param usr: the user to be added
        """
        usr = usr.strip() #remove whitespace
        try:
            User.objects.create_user(usr, password="123")
            print "user %s added!" % usr
        except IntegrityError:
            print "User '%s' exists in database." % usr
            transaction.rollback()
            if not User.objects.get(username=usr).is_active:
                print "If the user at some point was deleted "\
                    "you want to do a user restore instead of add"

        finally:
            transaction.commit()

    def deleteuser(self, usr):
        """
            Delete a user (or rather, set the is_active flag to False so
            any foreign keys to users won't break
            @param usr: the user to remove
        """
        usr = usr.strip() #remove whitespace
        try:
            u = User.objects.get(username=usr)
            u.is_active=False
            u.save()

            print "user %s removed (is_active=False)" % usr
        except User.DoesNotExist:
            print "User '%s' does not exists in database." % usr

    @transaction.commit_manually
    def updateuser(self, usr, arg):
        """
            Update an user
            @param usr: the user to update
            @param: arg: info to be updated
        """

        #o - oracle, s - student, r - restore (is_active = True)
        if arg == None or arg[0] not in ['o', 's', 'r', 'student', 'oracle', 'restore']:
            print "Argument must be of type 'o', 's', or 'r', 'student', 'oracle', 'restore'"
            return

        usr = usr.strip()

        try:
            u = User.objects.get(username=usr)
        except User.DoesNotExist:
            print "User '%s' does not exists in database." % usr
            transaction.rollback()
            return

        if arg[0] == 's' or arg[0] == 'student':
            s = Student(user=u)
            s.save()
            print "User %s is now registered as student." % usr
        elif arg[0] == 'o' or arg[0] == 'oracle':
            o = Oracle(user=u)
            o.save()
            print "User %s is now registered as oracle." % usr
        else: #arg is now r
            u.is_active = True
            u.save()
            print "User %s is now restored (is_active=True)." % usr

        transaction.commit()

    def flush(self):
        """
            Removes all entries in the user table (and not just is_active=False)
        """

        User.objects.all().delete()
        print "User table flushed"

