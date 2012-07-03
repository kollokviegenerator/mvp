#!/usr/bin/env python2.7

from __future__ import division

def all( a, b ):
    """
    @return     union of elements in 'a' and 'b'
    """
    return ( a | b )

def common( a, b ):
    """
    @return     intersection of elements in 'a' and 'b'
    """
    return ( a & b )

def pair_score( a, b ):
    """
    @return     a score for the wish pair containing 'a' and 'b'
                compared with the whole wish pool
    """
    return len(common( a , b )) / len(all( a, b ))

def wish_score( target, base ):
    """
    @return     a 'target's score for compatibility with 'base'
    """
    return len(common( target, base )) / len( target )



if __name__ == "__main__":
    a = set(["a", "b", "c"])
    b = set(["a", "b", "c", "d", "e"])

    print "Pair scores:"
    print pair_score(a,b)
    print pair_score(b,a)
    print "(should be equal)"
    print "Wish scores:"
    print "a: %f" % wish_score(a,b)
    print "b: %f" % wish_score(b,a)