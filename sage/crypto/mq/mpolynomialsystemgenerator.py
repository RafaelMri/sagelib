"""
Abstract base class for generators of MPolynomialSystems.

AUTHOR:
    Martin Albrecht <malb@informatik.uni-bremen.de>
"""

from sage.structure.sage_object import SageObject

class MPolynomialSystemGenerator(SageObject):
    """
    Abstract base class for generators of MPolynomialSystems.
    """

    def __getattr__(self, attr):
        if attr == "R":
            self.R = self.ring()
            return self.R
        else:
            raise AttributeError

    def varformatstr(self, name):
        """
        Return format string for a given name 'name' which is
        understood by print et al.

        Such a format string is used to construct variable
        names. Typically those format strings are somewhat like
        'name%02d%02d' such that rounds and offset in a block can be
        encoded.

        INPUT:
            name -- string
        """
        raise NotImplementedError
        
    def varstrs(self, name, round):
        """
        Return a list of variable names given a name 'name' and an
        index 'round'.

        This function is typically used by self._vars.

        INPUT:
            name -- string
            round -- integer index
        """
        raise NotImplementedError

    def vars(self, name, round):
        """
        Return a list of variables given a name 'name' and an
        index 'round'.

        INPUT:
            name -- string
            round -- integer index
        """
        raise NotImplementedError

    def ring(self):
        """
        Return the ring in which the system is defined.
        """
        raise NotImplementedError

    def block_order(self):
        """
        Return a block term ordering for the equation systems
        generated by self.
        """
        raise NotImplementedError

    def __call__(self, P, K):
        """
        Encrypt plaintext P using the key K.

        INPUT:
            P -- plaintext (vector, list)
            K -- key (vector, list)
        """
        raise NotImplementedError

    def sbox(self):
        """
        Return SBox object for self.
        """
        return self._sbox

    def polynomial_system(self, P=None, K=None):
        """
        Return a tuple F,s for plaintext P and key K where F is an
        MPolynomialSystem and s a dictionary which maps key variables
        to their solutions.
        
        INPUT:
            P -- plaintext (vector, list)
            K -- key (vector, list)
        """
        raise NotImplementedError

    def random_element(self):
        """
        Return random element. Usually this is a list of elements in
        the base field of length 'blocksize'.
        """
        raise NotImplementedError

