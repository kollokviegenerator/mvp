#!/usr/bin/env python2.7

from __future__ import division
from math import sqrt

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

def uncommon( a, b ):
    """
    @return     complement of the intersection between 'a' and 'b'
    """
    return ( a ^ b )

def pair_score( a, b ):
    """
    @return     a score for the wish pair containing 'a' and 'b'
                compared with the whole wish pool
    """
    return len(common( a , b )) / len(all( a, b ))

def wish_score( target, base ):
    """
    @return     a 'target's score for compatibility with 'base'
                a ratio of elements that exists in the target,
                compared to number of common elements of the pair
    """
    return len(common( target, base )) / len( target )

def quadratic_score( a, b ):
    return sqrt(wish_score(a,b) * wish_score(b,a))



def pair_equality_ratio( target, base ):
    return len(uncommon(target,base)) / len( common(target, base))

if __name__ == "__main__":
    a = set(["a", "c", "d", "g"])
    b = set(["a", "b"])

    print "Wish scores:"
    print "a: %f" % wish_score(a,b)
    print "b: %f" % wish_score(b,a)

    print "Pair scores:"
    print " by wish pool"
    print pair_score(a,b)
    print pair_score(b,a)
    print "(should be equal)"
    print " comparison"
    print "sqrt(a*b): %f" % ( quadratic_score(a,b) )

    print "Pair equality ratio:"
    print pair_equality_ratio( a,b )
    print pair_equality_ratio( b,a )

    #
    print ( len(all(a,b)) / len(uncommon(a,b)) )
