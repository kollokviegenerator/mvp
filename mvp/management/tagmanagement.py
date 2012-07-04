
"""
    The unifi command line interface
"""
from mvp.models import Tag

class TagManagement:
    """
        Takes care of tag management (adding, removing, getting ...)
    """
    def __init__(self):
        pass

    def addtag(self, tag):
        """
            Add a user
            @param usr: the user to be added
        """
        tag = tag.strip() #remove whitespace
        t = Tag.objects.get_or_create(name_of_tag=tag)
        print "tag '%s' added!" % tag
        return t

    def deletetag(self, tag):
        """
            Delete a tag (or rather, set the is_active flag to False so
            any foreign keys to users won't break
            @param usr: the user to remove
        """
        try:
            Tag.objects.get(name_of_tag=name).delete()
        except Tag.DoesNotExist:
            pass

    def getTag(self, name):
        """
        return a tag
        @param name: the name of the tag
        """

        try:
            return Tag.objects.get(name_of_tag=name)
        except Tag.DoesNotExist:
            return None

    def flush(self):
        """
            Removes all entries in the tag table (and not just is_active=False)
        """

        Tag.objects.all().delete()
        print "Tag table flushed"
