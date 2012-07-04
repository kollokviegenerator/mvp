
"""
    The unifi API
"""
from mvp.models import Student, Oracle, Wish, Tag, Group

class GroupManagement:
    """
        Takes care of group management
    """

    def __init__(self):
        pass

    def addgroup(self, tags=[], students=[], oracle=None):
        """
            Create a new group
            @param tags: the group tags
            @param students: the students belonging to this group
            @param oracle: the oracle tutoring this group
        """
        group = Group()
        group.save()

        for tag in tags:
            group.tags.add(tag)

        for student in students:
            group.students.add(student)

        if not oracle == None:
            group.oracle = oracle

        return group

    def setoracle(self, oracle, group):
        """
            Assign an oracle to this group
            @param oracle: the oracle
            @param group: the group
        """
        try:
            group.oracle = oracle
        except:
            pass

    def getoracle(self, group):
        """
            Get a groups oracle
            @param group: the group
            @return: the oracle
        """

        return group.oracle

    def getstudents(self, group):
        """
            Get the students on a group
            @param group: the group
            @return: the students
        """

        return group.students

    def gettags(self, group):
        """
            Get the tags on a group
            @param group: the group
            @return: the tags
        """

        return group.tags

    def flushgroups(self):
        """
            Delete all group objects
        """
        Group.objects.all().delete()

