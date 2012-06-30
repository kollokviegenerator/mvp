
"""
    The unifi command line interface
"""
from mvp.models import Tag
from django.db.utils import IntegrityError
from django.db import transaction

class TagManagement:
    """
        Takes care of tag management (adding, removing, updating ...)
    """
    def __init__(self):
        pass

    @transaction.commit_manually
    def addtag(self, tag):
        """
            Add a user
            @param usr: the user to be added
        """
        tag = tag.strip() #remove whitespace
        try:
            Tag(name_of_tag=tag).save()
            print "tag '%s' added!" % tag
        except IntegrityError:
            print "tag '%s' exists in database." % tag
            transaction.rollback()
        finally:
            transaction.commit()

    def deletetag(self, tag):
        """
            Delete a tag (or rather, set the is_active flag to False so
            any foreign keys to users won't break
            @param usr: the user to remove
        """
        pass

    def flush(self):
        """
            Removes all entries in the tag table (and not just is_active=False)
        """

        Tag.objects.all().delete()
        print "Tag table flushed"
