import numpy as np

# t axis in seconds
(t, deltat) = np.linspace(-10, 10, 5001, retstep=True)  

# Elementary signals
gauss     = lambda t: np.exp(-(t)**2)
unitstep  = lambda t: np.where(t>=0, 1, 0)
rect      = lambda t: unitstep(t+0.5) - unitstep(t-0.5)
tri       = lambda t: rect(t/2)*(1-abs(t))
si        = lambda t: np.sinc(t/np.pi) # English notation sinc(t) = sin(pi t)/(pi t)
rc_tp     = lambda f: 1 / (1 + 1j * 2 * np.pi * f) # RC = 1
rl_hp     = lambda f: (1j * 2 * np.pi * f) / (1 + 1j * 2 * np.pi * f) # RL = 1

eps = np.finfo(float).eps # floating point accuracy


def findIndOfLeastDiff(x, x0):
    """
    Find Index of the value that's nearest to x0

    Parameters
    ----------
    x : array_like
        Array to be inspected

    x0 : digit
        Target value to be searched for

    Returns
    -------
    index : int or list
        index(indices) of value(s) that is (are) nearest to x0
    """
    if isinstance(x0, list) or isinstance(x0, np.ndarray):
        return list(map(lambda t0: np.abs(x - t0).argmin(), x0))
    else:
        return np.abs(x - x0).argmin()
