
"""
    The unifi command line interface
"""
from mvp.models import Wish, Student, Tag
from django.db.utils import IntegrityError
from django.db import transaction
from django.contrib.auth.models import User

class WishManagement:

    """
        Takes care of wish management (adding, removing, updating ...)
    """
    def __init__(self):
        pass

    @transaction.commit_manually
    def addwish(self, student, tags):
        """
            Add a user
            @param usr: the user to be added
        """

        if not tags:
            print "Please specify at least one tag"
            return

        student = student.strip()
        try:
            s = Student.objects.get(user=User.objects.get(username=student))

            w = Wish()
            w.student=s
            w.save()
            for t in tags:
                try:
                    t = Tag.objects.get(name_of_tag=t)
                    w.tags.add(t)
                except Tag.DoesNotExist:
                    print "Tag %s does not exist" % t

            print "Wish added"
        except Student.DoesNotExist: #Can't find student
            print "User '%s' is not registered as a student" % student
            transaction.rollback()
        except User.DoesNotExist: #Can't even find the user
            print "Student '%s' does not exists in database." % student
            transaction.rollback()
        finally:
            transaction.commit()

    def deletewish(self, usr):
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

    def flush(self):
        """
            Removes all entries in the wish table (and not just is_active=False)
        """

        Wish.objects.all().delete()
        print "Wish table flushed"

