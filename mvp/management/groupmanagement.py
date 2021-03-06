
"""
    The unifi API
"""
from mvp.models import Student, Oracle, Wish, Tag, Group
from usermanagement import UserManagement

class GroupManagement:
    """
        Takes care of group management
    """

    def __init__(self):
        self.user_management = UserManagement()

    def addGroup(self, tags=[], students=[], oracle=None):
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
            if not student == None:
                group.students.add(student)

        if not oracle == None:
            group.oracle = oracle

        return group

    def setOracle(self, oracle, group):
        """
            Assign an oracle to this group
            @param oracle: the oracle
            @param group: the group
        """
        try:
            group.oracle = oracle
        except:
            pass

    def getOracle(self, group):
        """
            Get a groups oracle
            @param group: the group
            @return: the oracle
        """

        return group.oracle

    def getStudents(self, group):
        """
            Get the students on a group
            @param group: the group
            @return: the students
        """

        return group.students

    def getTags(self, group):
        """
            Get the tags on a group
            @param group: the group
            @return: the tags
        """

        return group.tags

    def getGroups(self, student):
        """
            Get all groups that a student is part of
            @param student: the student
            @return: a set of groups
        """

        #if student is a string, get the student object
        student = self.user_management.getStudent(student)
        print student
        groups = []

        return [group for group in Group.objects.all() if student in group.students.all()]


    def flushGroups(self):
        """
            Delete all group objects
        """
        Group.objects.all().delete()

