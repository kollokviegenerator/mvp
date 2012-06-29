
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
            User.objects.create_user(usr)
            print "user %s added!" % usr
#            transaction.commit()
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

            print "user %s removed (is_active=False)" % usr
#            transaction.commit()
        except IntegrityError:
            print "User '%s' exists in database." % usr
#            transaction.rollback()
            if not User.objects.get(username=usr).is_active:
                print "If the user at some point was deleted "\
                    "you want to do a user restore instead of add"

#        finally:
#            transaction.commit()

    def update(self, usr, *args):
        """
            Update an user
            @param usr: the user to update
            @param: args: info to be updated
        """

        pass

    def flush(self):
        """
            Removes all entries in the user table (and not just is_active=False)
        """

        User.objects.all().delete()
        print "User table flushed"

