from vectors import Vector
import math

def test_dot():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert v1.dot(v2) == 32

def test_norm_l2():
    v = Vector([3, 4])
    assert v.norm() == 5

def test_norm_l1():
    v = Vector([-1, 2, -3])
    assert v.norm(type="l1") == 6

def test_norm_inf():
    v = Vector([1, -7, 5])
    assert v.norm(type="inf") == 7

def test_normalize():
    v = Vector([3, 4])
    n = v.normalize()
    assert math.isclose(n.values[0], 0.6)
    assert math.isclose(n.values[1], 0.8)

def test_angle():
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    angle = v1.angle(v2)
    assert math.isclose(angle, math.pi/2)
