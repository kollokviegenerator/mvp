
"""
    The unifi command line interface
"""
from mvp.models import Student, Oracle
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class UserManagement:

    """
        banana banana banana
    """
    def __init__(self):
        pass

    def adduser(self, usr):
#        print usr
        try:
            User.objects.create_user(usr)
        except IntegrityError:
            print "User '%s' exists!" % usr

#    def delete


