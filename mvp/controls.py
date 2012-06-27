# util

def extract_tags( tag_string ):
    """ Processes a comma-separated tag string,
    @return     a list of tags
    """
    output = []
    output = tag_string.split(",")
    output = [t.strip() for t in output]

    return output

