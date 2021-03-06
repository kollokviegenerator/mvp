from django.db import models
from django.contrib.auth.models import User

MAX_TAG_LENGTH = 50
MAX_SUBJECT_NAME_LENGTH = 11

#class Person(models.Model):
#    """ Generic Person """
#    user = models.ForeignKey(User, unique=True)
#
#    class Meta:
#        abstract=True
#
#    def __unicode__(self):
#        return self.user.username

class Student(models.Model):
    """ Student
    Participates in group collaboration.
    """

    user = models.ForeignKey(User, unique=True)

    def username(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

class Oracle(Student):
    """ Oracle
    Student with a certain expertise.
    Assigned to one or many groups.
    """
    pass

class Group(models.Model):
    """ Group
    Student container.
    Requires assistance from an Oracle.
    """
    tags     = models.ManyToManyField( "Tag" )
    students = models.ManyToManyField( Student, null=True )
    oracle   = models.OneToOneField( Oracle, null=True ) # !

    def __unicode__(self):
        return "Group" #TODO change this


class Tag(models.Model):
    """ Tag
    A keyword that describes a certain expertise,
    either possessed by an Oracle or required by a Student.
    """
    name_of_tag = models.CharField( max_length=MAX_TAG_LENGTH, unique=True, null=True )

    def __unicode__(self):
        return self.name_of_tag

class Wish(models.Model):
    """
    """
    student = models.ForeignKey(Student, null=True)
    tags = models.ManyToManyField(Tag)
    wish_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Wish: " + self.student.__unicode__()

