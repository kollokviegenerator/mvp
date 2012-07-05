
"""
    The unifi command line interface
"""
from mvp.models import Wish, Student, Tag
from django.contrib.auth.models import User
from usermanagement import UserManagement


class WishManagement:
    """
        Takes care of wish management (adding, removing, updating ...)
    """

    def __init__(self):
        self.user_management = UserManagement()

    def addWish(self, student, tags):
        """
            Add a user
            @param student: the student's thats register a wish
            @param tags: wish tags
        """

        if not tags:
            print "Please specify at least one tag"
            return

        if student.__class__ == str:
            student = student.strip()
            student = self.user_management.getStudent(student)

        w = self.getWish(student, tags)

        if w != None:
            print "Wish for: %s exist" % student
            return w

        w = Wish()
        w.student=student
        w.save()

        for t in tags:
            try:
                t = Tag.objects.get_or_create(name_of_tag=t)
                w.tags.add(t[0])
            except Tag.DoesNotExist:
                print "Tag %s does not exist" % t

        print "Wish added for user %s" % student

        return w

    def deleteWish(self, wish):
        """
            Delete a wish
        """

        wish.delete()

    def getWish(self, student, tags):
        """
            get a wish (and your dream will come true)
            @param student: the students username
            @param tags: a list with tag names
        """

        if student.__class__ == str:
            student = self.user_management.getStudent(student)

        wishes = Wish.objects.filter(student=student)

        for w in wishes:
            wishtags = [t.name_of_tag for t in w.tags.all()]

            if set (wishtags) == set (tags):
                return w

        #If wish found
        return None

    def flush(self):
        """
            Removes all entries in the wish table
        """

        Wish.objects.all().delete()
        print "Wish table flushed"

