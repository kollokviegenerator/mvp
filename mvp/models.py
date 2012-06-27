from django.db import models
from django.contrib.auth.models import User

MAX_TAG_LENGTH = 50
MAX_SUBJECT_NAME_LENGTH = 11

class Person(models.Model):
    """ Generic Person """
    user = models.ForeignKey(User)

    class Meta:
        abstract=True

    def __unicode__(self):
        return self.user.username

class Student(Person):
    """ Student
    Participates in group collaboration.
    """

    test = models.CharField(max_length=10)

class Oracle(Person):
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
    tags     = models.ManyToManyField( "Tag",  )
    students = models.ManyToManyField( Student, null=True )
    oracle   = models.OneToOneField( Oracle, null=True ) # !


class Tag(models.Model):
    """ Tag
    A keyword that describes a certain expertise,
    either possessed by an Oracle or required by a Student.
    """
    keyword = models.CharField( max_length=MAX_TAG_LENGTH, unique=True, null=True )

    def __unicode__(self):
        return self.keyword


class Wish(models.Model):
    """
    """
    student = models.ForeignKey(Student, null=True)
    tags = models.ManyToManyField(Tag)
