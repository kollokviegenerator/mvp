#!/usr/bin/env python2.7

from __future__ import division
from math import sqrt

class Pool:
    """
    Ordering of pairs given by their index produced out of rating_function

    @param wishes               the list of wishes with at least one tag in each
    @param rating_function      the function that calculates the quality index
                                of each wish pair.
    """
    def __init__( self, wishes, rating_function ):
        self.wishes = wishes
        self.rate = rating_function

    def pair( self ):
        """
        @return     a list of pairs ordered by their quality index (score)
        """
        pass

    def __getitem__( self, index ):
        """
        @return     n-th wish-pair in the list ordered by quality index
        """
        pass


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
        self.A = self.Sample( A, B )
        self.B = self.Sample( B, A )

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

        print len(self.common())
        print len(self.A),len(self.B)

        numerator = 2.0 * len(self.common())
        denominator = 2.0 * len(self.A) * len(self.B) \
                      - (
                            ( len(self.A) + len(self.B) ) * len( self.common() )
                        )

        return numerator / denominator

if __name__ == "__main__":
    a = set(["z", "x", "c"])
    b = set(["z", "x", "d", "e"])

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