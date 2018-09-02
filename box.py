"""
box.py -- a box

"""

from point import Point

class Box:
    """
    Box -- a box

    """
    def __init__(self, min_p, max_p):
        """
        Initalize a box.

        """
        self.min_p = min_p
        self.max_p = max_p