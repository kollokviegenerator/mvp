from django.db import models
from django.contrib.auth.models import User

MAX_TAG_LENGTH = 50
MAX_SUBJECT_NAME_LENGTH = 11

class Person(models.Model):
    """Generic Person"""
    user = models.ForeignKey(User)

    class Meta:
        abstract=True

    def __unicode__(self):
        return self.user.username

class Student(Person):
    """Student
    Participates in group collaboration.
    """
    pass

class Oracle(Person):
    """Oracle
    Student with a certain expertise.
    Assigned to one or many groups.
    """
    pass

class Group(models.Model):
    """Group
    Student container.
    Requires assistance from an Oracle.
    """
    tags     = models.ManyToManyField( "Tag",  )
    students = models.ManyToManyField( Student, null=True )
    oracle   = models.OneToOneField( Oracle, null=True ) # !

    def __unicode__(self):
        return ",".join(self.tags)


class Tag(models.Model):
    """Tag
    A keyword that describes a certain expertise,
    either possessed by an Oracle or required by a Student.
    """
    name = models.CharField( max_length=MAX_TAG_LENGTH, unique=True, null=True )

    def __unicode__(self):
        return self.name


class Subject(models.Model):
    """Subject
    A tag that specifies subject of the expertise.
    """

    name = models.CharField( max_length=MAX_SUBJECT_NAME_LENGTH, unique=True, null=True )

    def __unicode__(self):
        return self.name


class Wish(models.Model):
    """
    """
    # student = models.ForeignKey(Student)
    username = models.CharField(max_length=12)
    tags = models.ManyToManyField(Tag)