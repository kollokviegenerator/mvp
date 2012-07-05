#!/usr/bin/env python2.7

from __future__ import division
from itertools import combinations
from math import sqrt

class Pool:
    """
    Ordering of pairs given by their index

    @param wishes               the list of wishes with at least one tag in each
    """
    def __init__( self, wishes ):
        self.wishes = wishes

    def pair( self ):
        """
        @return     a list of pairs ordered by their quality index (score)
        """
        pairs = ( Pair( p[0], p[1] ) for p in combinations( self.wishes, 2 ) )
        return pairs




class Pair:

    class Sample:
        def __init__( self, this, other ):
            self.this = set(this)
            self.other = set(other)

        def __call__( self ):
            return self.this

        def __len__( self ):
            return len( self.this )

        def __rsub__( self, other ):
            return self.this - other

        def __rsub__( self, other ):
            return other - self.this

        def __add__( self, other ):
            return self.this.union( other )

        def __radd__( self, other ):
            return self.__add__( other )

        def common( self ):
            return ( self.this & self.other )

        def uncommon( self ):
            return ( self.this ^ self.other )

        def complement(self):
            return self.other - self.this

        def own(self):
            return self.this - self.other

    def __init__( self, A, B ):
        self.A_wish = A
        self.B_wish = B
        self.A = self.Sample( A.tags.all(), B.tags.all() )
        self.B = self.Sample( B.tags.all(), A.tags.all() )

    def all( self ):
        """
        @return     union av self.A and self.B
        """
        return ( self.A() | self.B() )

    def common( self ):
        return ( self.A() & self.B() )

    def uncommon( self ):
        return ( self.A() ^ self.B() )

    def distance( self, insertion_cost=1, deletion_cost=1 ):
        """
        @return     the distance from A to B, mind that this is not
                    a commutative operation if insertion_cost != deletion_cost
        """
        # for e in a:
        #     if e not in b: # implies deletion from A
        #         score += deletion_cost

        # for e in b:
        #     if e not in a: # implies insertion into A
        #         score += insertion_cost

        return len( self.A.complement() ) * insertion_cost + \
               len( self.B.complement() ) * deletion_cost


    def inverse_distance( self, insertion_cost=1, deletion_cost=1 ):
        return len( self.B.complement() ) * insertion_cost +\
               len( self.A.complement() ) * deletion_cost

    # Similarity indices

    def sorensen_similarity( self ):
        return ( 2.0 * len( self.common()) ) / ( len(self.A) + len(self.B) )

    def tversky_similarity( self, alpha = 0.5, beta = 0.5 ):
        """
        @param alpha
        @param beta
        """
        numerator = len(self.common())
        denominator = len(self.common()) + alpha*len(self.A.own()) + beta*len(self.B.own())
        return numerator / denominator

    def jaccard_similarity( self ):
        return len(self.common()) / \
               len(self.all())

    def mountford_similarity( self ):
        result = 0.0
        numerator = 2.0 * len(self.common())
        denominator = 2.0 * len(self.A) * len(self.B) \
                      - (
                            ( len(self.A) + len(self.B) ) * len( self.common() )
                        )
        try:
            result = numerator / denominator
        except ZeroDivisionError:
            result = 0.0

        return result

if __name__ == "__main__":
    a = set(["z", "x", "c"])
    b = set(["z", "x", "d", "e"])

    from string import ascii_lowercase

#    with open( "results.csv", "w" ) as results:
#        for x in xrange(0, len(ascii_lowercase) -1):
#            p = Pair( set(ascii_lowercase[0]), set(ascii_lowercase[0:x]) )
#
#            results.write(
#                "%f,%f,%f,%f \n" % (
#                    p.sorensen_similarity(),
#                    p.tversky_similarity( alpha=1.0, beta=1.0 ),
#                    p.jaccard_similarity(),
#                    p.mountford_similarity()
#                )
#            )




    c = Pair( a,b )

    out = [
        "Elements missing in A",
        c.A.complement(),
        "Elements missing in B",
        c.B.complement(),
        "Distance from A -> B",
        c.distance( insertion_cost=2, deletion_cost=1 ),
        "Distance from B -> A",
        c.inverse_distance( insertion_cost=2, deletion_cost=1 ),
        "Sorensen index",
        c.sorensen_similarity(),
        "Tversky index",
        c.tversky_similarity(),
        "Jaccard index",
        c.jaccard_similarity(),
        "Mountford index",
        c.mountford_similarity()
    ]

    for line in out:
        print line.__str__()