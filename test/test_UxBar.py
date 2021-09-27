from py306 import UxBar
import sympy as sp

MAX_ERROR = 1e-6


def test_UxBar_1():
    """
    Evaluates example 1 from one drive notes.
    """
    x = sp.Symbol('x')
    Ni = sp.Matrix([[x], [x**2]])
    N0 = 2
    bar = UxBar(Ni, N0, 20, 1e7, 0.2, 3*x, [0, 50], 12e-6, 100*(1-x/(2*20)))
    assert [abs(bar.q[i] - sp.Matrix([[0.0015750000], [-0.00002250000]])
                [i]) <= MAX_ERROR for i in range(sp.shape(bar.q)[0])]
