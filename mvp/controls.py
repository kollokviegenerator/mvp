# util

def extract_tags( tag_string ):
    """ Tokenizes a comma-separated string.
    @return     a list of tags
    """
    output = []
    # splits the tag string into tokens
    output = tag_string.split(",")
    # strips empty characters from each tag
    output = [t.strip() for t in output]
    # removes all empty-string from the remaining tags
    output = [t for t in output if t != ""]

    return output

