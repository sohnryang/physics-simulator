"""
collision.py -- collision check functions

"""


def box_vs_box(box1, box2):
    """
    Check collision between two boxes.

    """
    if box1.max_p.x < box2.min_p.x or box1.min_p.x > box2.max_p.x:
        return False
    if box1.max_p.y < box2.min_p.y or box1.min_p.y > box2.max_p.y:
        return False
    return True